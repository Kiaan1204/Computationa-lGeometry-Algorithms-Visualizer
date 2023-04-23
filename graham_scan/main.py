import random
from graham_scan_interface import Point, graham_scan
from visualizer import visualize

def main():
    num_points = 25
    min_coord = 0
    max_coord = 10

    points = [
        Point(random.uniform(min_coord, max_coord), random.uniform(min_coord, max_coord))
        for _ in range(num_points)
    ]
    
    hull_points = graham_scan(points)
    visualize(points, hull_points)

if __name__ == "__main__":
    main()
