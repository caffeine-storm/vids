all: it

PREVIEW=media/videos/main/854p15/Memory.mp4

it: ${PREVIEW}

${PREVIEW}: main.py manim.cfg
	manim --resolution 480,854 --fps 15 ./main.py

go: ${PREVIEW}
	ffplay -loglevel 0 -autoexit ${PREVIEW}

debug: debug.py manim.cfg
	manim render --resolution 480,854 debug.py
	feh media/images/debug/DebugImg_ManimCE_v0.19.0.png

.PHONY: go debug
