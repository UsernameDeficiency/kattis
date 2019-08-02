import sys
pillars = int(sys.stdin.readline())
if pillars <= 3:
    print("1")
else:
    print(pillars - 2)
