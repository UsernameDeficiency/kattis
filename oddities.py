import sys

sys.stdin.readline()  # Strip first line
for i in sys.stdin:
    j = int(i.strip())
    if j % 2 == 0:
        print(j, "is even")
    else:
        print(j, "is odd")
