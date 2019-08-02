import sys

num_lines = int(sys.stdin.readline())
for i in range(num_lines):
    curr_line = [int(x) for x in sys.stdin.readline().split()]
    for j in range(2, len(curr_line)):
        if curr_line[j] != curr_line[j - 1] + 1:
            print(j)
            break
