#!/usr/bin/env bash
# Pemakaian: bash render.sh <folder_proyek> draft            -> render cepat + contact sheet QC (qc_sheet.png)
#            bash render.sh <folder_proyek> final "<Nama>"   -> render kualitas final ke renders/<Nama>.mp4
set -e
P="$1"; MODE="${2:-draft}"; NAMA="${3:-Video}"
cd "$P"
npx hyperframes lint 2>&1 | grep -E "error\(s\)|✗" || true
if [ "$MODE" = "draft" ]; then
  npx hyperframes render -o renders/_draft.mp4 -q draft --quiet >/dev/null 2>&1
  DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 renders/_draft.mp4)
  W=$(ffprobe -v error -select_streams v -show_entries stream=width -of csv=p=0 renders/_draft.mp4)
  H=$(ffprobe -v error -select_streams v -show_entries stream=height -of csv=p=0 renders/_draft.mp4)
  N=9; ARGS=""; FILT=""
  for i in $(seq 0 $((N-1))); do
    T=$(python3 -c "print(round($DUR*($i+0.6)/$N,2))")
    ffmpeg -v error -y -ss $T -i renders/_draft.mp4 -frames:v 1 -vf "scale=360:-2,drawtext=text='${T}s':x=10:y=10:fontsize=22:fontcolor=yellow" /tmp/qc_$i.png 2>/dev/null \
      || ffmpeg -v error -y -ss $T -i renders/_draft.mp4 -frames:v 1 -vf scale=360:-2 /tmp/qc_$i.png
    ARGS="$ARGS -i /tmp/qc_$i.png"
  done
  ffmpeg -v error -y $ARGS -filter_complex "[0][1][2]hstack=3[a];[3][4][5]hstack=3[b];[6][7][8]hstack=3[c];[a][b][c]vstack=3" ../qc_sheet.png
  echo "DRAFT OK: durasi ${DUR}s, ${W}x${H}. Cek gambar: $(cd .. && pwd)/qc_sheet.png"
else
  rm -f renders/_draft.mp4
  npx hyperframes render -o "renders/$NAMA.mp4" --quiet >/dev/null 2>&1
  echo "FINAL: $(pwd)/renders/$NAMA.mp4"
fi
