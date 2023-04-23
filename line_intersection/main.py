from line_intersection_interface import Line, Point
from line_intersection_visualizer import visualize

def main():
    # Create some test lines
    lines = [
        Line(Point(1, 2), Point(4, 4)),
        Line(Point(2, 6), Point(5, 8)),
        Line(Point(1, 4), Point(4, 1))
    ]

    # Visualize the line intersection process
    visualize(lines)

if __name__ == "__main__":
    main()
