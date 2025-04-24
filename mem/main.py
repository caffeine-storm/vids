from manim import *

from typing import List

class MemoryLadder(VGroup):
    def __init__(self, width, height, labels:List[int]):
        super().__init__()
        self.labels = labels
        grid = Rectangle(height=height, width=width, grid_ystep=height/len(labels))
        self.add(grid)

class Memory(Scene):
    def construct(self):
        kwargs = {
            'x_range': [-8, 8, 1],
            'unit_size': 0.25,
            'font_size': 12,
            'color': ManimColor("#00FF00"),
        }

        dashl = NumberLine(**kwargs)

        kwargs['include_numbers'] = True
        nl = NumberLine(**kwargs)

        kwargs['x_range'] = [0, 16, 1]
        posl = NumberLine(**kwargs)

        kwargs['rotation'] = -PI/2
        kwargs['label_direction'] = LEFT
        kwargs['unit_size'] = 0.45
        vertl = NumberLine(**kwargs)

        mem = MemoryLadder(vertl.width*3, vertl.height, vertl.get_tick_marks())

        self.play(Create(dashl))  # animate the creation of the numberline
        self.play(Transform(dashl, nl, replace_mobject_with_target_in_scene=True))
        self.pause(2)
        self.play(Transform(nl, posl, replace_mobject_with_target_in_scene=True))
        self.pause(2)
        self.play(Transform(posl, vertl, replace_mobject_with_target_in_scene=True))
        self.pause(2)
        self.play(Transform(vertl, mem))
        self.pause(2)
        #self.play(FadeOut(vertl))  # fade out animation
