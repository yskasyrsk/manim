from manim import *
import numpy as np

class Balls(Scene):
    def construct(self):
        ground_y = -2.5
        start_y = 2.5
        start_x = -1
        r = 0.4    

        t = ValueTracker(0)

        ground = Line(LEFT*6, RIGHT*6).shift(DOWN*2.5)

        def make_ball():
            y = ground_y + r + abs(np.sin(t.get_value()))*(start_y-ground_y-r)
            height_from_floor = y -ground_y
            squash = np.clip(height_from_floor/(2*r), 0.45, 1.0)

            h = 2*r*squash
            w = 2*r/squash



            ball = Circle(radius = r, color = ORANGE,  fill_opacity = 1)
            ball.stretch_to_fit_height(h)
            ball.stretch_to_fit_width(w)
            ball.move_to([0,ground_y+h/2,0])

            if squash >= 0.999:
                ball.move_to([0,y,0])
            return ball

        ball = always_redraw(make_ball)
        self.add(ground,ball)
        self.play(t.animate.set_value(3*PI), run_time=4, rate_func = linear)
        