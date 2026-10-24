# Runbook — Konten Harian Motion Graphic Naik Kelas HQ

Video edukasi/motivasi 9:16, ±30 detik, faceless, dark navy (brand `nkhq`), suara Gemini **Achernar**, caption karaoke.
Diposting ke Instagram @naik_kelas_id (Reels) + Threads @naikkelas_hq lewat Buffer.

## Environment (wajib di-export di setiap command)
```
export HF_HUB_DISABLE_XET=1   # xet CDN HuggingFace diblokir proxy
export HYPERFRAMES_BROWSER_PATH=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-*/*headless*shell | grep -v '\.' | head -1)  # download Chrome diblokir
```
Cek path headless_shell dengan `ls /opt/pw-browsers/` kalau versinya berubah.

## Langkah
1. `bash studio/setup.sh` → ~/studio-video siap.
2. API key Gemini **tidak** disimpan di repo ini (repo publik). Ambil dari instruksi task, simpan: `umask 077 && printf 'GEMINI_API_KEY=%s\n' '<key>' > ~/studio-video/.env.gemini`
3. Tulis naskah 55–70 kata ke `work/naskah.txt` (hook ≤3 detik, 1 ide per kalimat, penutup "Simpan konten ini..."). Tanpa angka/regulasi/klaim karangan.
4. Suara: `set -a; . ./.env.gemini; set +a; python3 tts_gemini.py work/naskah.txt work/voice.wav Achernar "perempuan muda Indonesia, suara halus, lembut dan hangat, enak didengar, tempo santai dan jelas. Singkatan dieja per huruf."`
5. Timestamp: `python3 transcribe_words.py work/voice.wav work/naskah.txt work/words.json small` → harus "matched" = jumlah kata.
6. Komposisi: salin pola `contoh/tanda_akreditasi.py` → `work/<slug>.py` (6–8 scene, kartu UI/mockup, tiap elemen dikunci ke kata via `v.at()`), header teks "NAIK KELAS HQ".
   `HYPERFRAMES_SKIP_SKILLS=1 npx hyperframes init proj_<slug> --example blank --resolution portrait --skip-transcribe --non-interactive`
   `python3 work/<slug>.py work/words.json work/voice.wav proj_<slug> portrait nkhq`
7. Render: `cd proj_<slug> && npx hyperframes render -o renders/final.mp4` (±3 menit). QC: ambil 9 frame dengan ffmpeg, Read, cek teks terpotong/tumpang tindih/keluar layar. Perbaiki lalu render ulang.
8. Simpan ke repo: `konten/YYYY-MM-DD-<slug>.mp4` + thumbnail `.jpg`, tambah baris di `konten/LOG.md`, commit & push ke main. URL publik: `https://raw.githubusercontent.com/naikkelashq-cmyk/adsvideo/main/konten/<file>`
9. Buffer (org "My organization"): Instagram channel `6ad5cdc9778b240e2f55b00a` (reel, shouldShareToFeed true) + Threads channel `6ad5d2fa778b240e2f55ea40` (post, tanpa hashtag), mode customScheduled, dueAt hari ini 15:00:00+07:00.

## Pelajaran
- Decoder PyAV faster-whisper error → transcribe_words.py sudah decode via ffmpeg.
- `render.sh draft` bisa gagal diam-diam; jalankan `npx hyperframes render` langsung kalau perlu lihat error.
- Elemen dekat tepi kanan (cap/stamp) sering keluar layar — beri `right:30px`, bukan nilai negatif.
- Path headless shell sekarang `chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell` (export di atas mencarinya otomatis).
- `pip install` di setup.sh bisa macet tanpa output (-q); kalau >3 menit, kill lalu jalankan ulang tanpa `-q`.

---

# Carousel Harian (tayang 10:00 WIB)

Carousel IG 4:5 (1080x1350), 7 slide: sampul + teaser, 5 slide poin (kartu "Yang sering terjadi" / "Lakukan ini"), penutup ajakan komentar + simpan/bagikan.

1. Tulis spec JSON (pola: `studio/contoh/carousel_spo.json`; `cover.teaser: true`). Judul poin ≤ 32 karakter, teks kartu ≤ 95 karakter.
   Variasikan format lewat "bad_label"/"good_label" (mis. "✕ Mitos"/"✓ Fakta", "✕ Sebelum"/"✓ Sesudah", "⚠ Tanda bahaya"/"✓ Langkah aman"). Jumlah poin 3–6.
2. Render: `python3 studio/carousel.py spec.json out/` (Playwright + Chromium /opt/pw-browsers/chromium). Read tiap slide untuk QC: tidak ada teks terpotong/tumpang tindih/mepet header.
3. Simpan ke `konten/carousel/YYYY-MM-DD-<slug>-NN.jpg`, tambah baris di `konten/LOG_CAROUSEL.md`, commit & push, cek URL raw status 200.
4. Buffer: Instagram `6ad5cdc9778b240e2f55b00a` metadata instagram type "post", shouldShareToFeed true, assets = 7 image (urut, altText singkat per slide).
   Threads `6ad5d2fa778b240e2f55ea40` type "post", assets sama, caption tanpa hashtag. customScheduled dueAt T10:00:00+07:00.
