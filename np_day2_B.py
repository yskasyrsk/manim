from manim import *
import numpy as np

def math_to_scene(axes, x, y):
    x = np.asarray(x, dtype = float)
    y = np.asarray(y, dtype= float)
    origin = axes.c2p(0,0)
    ex = axes.c2p(1,0) - origin
    ey = axes.c2p(0,1) - origin
    return origin + x[:,None]*ex + y[:, None]*ey

class SceneB_Mesh(Scene):
    def construct(self):

        axes = Axes(
            x_range = [-3, 3, 1],
            y_range = [-2,2,1],
            x_length = 10,
            y_length = 6,

        )
        
        xs = np.linspace(-2.5, 2.5, 9)
        ys = np.linspace(-1.5, 1.5, 7)
        X, Y = np.meshgrid(xs,ys,indexing = "xy")

        nodes_scene = math_to_scene(axes, X.ravel(), Y.ravel())
        dots = VGroup(*[Dot(p, radius = 0.05, color = YELLOW) for p in nodes_scene])

        row_lines = VGroup()
        for i in range(X.shape[0]):
            row_pts = math_to_scene(axes, X[i], Y[i])
            line = VMobject(color = BLUE, stroke_width = 2)
            line.set_points_as_corners(row_pts)
            row_lines.add(line)

        col_lines = VGroup()
        for j in range(X.shape[1]):
            col_pts = math_to_scene(axes, X[:,j], Y[:,j])
            line = VMobject(color = TEAL, stroke_width = 2)
            line.set_points_as_corners(col_pts)
            col_lines.add(line)

        info = VGroup(
            Text(f"xs.shape = {xs.shape}, ys.shape = {ys.shape}", font_size = 22),
            Text(f"X.shape = {X.shape} (ny, nx)", font_size = 22),
            Text(f"nodes = {nodes_scene.shape[0]}", font_size = 22), 
        ).arrange(DOWN, aligned_edge= LEFT).to_corner(UL)

        self.play(Create(axes), FadeIn(info))
        self.play(Create(row_lines), Create(col_lines), run_time = 1.5)
        self.play(LaggedStart(*[FadeIn(d, scale = 0.3) for d in dots], 
                              lag_ratio = 0.02))
        self.wait(2)

        assert X.shape == (len(ys), len(xs))
        print("X[0] =", X[0])
        print("Y[0] = ", Y[0])

