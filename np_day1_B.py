from manim import *
import numpy as np

class SceneB_Sum(Scene):
    def construct(self):
        a = 2.0*RIGHT + 0.5*UP
        b = 0.5*RIGHT + 1.5*UP
        s = a + b

        def vect(start, vec, color, name):
            end = start + vec
            arrow = Arrow(start, end, buff=0, color = color, stroke_width=4)
            tip_dot = Dot(end, color=color, radius = 0.05)
            lab = MathTex(name, color = color, font_size = 36)
            lab.next_to(end, UP if vec[1]>=0 else DOWN, buff = 0.12)
            length = np.linalg.norm(vec)
            meas = Text(f"||{name}={length:.2f}", font_size=20, color = color)
            meas.next_to(lab, RIGHT, buff=0.1)
            return VGroup(arrow, tip_dot, lab, meas), end

        ga, _ = vect(ORIGIN, a, BLUE, "a")
        gb,_ = vect(ORIGIN, b, GREEN, "b")
        gs, _ = vect(ORIGIN, s, YELLOW, r"a+b")

        b_shifted, _ = vect(a,b, GREEN, "b")
        b_shifted.set_opacity(0.45)

        title = Text("a+b = поэлементная сумма ndarray", font_size = 28)
        title.to_edge(UP)

        self.play(Write(title))
        self.play(LaggedStart(FadeIn(ga), FadeIn(gb), lag_ratio = 0.3))
        self.wait(0.4)
        self.play(FadeIn(b_shifted))
        self.play(Create(gs[0]), FadeIn(gs[1:]))

        assert a.shape == (3,)
        assert np.allclose(s, a+b)
        print("a = ", a,"||a||=", np.linalg.norm(a))
        print("s = ", s,"||s||=", np.linalg.norm(s))
            

