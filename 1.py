# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(inner, outer, points_x, points_y):
    # write your code in Python 3.6
    amount_of_dots = len(points_x)
    counter = 0
    for i in range(amount_of_dots):
        x = points_x[i]
        y = points_y[i]
        # Distance from 0,0 to point
        d = math.sqrt((x*x + y*y))
        if (d < outer and d > inner):
            counter += 1
    return counter

    # Tests

# result = solution(inner=1, outer=3, points_x= [0,1,2,-2,3], points_y= [0,1,4,1,0])
# print (result == 2)

# result_2 = solution(inner=2, outer=4, points_x= [4,0,1,-2], points_y= [-4,4,3,0])
# print (result_2 == 1)