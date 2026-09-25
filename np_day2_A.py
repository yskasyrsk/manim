from manim import *
import numpy as np


def math_to_scene(axes, x,y):
    """x , y arrays (N,) returs (N,3)"""

    x  = np.asarray(x, dtype = float)
    y = np.asarray(y, dtype = float)
    origin = axes.c2p(0,0)
    ex = axes.c2p(1,0)
    ey = axes.c2p(0,1)
    return origin + x[:, None] * ex + y[:,None] * ey


class SceneA_Sine(Scene):
    def construct(self):
        axes = Axes(x_range = [-4, 4, 1],
                    y_range = [-2,2,1],
                    x_length = 10,
                    y_length = 5,
                    tips = True
                    )

        axes.add_coordinates()
        labels = axes.get_axis_labels(MathTex("x"), MathTex("y"))

        x = np.linspace(-4.0, 4.0, 241)
        y = np.sin(x**2)
        z = np.zeros_like(x)
        pts_math = np.column_stack([x,y,z])
        pts_scene = math_to_scene(axes, x, y)

        poly = VMobject(color = YELLOW, stroke_width = 4)
        poly.set_points_as_corners(pts_scene)

        builtin = axes.plot(lambda t: np.sin(t), x_range= [-4,4], color = BLUE)
        builtin.set_stroke(opacity = 0.35, width = 10)

        info = VGroup(
            Text(f"x.shape = {x.shape}", font_size = 22),
            Text(f"pts_scene.shape = {pts_scene.shape}", font_size=22),
            Text("Жёлтый - ручной массив, синий - axes.plot", font_size = 20, color = GRAY_B),


        ).arrange(DOWN, aligned_edge = LEFT).to_corner(UL).shift(DOWN*0.2)

        self.play(Create(axes), FadeIn(labels), run_time = 1.2)
        self.play(FadeIn(info))
        self.play(Create(builtin), run_time=1.0)
        self.play(Create(poly), run_time = 2.0)
        self.wait(2)

        assert pts_math.shape == (241,3)
        assert pts_scene.shape == (241,3)
        print("max |y| =", np.max(np.abs(y)))
        print("first | last math point:", pts_math[0], pts_math[-1])




