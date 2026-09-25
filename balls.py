from manim import *
from math import sin

class Balls(Scene):
    def construct(self):
        circ = Circle(radius = 0.5, color = BLUE, fill_color = BLUE, fill_opacity = 1)
        START_Y = 2
        START_X = -3
        point = [START_X, START_Y, 0]

       

        floor = Line()
        circ.move_to(point)
        self.add(circ)

        t = ValueTracker(0)

        def move_ball(ball: Circle):
            dt = t.get_value()+START_X
            dy = abs(sin(t.get_value()))
            point = [dt,dy,0]
            ball.move_to(point)

        def squisch_ball(ball: Circle):
            dy = abs(sin(t.get_value()))
            stretch_value = 0
            if dy >= START_Y-0.1: 
                stretch_value = 0.5 
            else: stretch_value = 1
            ball.stretch_to_fit_height(stretch_value)

        def add_label(ball:Circle):
            x = t.get_value()+START_X
            y = abs(sin(t.get_value()))
            label = Text(f"x={x}, y={y}").move_to([x,y,0]).shift(UP*1)
            self.add(label)

            

        circ.add_updater(move_ball)
        circ.add_updater(squisch_ball)
        circ.add_updater(add_label)

            
        self.play(t.animate.set_value(24), run_time=6)

        

        