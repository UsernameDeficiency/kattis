# Problem: A common problem in mathematics is to determine which quadrant a given point lies in.
#   There are four quadrants, numbered from 1 to 4, counting ccw and quadrant 1 containing only positive numbers.
#   Your job is to take a point and determine the quadrant it is in.
#   You can assume that neither of the two coordinates will be 0.
# Input: The first line of input contains the integer x (−1000≤x≤1000;x≠0).
#   The second line of input contains the integer y (−1000≤y≤1000;y≠0).
# Output: Output the quadrant number (1, 2, 3 or 4) for the point (x,y).
import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
# Print quadrant number
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
