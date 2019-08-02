import sys

num_lines = sys.stdin.readline()  # Strip #lines

for line in sys.stdin:
    line = line.split()
    name = line[0]
    study_year = int(line[1][0:4])  # method 1
    birth_year = int(line[2].split("/")[0])  # method 2
    num_courses = int(line[3])
    if study_year >= 2010 or birth_year >= 1991:
        print(name + " eligible")
    elif num_courses >= 41:
        print(name + " ineligible")
    else:
        print(name + " coach petitions")
