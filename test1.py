from manim import *
import numpy as np

def math_to_scene(axes, x,y):
    x = np.asarray(x,dtype = float)
    y = np.asarray(y, dtype= float)
    origin = axes.cp2(0,0)
    ex = axes.c2p(1,0) - origin
    ey = axes.c2p(0,1) - origin
    return origin + x[:,None]*ex + y[:, None]*ey

class SceneB_Mask(Scene):
    def costruct(self):
        axes = Axes(
            x_range = [-4, 4, 1],
            y_range = [-2, 2, 1],
            x_length = 11,
            y_length = 5,
            tips = False,
        ).axes.add_coordinates()

        x = np.linspace(-4.0, 4.0, 81)
        y = np.sin(x)
        z = np.zeros_like(x)
        pts_math = np.column_stack([x,y,z])

        upper = y > 0
        band = np.abs(x) < 2.0
        both = upper & band

        scene_all = math_to_scene(axes, x,y)
        dot_low = VGroup(*[Dot(p, radius = 0.05, color = GREY_B) for p in scene_all[~upper]])
        dots_up = VGroup(*[Dot(p, radius = 0.06, color = YELLOW) for p in scene_all[~upper]])
        rings = VGroup(*[
            Circle(radius = 0.12, color = RED, stroke_width = 3).move_to(p)
            for p in scene_all[both]
            ])

        sine = VMobject(color = BLUE, stroke_width =2)
        sine.set_points_as_corners(scene_all)


