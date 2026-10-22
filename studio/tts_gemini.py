"""Langkah 2 (versi asli di postingan): naskah -> suara pakai Gemini TTS.
Syarat: pip install "google-genai>=2.25.0"  dan  env GEMINI_API_KEY berisi API key dari aistudio.google.com/apikey
Pemakaian: python3 tts_gemini.py naskah.txt voice.wav [nama_voice] [gaya]
"""
import base64, sys
from google import genai

naskah, out = sys.argv[1], sys.argv[2]
voice = sys.argv[3] if len(sys.argv) > 3 else "Charon"          # Informative; coba juga Puck / Kore / Sadaltager
style = sys.argv[4] if len(sys.argv) > 4 else "energik, santai, seperti kreator konten Indonesia"

client = genai.Client()  # baca GEMINI_API_KEY dari environment
interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",                                  # lebih murah: gemini-3.8-flash-lite-tts
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": open(naskah).read().strip(),
            "annotations": [{"type": "speech_metadata", "style": style}],
        }],
    }],
    response_format={"type": "audio"},                             # default WAV 24 kHz mono
    generation_config={"speech_config": [{"voice": voice}]},
)
open(out, "wb").write(base64.b64decode(interaction.output_audio.data))
print("tersimpan:", out)
