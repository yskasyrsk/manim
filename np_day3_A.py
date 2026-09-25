from manim import *
import numpy as np

def math_to_scene(axes,x,y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    origin = axes.c2p(0,0)
    ex = axes.c2p(1,0) - origin
    ey = axes.c2p(0,1) - origin

    return origin + x[:,None]*ex + y[:,None]*ey 

def bump(X,Y):
    return np.exp(-(X**2+Y**2))


class SceneA_FieldScalar(Scene):
    def construct(self):

        axes = Axes(
            x_range = [-2.5, 2.5, 1],
            y_range = [-2.5, 2.5, 1],
            x_length = 6.5,
            y_length = 6.5,
            )

        axes.shift(LEFT * 0.8)

        xs = np.linspace(-2.0, 2.0, 17)
        ys = np.linspace(-2.0, 2.0, 17)
        X, Y = np.meshgrid(xs, ys, indexing = "xy")
        Z = bump(X,Y)
        pts = math_to_scene(axes, X.ravel(), Y.ravel())
        z = Z.ravel()
        z_min, z_max = z.min(), z.max()

        t = (z-z_min) / (z_max - z_min + 1e-12)

        dots = VGroup()
        for p, ti in zip(pts,t):
            r = 0.03 + 0.07*ti
            color = interpolate_color(BLUE_E, YELLOW, float(ti))
            dots.add(Dot(p, radius = r, color = color))

        title = Text("g(x,y) = exp(-(x+y)) на всей сетке", font_size = 28)
        title.to_edge(UP)
        info = VGroup(
            Text(f"Z.shape = {Z.shape}", font_size = 28),
            Text(f"Z.min = {z_min:.3f}, Z.max = {z_max:.3f}", font_size = 22),
            Text("формула - одна строка, цикл только собирает Dot", font_size = 20, color= GRAY_B),
        ).arrange(DOWN, aligned_edge = LEFT).to_corner(UR).shift(DOWN * 0.6)

        self.play(Write(title), Create(axes), FadeIn(info))
        self.play(FadeIn(dots), run_time = 1.5)
        self.wait(2)

        assert Z.shape == X.shape
        print("Z[центр] #", Z[Z.shape[0]//2, Z.shape[1] // 2])

        
