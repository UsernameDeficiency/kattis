import sys

limit = int(sys.stdin.readline())  # Bandwith limit/month
sys.stdin.readline()  # Throw away first month (since kattis calculation is incorrect)

remain = 0
total = 0
for used in sys.stdin:
    remain = limit - int(used)
    total += remain
print(total + limit)
