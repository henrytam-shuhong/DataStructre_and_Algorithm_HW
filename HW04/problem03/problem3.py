# You are given n different points in a 2-dimensional space. Design an algorithm that determines the unique number of right
# triangles that can be formed by choosing sets of three points. Your solution must run in under 30 seconds to receive full credit,
# partial credit will be given for all correct answers.
# You will be given an input file where the first line contains the number of points followed by a number of lines each with one
# point e.g.
# 5
# 0 0
# 0 4
# 0 7
# 3 0
# 9 0
# Your solution should the answer to the console:
# Python3 rightTriangles.py < right_triangles_input.txt
# The number of right triangles is: <your answer>

'''
- read the input file and creat a matrix for coordinates
- traverse every point and build up coordinates based on it
- calculate the new  coordinates of other points and the angles of each points in the polar coordinates
- sort the points in regard to the angles in the new array
- traverse the new array and search for the complementary points which form a right angle together with the origin as the right angel vertex.
- conclude the total number of right triangles
'''

# 5
# 0 0
# 0 4
# 0 7
# 3 0
# 9 0


# read the file via standard input
import sys, math, time
from bisect import bisect_left, bisect_right

start_time = time.time()

input = sys.stdin.read().strip().split('\n')
input.pop(0)
Matrix = [list(map(int, x.split(' '))) for x in input]
# print(Matrix)

# count the angles
right_angle_count = 0

# ensure the angle is always in the range of [-pi, pi]
def normalize_to_range_pi(angle):
    if angle > 0 and angle > math.pi:
        angle -= 2 * math.pi
    if angle < 0 and angle < -math.pi:
        angle += 2 * math.pi
    return angle

# traverse every point
for i in range(len(Matrix)):
    # calculate the new  coordinates of other points
    dx = 0-Matrix[i][0]
    dy = 0-Matrix[i][1]
    new_matrix = []
    for j in range(len(Matrix)):
        new_matrix.append([dx+Matrix[j][0], dy+Matrix[j][1]])
    # calculate the angle of the new points in the polar coordinate
    angle_arr = []
    for k in range(len(new_matrix)):
        # angel in radians
        angle = math.atan2(new_matrix[k][1],new_matrix[k][0])
        angle_arr.append(angle)


    # exclude the origin
    angle_arr.pop(i)
    # sort the angel_arr
    angle_arr.sort()

    # For each angle, search for its complementary angle (± pi/2)
    for angle in angle_arr:
        # + pi/2
        target_angle_1 = normalize_to_range_pi(angle + math.pi / 2)
        # - pi/2
        target_angle_2 = normalize_to_range_pi(angle - math.pi / 2)
        # find complementary angles in the sorted angle_arr
        # using binary search with tolerance for floating point precision
        tolerance = 1e-9
        idx1 = bisect_left(angle_arr, target_angle_1 - tolerance)
        idx2 = bisect_right(angle_arr, target_angle_1 + tolerance)
        idx3 = bisect_left(angle_arr, target_angle_2 - tolerance)
        idx4 = bisect_right(angle_arr, target_angle_2 + tolerance)


        if idx1 < idx2:
            right_angle_count += idx2 - idx1
        if idx3 < idx4:
            right_angle_count += idx4 - idx3


# print start time
print(f"Compute Triangle Code Starting:{start_time}")

# the final answer:
print(f"The number of right triangles is: {right_angle_count // 2}")

# End time
end_time = time.time()

# Calculate elapsed time in seconds
elapsed_time = end_time - start_time
print(f"Compute Triangle Code took:  {elapsed_time:.5f} seconds")