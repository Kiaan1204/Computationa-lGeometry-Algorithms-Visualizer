import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from graham_scan_interface import Point, graham_scan

def init_plot(points, hull_points):
    fig, ax = plt.subplots()
    ax.set_title('Convex Hull Visualization')

    x, y = zip(*[(p.x, p.y) for p in points])
    scat = ax.scatter(x, y, color='blue', zorder=10)

    hull_line = list(hull_points) + [hull_points[0]]
    hx, hy = zip(*[(p.x, p.y) for p in hull_line])
    poly, = ax.plot(hx, hy, 'r-', zorder=5)

    return fig, ax, scat, poly

def update(frame, points, hull_points, scat, poly):
    hull_line = hull_points[:frame] + [hull_points[0]]
    hx, hy = zip(*[(p.x, p.y) for p in hull_line])

    poly.set_data(hx, hy)
    return scat, poly

def visualize(points, hull_points):
    fig, ax, scat, poly = init_plot(points, hull_points)
    ani = FuncAnimation(fig, update, frames=len(hull_points) + 1, fargs=(points, hull_points, scat, poly), interval=500, blit=True)
    plt.show()
