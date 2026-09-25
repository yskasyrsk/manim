from manim import *
import numpy as np

class SceneA_OnePoint(Scene):
    def construct(self):
        p = np.array([2.0, 1.0, 0.0], dtype = float)

        axes = Axes(
            x_range = [-1,4,1],
            y_range = [-1,3,1],
            x_length = 7,
            y_length = 5,
            tips = False,
        )

        x = np.linspace(-1, 4, 50)
        y = 0.5 * x**2

        cloud = np.column_stack((x,y)) 
       
        axes.to_edge(DOWN, buff=0.4)
        
        p_scene = axes.c2p(*p[:2])

        parab = VGroup()

        for i in range(0,49):
            
            streck = Line(axes.c2p(*cloud[i]), axes.c2p(*cloud[i+1]))
            parab.add(streck) 


        dot = Dot(point = p_scene, color = YELLOW, radius = 0.08)
        label = MathTex(
            rf"p = ({p[0]:.0f},\;{p[1]:.0f},\;{p[2]:.0f})", font_size = 32,). next_to(dot, UR, buff=0.15)
        shape = Text(f"shape = {p.shape}", font_size= 24, color = GRAY_B)
        shape.to_corner(UL)

        

        self.play(Create(axes), run_time = 1.2)
        self.play(FadeIn(dot, scale = 0.3), Write(label), FadeIn(shape))
        self.play(FadeIn(parab))
        self.wait(1.5)

        print("p.shape = ",p.shape)
        print("p.scene = ", p_scene)


        