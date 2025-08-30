import math
import numpy as np
import matplotlib.pyplot as plt

def spiral_points(n: int):
    """
    Generate coordinates of the 'archimedean snail' (Spiral of Theodorus).
    Each step is length 1, rotated perpendicular to the radius.
    """
    pts = np.zeros((n, 2))
    pts[0] = [1.0, 0.0]  # start at (1,0)
    for k in range(1, n):
        x, y = pts[k - 1]
        r = math.hypot(x, y)  # distance from origin
        vx, vy = -y / r, x / r  # unit vector perpendicular to (x,y)
        pts[k] = [x + vx, y + vy]
    return pts

def plot_snail(n=200, rays=True, annotate=True):
    pts = spiral_points(n)
    xs, ys = pts[:, 0], pts[:, 1]

    fig, ax = plt.subplots()
    ax.plot(xs, ys, linewidth=1.0, label="Snail curve")

    # Draw rays with sqrt(n) labels
    if rays:
        for i, (x, y) in enumerate(pts, start=1):
            ax.plot([0, x], [0, y], linewidth=0.5, color="gray")

            if annotate:
                xm, ym = x / 1.5, y / 1.5  # midpoint of ray
                ax.text(
                    xm, ym,
                    f"$\\sqrt{{{i}}}$",   # LaTeX-style square root
                    fontsize=8,
                    ha="center", va="center"
                )

    # Draw outer connecting lines with "1" labels
    for i in range(1, len(pts)):
        x1, y1 = pts[i - 1]
        x2, y2 = pts[i]
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2  # midpoint
        ax.text(
            xm, ym,
            "1",
            fontsize=7,
            color="blue",
            ha="center", va="center"
        )

    ax.set_aspect("equal", adjustable="box")
    ax.set_title(f"Archimedean Snail (N={n})")
    ax.legend()
    plt.show()



if __name__ == "__main__":
    plot_snail(17)
