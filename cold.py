# The input is composed of two lines. The first line contains a single positive integer n (1≤n≤100) that specifies the
# number of temperatures collected by the University of Chicago Weather Service. The second line contains n
# temperatures, each separated by a single space. Each temperature is represented by an integer t (−1000000≤t≤1000000)
# You must print a single integer: the number of temperatures strictly less than zero.
import sys
cold_days = 0
sys.stdin.readline()  # Strip first line
temps = sys.stdin.readline().split()
for i in temps:
    if int(i) < 0:
        cold_days += 1
print(cold_days)

