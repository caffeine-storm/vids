from manim import *

from typing import List

caffeine_green = ManimColor("#00FF00")
memory_yellow = ManimColor("#FFFF00")

class MemoryCell(VMobject):
    def __init__(self, addr: int, width, height):
        super().__init__()
        self.add(Text(str(addr), color=memory_yellow, font_size=12, font='Source Code Pro'))
        self.add(Rectangle(width=width, height=height, color=caffeine_green))

    def realign(self, target, direction):
        self.submobjects[1].align_to(target, direction)
        self.submobjects[0].next_to(self.submobjects[1], LEFT * 0.5)

# TODO: should we just use https://pypi.org/project/manim-dsa/ ?
class MemoryLadder(VGroup):
    def __init__(self, width:int, height:int, labels:List[int]):
        super().__init__()
        self.labels = labels
        self.cells = list()
        cells = VGroup()
        for label in labels:
            cell = MemoryCell(addr=label, height=height/len(labels), width=width)
            self.cells.append(cell)
            cells += cell

        cells.arrange(DOWN, buff=0)

        baseline = self.cells[0].submobjects[1]
        for cell in self.cells:
            cell.realign(baseline, LEFT)

        self.add(cells)

def label_constructor(*args, **kwargs):
    kwargs['color'] = caffeine_green
    return MathTex(*args, **kwargs)

class Memory(Scene):
    def construct(self):
        kwargs = {
            'x_range': [-8, 8, 1],
            'unit_size': 0.25,
            'font_size': 12,
            'color': caffeine_green,
        }

        dashl = NumberLine(**kwargs)

        kwargs['include_numbers'] = True
        kwargs['label_constructor'] = label_constructor
        nl = NumberLine(**kwargs)

        kwargs['x_range'] = [0, 16, 1]
        posl = NumberLine(**kwargs)

        kwargs['rotation'] = -PI/2
        kwargs['label_direction'] = LEFT
        kwargs['unit_size'] = 0.45
        vertl = NumberLine(**kwargs)

        mem = MemoryLadder(vertl.width*6, vertl.height, list(range(16)))

        self.play(Create(dashl))  # animate the creation of the numberline
        self.play(Transform(dashl, nl, replace_mobject_with_target_in_scene=True))
        self.pause(2)
        self.play(Transform(nl, posl, replace_mobject_with_target_in_scene=True))
        self.pause(2)
        self.play(Transform(posl, vertl, replace_mobject_with_target_in_scene=True))
        self.pause(2)
        self.play(Transform(vertl, mem), replace_mobject_with_target_in_scene=True)
        self.pause(5)
        self.play(FadeOut(mem))  # fade out animation
