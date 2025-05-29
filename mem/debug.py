from manim import *
from main import MemoryCell

class DebugImg(Scene):
    def construct(self):
        print("self.cam.width/height:", self.camera.pixel_width, self.camera.pixel_height)
        w = self.camera.pixel_width * 0.8
        h = self.camera.pixel_height * 0.8
        cell = MemoryCell(addr=12, width=2.7495840000000036)
        self.add(cell)
