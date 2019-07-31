# https://open.kattis.com/problems/fizzbuzz
# Input: Three integers on a single line, X, Y and N (1≤X<Y≤N≤100).
# Output: Print integers from 1 to N in order, each on its own line, replacing the ones divisible by X with Fizz,
# the ones divisible by Y with Buzz and ones divisible by both X and Y with FizzBuzz.
import sys
XYN = sys.stdin.readline().split()
X = int(XYN[0])
Y = int(XYN[1])
N = int(XYN[2])

for i in range(1, N + 1):
    if i % X == 0:
        if i % Y == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % Y == 0:
        print("Buzz")
    else:
        print(i)
