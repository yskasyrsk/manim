from manim import *
import numpy as np

class SceneC_Cloud(Scene):
    def construct(self):
        cloud = np.array(
            [
                [1.5, 1.0, 0.0],
                [-1.5, 1.0, 0.0],
                [-1.5, -1.0, 0.0],
                [1.5, -1.0, 0.0],
            ], dtype = float,
        )

        path_pts = np.vstack([cloud, cloud[0]])
        center = cloud.mean(axis = 0)
        deltas = cloud - center
        lengths = np.linalg.norm(deltas, axis = 1)
        hats = deltas / lengths[:, None]

        dots = VGroup(*[Dot(p, color = YELLOW) for p in cloud])
        poly = VMobject(color = BLUE, stroke_width = 3)
        poly.set_points_as_corners(path_pts)

        mid = Dot(center, color = RED)
        unit_arrows = VGroup(
            *[Arrow(center, center + hat, buff = 0, color = ORANGE, stroke_width=3)
              for hat in hats]
        )

        info = VGroup(
            Text(f"cloud.shape = {cloud.shape}", font_size = 24),
            Text(f"deltas.shape= {deltas.shape}", font_size = 24),
            Text(f"hats[0] norm = {np.linalg.norm(hats[0]):.3f}", font_size = 24),
        ).arrange(DOWN, aligned_edge = LEFT).to_corner(UL)

        self.play(Write(info))
        self.play(Create(poly), LaggedStart(*[FadeIn(d) for d in dots], lag_ratio = 0.15))
        self.play(FadeIn(mid))
        self.play(LaggedStart(*[Create(a) for a in unit_arrows], lag_ratio = 0.1))
        self.wait(2)

        print("length =", lengths)
        print("hats =\n", hats)
        print("row norms =", np.linalg.norm(hats, axis =1))
        
