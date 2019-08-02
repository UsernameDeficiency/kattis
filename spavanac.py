import sys

time = sys.stdin.readline().split()
hour = int(time[0])
minute = int(time[1])

if minute >= 45:
    print(str(hour) + " " + str(minute - 45))
elif hour != 0:
    print(str(hour - 1) + " " + str(60 + minute - 45))
else:
    print("23 " + str(60 + minute - 45))

