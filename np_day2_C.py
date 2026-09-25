from manim import *
import numpy as np

def math_to_scene(axes, x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype = float)
    origin = axes.c2p(0,0)
    ex = axes.c2p(1,0) - origin
    ey = axes.c2p(0,1) - origin
    return origin + x[:,None]*ex + y[:,None]*ey

def polar_curve(n_points, endpoint):
    theta = np.linspace(0.0, 2*np.pi, n_points, endpoint = endpoint)
    ## r = 1.0 + 0.4 * np.cos(4*theta)  
    # полярная роза
    # r = theta / (2*np.pi)  
    # спираль Архимеда
    r = 1.0 -np.cos(theta) 
    ## кардиоида
    # r = np.full_like(theta, 1.5) ## окружность
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y, theta

class SceneC_Polar(Scene):
    def construct(self):

        axes = Axes(
            x_range = [-2,2,1],
            y_range = [-2,2,1],
            x_length = 6,
            y_length = 6,
        )

        axes.shift(LEFT * 0.5)
        x_ok, y_ok, _ = polar_curve(401, endpoint = True)
        pts_ok = math_to_scene(axes, x_ok, y_ok)
        rose = VMobject(color = YELLOW, stroke_width = 4)
        rose.set_points_as_corners(pts_ok)

        x_bad, y_bad, _ = polar_curve(20, endpoint=False)
        pts_bad = math_to_scene(axes, x_bad, y_bad)
        broken = VMobject(color = RED, stroke_width = 3)
        broken.set_points_as_corners(pts_bad)
        broken.shift(RIGHT*0.0)

        title = Text("полярные x,y - сразу массивом", font_size = 28)
        title.to_edge(UP)
        note = Text(
            "жёлтый : linspace(..., endpoint = True), 401 точка\n"
            "красный: 20 точек и правый край вырезан - разрыв",
            font_size = 20,
            color = GRAY_B,
        ).to_edge(DOWN)

        self.play(Write(title), Create(axes))
        self.play(Create(rose), run_time = 2.0)
        self.play(Create(broken), FadeIn(note), run_time = 1.2)
        self.wait(2)

        gap =np.linalg.norm(
            np.array([x_bad[0], y_bad[0]]) - np.array(x_bad[-1], y_bad[-1])
        )

        print("разрыв красной линии в математике = ", gap)
        print("rose math shape =", np.column_stack([x_ok, y_ok, np.zeros_like(x_ok)]).shape)
        
        

        