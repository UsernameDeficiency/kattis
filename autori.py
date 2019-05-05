# The first and only line of input will contain at most 100 characters, uppercase and lowercase letters of the English
# alphabet and hyphen (‘-’ ASCII 45). The first character will always be an uppercase letter. Hyphens will always be
# followed by an uppercase letter. All other characters will be lowercase letters.
# The first and only line of output should contain the appropriate short variation (initialism).
import sys
initial = ""  # Empty string for storing the initialism
line = sys.stdin.readline().split('-')
for j in line:
    initial += j[0]

print(initial)
