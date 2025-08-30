import math
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

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

def plot_snail(n=17, rays=True, annotate=True):
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
    if annotate:
        for i in range(1, len(pts)):
            x1, y1 = pts[i - 1]
            x2, y2 = pts[i]
            xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(xm, ym, "1", fontsize=7, color="blue", ha="center", va="center")

    # Draw outer connecting lines with "1" labels


    ax.set_aspect("equal", adjustable="box")
    ax.set_title(f"Archimedean Snail (N={n})")
    ax.legend()
    plt.show()
    return fig, ax



def main():
    parser = argparse.ArgumentParser(
        description="Plot the Archimedean Snail (Spiral of Theodorus)."
    )
    parser.add_argument(
        "--n", type=int, default=17,
        help="Number of points (default: 17)"
    )
    parser.add_argument(
        "--no-rays", action="store_true",
        help="Hide the radial lines"
    )
    parser.add_argument(
        "--no-annotations", action="store_true",
        help="Hide all labels (√n on rays and 1 on lines)"
    )
    parser.add_argument(
        "--outfile", type=str, default=None,
        help="File name to save the plot (will be saved in 'results/' folder)"
    )
    parser.add_argument(
        "--no-show", action="store_true",
        help="Do not display the interactive window"
    )

    args = parser.parse_args()

    fig, ax = plot_snail(
        n=args.n,
        rays=not args.no_rays,
        annotate=not args.no_annotations
    )

    if args.outfile:
        output_folder = "results"
        os.makedirs(output_folder, exist_ok=True)
        full_path = os.path.join(output_folder, args.outfile)
        fig.savefig(full_path, dpi=200, bbox_inches="tight")
        print(f"Saved plot to {full_path}")

    if not args.no_show:
        import matplotlib.pyplot as plt
        plt.show()


if __name__ == "__main__":
    main()
