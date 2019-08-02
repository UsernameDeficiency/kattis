import sys

in_line = sys.stdin.readline().split()
num_articles = int(in_line[0])
impact = int(in_line[1])

print(num_articles*(impact - 1) + 1)
