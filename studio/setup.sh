#!/usr/bin/env bash
# Pasang studio video Naik Kelas HQ (sekali per sesi). Jalankan: bash studio/setup.sh  -> menyiapkan ~/studio-video
set -e
SRC="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/studio-video/work && cp "$SRC"/*.py "$SRC"/render.sh ~/studio-video/ && cp -r "$SRC"/contoh ~/studio-video/
cd ~/studio-video
export HF_HUB_DISABLE_XET=1
pip install --break-system-packages -q "google-genai>=2.25.0" faster-whisper pillow 2>&1 | grep -v WARNING || true
[ -f package.json ] || npm init -y >/dev/null
npm i -s hyperframes@latest gsap@3.14.2 >/dev/null 2>&1
python3 -c "from faster_whisper import WhisperModel; WhisperModel('small', device='cpu', compute_type='int8')"
echo "STUDIO SIAP"
