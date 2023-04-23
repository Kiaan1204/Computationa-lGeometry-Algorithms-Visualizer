#include <iostream>
#include <cmath>

struct Point {
    double x, y;
};

struct Line {
    Point p1, p2;
};

bool do_lines_intersect(const Line& line1, const Line& line2) {
    double x1 = line1.p1.x, x2 = line1.p2.x, x3 = line2.p1.x, x4 = line2.p2.x;
    double y1 = line1.p1.y, y2 = line1.p2.y, y3 = line2.p1.y, y4 = line2.p2.y;

    double den = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1);

    if (std::abs(den) < 1e-10) {
        return false; // Parallel or coincident lines
    }

    double ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / den;
    double ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / den;

    return (ua >= 0 && ua <= 1 && ub >= 0 && ub <= 1);
}

extern "C" {
    bool line_intersection_wrapper(const Line* line1, const Line* line2) {
        return do_lines_intersect(*line1, *line2);
    }
}