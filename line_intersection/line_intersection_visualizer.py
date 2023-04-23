import matplotlib.pyplot as plt
import matplotlib.animation as animation
from line_intersection_interface import Line, Point,line_intersection

def intersection_point(line1, line2):
    x1, x2, x3, x4 = line1.p1.x, line1.p2.x, line2.p1.x, line2.p2.x
    y1, y2, y3, y4 = line1.p1.y, line1.p2.y, line2.p1.y, line2.p2.y

    den = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / den

    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)

    return Point(x, y)



def visualize(lines, interval=1000):
    fig, ax = plt.subplots()

    # Set up the axis limits
    ax.set_xlim(min(min(line.p1.x, line.p2.x) for line in lines) - 1,
                max(max(line.p1.x, line.p2.x) for line in lines) + 1)
    ax.set_ylim(min(min(line.p1.y, line.p2.y) for line in lines) - 1,
                max(max(line.p1.y, line.p2.y) for line in lines) + 1)

    # Create line objects
    line_objects = [ax.plot([], [], lw=2)[0] for _ in range(len(lines))]
    intersection_points = []



    def animate(i):
        for j, line_obj in enumerate(line_objects):
            line = lines[j]
            line_obj.set_data([line.p1.x, line.p2.x], [line.p1.y, line.p2.y])

        if i < len(lines):
            for j in range(i):
                if line_intersection(lines[i], lines[j]):
                    intersection = intersection_point(lines[i], lines[j])
                    intersection_points.append(ax.plot(intersection.x, intersection.y, 'ro', markersize=5))

        return line_objects + [point[0] for point in intersection_points]

    

    ani = animation.FuncAnimation(fig, animate, frames=len(lines) + 1, interval=interval,
                                  blit=True, repeat=False)

    plt.show()
