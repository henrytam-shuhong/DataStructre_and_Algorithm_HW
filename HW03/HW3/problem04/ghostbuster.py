import sys
from typing import List, Tuple
# a function can determine whether two segments intersect use knowledge of cross product
# To determine whether two line segments intersect,
# you can determine whether the two endpoints of the two line segments are on their respective sides.
# Correspondingly,  use the positive and negative values
# of the two-dimensional vector cross product results to represent the
# characteristics of the vector rotation direction.


Point = Tuple[int, int]

def cross_product(p1: Point, p2: Point, p3: Point) -> int:
    x1 = p2[0] - p1[0]
    y1 = p2[1] - p1[1]
    x2 = p3[0] - p1[0]
    y2 = p3[1] - p1[1]
    return x1 * y2 - x2 * y1

def on_segment(p: Point, seg: Tuple[Point, Point]) -> bool:
    a, b = seg
    x, y = p
    return (
        x >= min(a[0], b[0]) and
        x <= max(a[0], b[0]) and
        y >= min(a[1], b[1]) and
        y <= max(a[1], b[1])
    )

def is_segment_intersect(seg1: Tuple[Point, Point], seg2: Tuple[Point, Point]) -> bool:
    a, b = seg1
    c, d = seg2

    d1 = cross_product(a, b, c)
    d2 = cross_product(a, b, d)
    d3 = cross_product(c, d, a)
    d4 = cross_product(c, d, b)

    # General case
    if d1 * d2 < 0 and d3 * d4 < 0:
        return True

    # Special cases (collinear points on segment)
    if d1 == 0 and on_segment(c, seg1):
        return True
    if d2 == 0 and on_segment(d, seg1):
        return True
    if d3 == 0 and on_segment(a, seg2):
        return True
    if d4 == 0 and on_segment(b, seg2):
        return True

    return False

# Testing
seg1 = [(0, 0), (1, 1)]
seg2 = [(0, 1), (1, 0)]
seg3 = [(0, 0), (2, 2)]
seg4 = [(1, 1), (1, 0)]
# Normal intersection case
# print(is_segment_intersect(seg1, seg2))  # Output: True
# One endpoint of segment 1 lies on segment 2
# print(is_segment_intersect(seg3, seg4))  # Output: True


# turn the input files into a segments array:
def parse_input_to_segments() -> List[List[Tuple[int, int]]]:
    # Read all input from standard input (e.g., from a file using redirection)
    input_data = sys.stdin.read().strip()
    lines = input_data.split('\n')

    n = int(lines[0])  # Number of Ghostbuster-ghost pairs

    segments = []
    for i in range(1, n + 1):
        parts = lines[i].split()
        # Extract Ghostbuster coordinates (B x1 y1)
        b_x, b_y = int(parts[1]), int(parts[2])
        # Extract Ghost coordinates (G x2 y2)
        g_x, g_y = int(parts[4]), int(parts[5])
        # Form the segment [(b_x, b_y), (g_x, g_y)]
        segment = [(b_x, b_y), (g_x, g_y)]
        segments.append(segment)

    return segments


# using recurrence to examine all pairs of segments
def examineArrays(arr, start, end):
    # Base case: if we've checked all possible pairs
    if start == len(arr) - 1:
        print("All Ghosts: were eliminated")
        return
    # If 'end' has reached the end of the array, move 'start' to next element and reset 'end'
    if end == len(arr):
        examineArrays(arr, start+1, start+2)
        return
    # Check if current pair of segments intersect
    if is_segment_intersect(arr[start],arr[end]):
        print("All Ghosts: were not eliminated")
        return
    else:
    # Recursively check the next pair
        examineArrays(arr, start, end+1)

# inplement inputfile
segments = parse_input_to_segments()
print(segments)
examineArrays(segments, 0, 1, )

