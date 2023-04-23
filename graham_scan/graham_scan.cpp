#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

struct Point {
    double x, y;
};

bool compare(const Point &a, const Point &b) {
    return a.y < b.y || (a.y == b.y && a.x < b.x);
}

double cross_product(const Point &o, const Point &a, const Point &b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

std::vector<Point> graham_scan(std::vector<Point> points) {
    if (points.size() <= 3) return points;

    std::sort(points.begin(), points.end(), compare);

    std::vector<Point> hull(2 * points.size());
    int k = 0;

    for (int i = 0; i < points.size(); ++i) {
        while (k >= 2 && cross_product(hull[k - 2], hull[k - 1], points[i]) <= 0) k--;
        hull[k++] = points[i];
    }

    for (int i = points.size() - 2, t = k + 1; i >= 0; --i) {
        while (k >= t && cross_product(hull[k - 2], hull[k - 1], points[i]) <= 0) k--;
        hull[k++] = points[i];
    }

    hull.resize(k - 1);
    return hull;
}

extern "C" {
    void graham_scan_wrapper(const Point* points, int n, Point* result, int* result_size) {
        std::vector<Point> input_points(points, points + n);
        std::vector<Point> output_points = graham_scan(input_points);
        std::copy(output_points.begin(), output_points.end(), result);
        *result_size = output_points.size();
    }
}
