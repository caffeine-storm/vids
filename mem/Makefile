all: it

PREVIEW=media/videos/main/854p15/Memory.mp4

it: ${PREVIEW}

${PREVIEW}: main.py manim.cfg
	manim --resolution 480,854 --fps 15 ./main.py

go: ${PREVIEW}
	mpv ${PREVIEW}

.PHONY: go
