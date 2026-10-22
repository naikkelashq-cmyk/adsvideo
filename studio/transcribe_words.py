"""Langkah 3: faster-whisper -> timestamp per kata (words.json).
Pakai naskah asli sebagai acuan ejaan: kata hasil whisper disejajarkan ke kata naskah.
"""
import json, re, sys
from difflib import SequenceMatcher
from faster_whisper import WhisperModel

audio, naskah_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
model_size = sys.argv[4] if len(sys.argv) > 4 else "small"

import subprocess, numpy as np
# Decode audio via ffmpeg (16 kHz mono float) — lebih aman daripada decoder bawaan
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                     capture_output=True, check=True).stdout
samples = np.frombuffer(pcm, dtype=np.float32)

model = WhisperModel(model_size, device="cpu", compute_type="int8")
segments, _ = model.transcribe(samples, language="id", word_timestamps=True,
                               initial_prompt=open(naskah_path).read())
heard = [w for s in segments for w in s.words]

def norm(t): return re.sub(r"[^\w]", "", t.lower())
script_words = open(naskah_path).read().split()

# Sejajarkan kata naskah dengan kata yang didengar whisper
sm = SequenceMatcher(a=[norm(w) for w in script_words], b=[norm(w.word) for w in heard], autojunk=False)
mapping = {}
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
        for k in range(i2 - i1):
            mapping[i1 + k] = heard[j1 + k]
    elif tag == "replace":  # beda jumlah kata: bagi rentang waktu rata
        start, end = heard[j1].start, heard[j2 - 1].end
        step = (end - start) / (i2 - i1)
        for k in range(i2 - i1):
            mapping[i1 + k] = type("W", (), {"start": start + k * step, "end": start + (k + 1) * step})

result, last_end = [], 0.0
for i, w in enumerate(script_words):
    h = mapping.get(i)
    s, e = (h.start, h.end) if h else (last_end, last_end + 0.25)
    result.append({"word": w, "start": round(s, 3), "end": round(e, 3)})
    last_end = e

json.dump(result, open(out, "w"), ensure_ascii=False, indent=1)
print(f"{len(result)} kata, matched {len(mapping)}; terakhir selesai {last_end:.2f}s")
