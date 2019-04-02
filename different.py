# Problem: Write a program that computes the difference between non-negative integers.
# Input: Each line of the input consists of a pair of integers, separated by spaces.
#   Each integer is between 0 and 10^15 (inclusive). The input is terminated by end of file.
# Output: For each pair of integers in the input, output one line, containing the absolute value of their difference.
# Status: Solved!
import sys

for i in sys.stdin:
    line = i.split()
    num1 = int(line[0])
    num2 = int(line[1])
    print(abs(num1-num2))
