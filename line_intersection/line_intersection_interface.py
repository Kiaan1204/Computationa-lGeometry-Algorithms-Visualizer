from ctypes import cdll, Structure, c_double, POINTER
import os

class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

class Line(Structure):
    _fields_ = [("p1", Point), ("p2", Point)]

line_intersection_lib = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "line_intersection.dll"))
line_intersection_lib.line_intersection_wrapper.argtypes = (POINTER(Line), POINTER(Line))
line_intersection_lib.line_intersection_wrapper.restype = bool

def line_intersection(line1, line2):
    return line_intersection_lib.line_intersection_wrapper(POINTER(Line)(line1), POINTER(Line)(line2))

