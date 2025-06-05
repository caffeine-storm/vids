from manim import *

from typing import List

caffeine_green = ManimColor("#00FF00")
memory_yellow = ManimColor("#FFFF00")

def MemoryText(txt, **kwargs):
    args = {
        'color': caffeine_green,
        'font_size': 16,
        'font': 'Source Code Pro',
    }
    args.update(kwargs)
    return Text(txt, **args)

class MemoryCell(VMobject):
    def __init__(self, addr: int, width, height):
        super().__init__()
        self.addressLabel = Text(str(addr), color=memory_yellow, font_size=14, font='Source Code Pro')
        self.add(self.addressLabel)

        self.box = Rectangle(width=width, height=height, color=caffeine_green)
        self.add(self.box)
        self.value = MemoryText(" ")
        self.value.move_to(self.box)
        self.add(self.value)

        self.addressLabel.next_to(self.box, LEFT * 0.5)

    def Realign(self, target, direction):
        self.box.align_to(target, direction)
        print(f"realign: from: {self.value.get_center()} to: {self.box.get_center()}")
        self.value.move_to(self.box)

    def Assign(self, value):
        newtext = MemoryText(str(value))
        newtext.move_to(self.box)

        print(f"assign: from: {self.value.get_center()} to: {newtext.get_center()}")

        # TODO: for some reason, the old text is at the origin instead of lined
        # up with the box? I'd rather that new values 'appear' in the cells
        # instead of move to them.
        return self.value.animate.become(newtext)

# TODO: should we just use https://pypi.org/project/manim-dsa/ ?
class MemoryLadder(VGroup):
    def __init__(self, width:int, height:int, labels:List[int]):
        super().__init__()
        self.labels = labels
        self.cells = VGroup()
        for label in labels:
            self.cells += MemoryCell(addr=label, width=width, height=height/len(labels))

        self.cells.arrange(DOWN, buff=0)

        baseline = self.cells[0].box
        for cell in self.cells:
            cell.Realign(baseline, LEFT)

        self.add(self.cells)

    def __len__(self):
        return len(self.labels)

    def ReplaceNumLine(self, nl: NumberLine):
        return Transform(nl, self, replace_mobject_with_target_in_scene=True)

    def Assign(self, data):
        animations = list()
        for i, val in enumerate(data):
            animations.append(self.cells[i].Assign(val))
        return LaggedStart(*animations, lag_ratio=0.07)

    def ForEach(self, fn):
        for i, (label, cell) in enumerate(zip(self.labels, self.cells)):
            yield fn(idx=i, label=label, cell=cell)

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

        mem = MemoryLadder(vertl.width*6, vertl.height, list(range(17)))

        self.play(Create(dashl))  # animate the creation of the numberline
        self.play(Transform(dashl, nl, replace_mobject_with_target_in_scene=True))
        self.pause(2)
        self.play(Transform(nl, posl, replace_mobject_with_target_in_scene=True))
        self.pause(2)
        self.play(Transform(posl, vertl, replace_mobject_with_target_in_scene=True))
        self.pause(2)
        self.play(mem.ReplaceNumLine(vertl))
        self.pause(2)

        memcontents = list("hello world!\n")
        memcontents.extend(['\0' for _ in range(len(mem)-len(memcontents))])
        memcontents = list(map(ord, memcontents))
        self.play(mem.Assign(memcontents))
        self.pause(2)

        self.play(LaggedStart(mem.ForEach(lambda cell, **kwargs: Wiggle(cell, rotation_angle=0)), lag_ratio=0.07, run_time=2))

        self.pause(2)
        self.play(LaggedStart(mem.ForEach(lambda cell, **kwargs: Wiggle(cell.value, rotation_angle=0, scale_value=1.7)), lag_ratio=0.07, run_time=2))

        self.pause(2)
        self.play(LaggedStart(mem.ForEach(lambda cell, **kwargs: Wiggle(cell.addressLabel, rotation_angle=0, scale_value=1.7)), lag_ratio=0.07, run_time=2))

        self.pause(2)
        self.play(FadeOut(mem))
