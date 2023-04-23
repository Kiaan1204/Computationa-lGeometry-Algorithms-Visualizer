import random
from voronoi_interface import generate_voronoi
from visualizer import animate_voronoi

def main():
    num_points = 25
    min_coord = 0
    max_coord = 10

    points = [
        (random.uniform(min_coord, max_coord), random.uniform(min_coord, max_coord))
        for _ in range(num_points)
    ]
    
    voronoi = generate_voronoi(points)
    animate_voronoi(voronoi)

if __name__ == "__main__":
    main()
