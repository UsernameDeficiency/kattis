# Input: Five lines, each containing 4 integers, the grades a contestant got.
# The contestants are numbered 1 to 5 in the order in which their grades were given.
# Output: Output on a single line the winner’s number and their points, 
# separated by a space.
import sys
tot_grade = [0 for i in range(5)]  # Sum of each contestant's grades
winner = 0   # Winner's index
highest = 0  # Winner's total grade

for i in range(0, 5):
        line = sys.stdin.readline()
        for grade in line.split():  # Grades split by whitespace
                tot_grade[i] += int(grade)
        if tot_grade[i] > highest:
                winner = i
                highest = tot_grade[i]

print(winner + 1, highest)
