from ctypes import cdll, Structure, c_double, POINTER, c_int
import os

class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

graham_scan_lib = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "graham_scan.dll"))
graham_scan_lib.graham_scan_wrapper.argtypes = (POINTER(Point), c_int, POINTER(Point), POINTER(c_int))
graham_scan_lib.graham_scan_wrapper.restype = None

def graham_scan(points):
    point_array = (Point * len(points))(*points)
    result_array = (Point * len(points))()
    result_size = c_int(0)

    graham_scan_lib.graham_scan_wrapper(point_array, len(points), result_array, POINTER(c_int)(result_size))

    return [result_array[i] for i in range(result_size.value)]
