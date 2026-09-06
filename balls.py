from manim import *
from math import sin

class Balls(Scene):
    def construct(self):
        circ = Circle(radius = 0.5, color = BLUE, fill_color = BLUE, fill_opacity = 1)
        START_Y = 1
        START_X = -5
        point = [START_X, START_Y, 0]

        circ.move_to(point)
        self.add(circ)

        t = ValueTracker(0)

        def move_ball(ball: Circle):
            dt = t.get_value()
            dy = abs(sin(t.get_value()))
            point = [dt,dy,0]
            ball.move_to(point)

        def squisch_ball(ball: Circle):
            dy = abs(sin(t.get_value()))
            stretch_value = 0
            if dy == START_Y: 
                stretch_value = 0.5 
            else: stretch_value = 0
            ball.stretch(0, stretch_value)
        
            

        circ.add_updater(move_ball)
        circ.add_updater(squisch_ball)
            
        self.play(t.animate.set_value(24), run_time=6)

        

        