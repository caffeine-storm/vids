from manim import *

class Memory(Scene):
	def construct(self):
		dashl = NumberLine(
			x_range=[-8, 8, 1],
			unit_size=0.25,
			font_size=12,
		)
		nl = NumberLine(
			x_range=[-8, 8, 1],
			unit_size=0.25,
			include_numbers=True,
			font_size=12,
		)

		posl = NumberLine(
			x_range=[0, 16, 1],
			unit_size=0.25,
			include_numbers=True,
			font_size=12,
		)

		# self.add(nl)
		#circle = Circle()  # create a circle
		#circle.set_fill(PINK, opacity=0.5)  # set color and transparency

		#square = Square()  # create a square
		#square.flip(RIGHT)  # flip horizontally
		#square.rotate(-3 * TAU / 8)  # rotate a certain amount

		#self.play(Transform(square, circle))  # interpolate the square into the circle
		self.play(Create(dashl))  # animate the creation of the graph
		self.play(Transform(dashl, nl, replace_mobject_with_target_in_scene=True))
		self.pause(2)
		self.play(Transform(nl, posl, replace_mobject_with_target_in_scene=True))
		self.pause(5)
		self.play(FadeOut(posl))  # fade out animation
