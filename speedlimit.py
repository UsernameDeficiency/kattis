import sys

num_lines = sys.stdin.readline()
while num_lines.strip() != "-1":
    last_time = 0
    distance = 0
    for i in range(int(num_lines)):
        curr_line = sys.stdin.readline().split()  # read stopwatch
        speed = int(curr_line[0])
        time = int(curr_line[1]) - last_time
        last_time = int(curr_line[1])
        distance += speed*time
    print(str(distance) + " miles")
    num_lines = sys.stdin.readline()
