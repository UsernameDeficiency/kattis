# Problem: The number S is called the mean of two numbers R1 and R2 if S is equal to (R1+R2)/2.
#   Mirko’s birthday present for Slavko was two integers R1 and R2. Slavko promptly calculated their mean which also
#   happened to be an integer but then lost R2! Help Slavko restore R2.
# Input: The only line of input contains two whitespace separated integers R1 and S, both between −1000 and 1000.
# Output: Output R2 on a single line.
# Status: Solved!
import sys

inputLine = sys.stdin.readline()
numList = inputLine.split()
R1 = int(numList[0])
S = int(numList[1])

# S = (R1+R2)/2 => R2 = 2S - R1
print(2*S - R1)
