# Problem: The QALY (Quality-Adjusted Life-Year) for each period in which the quality of life is constant is simply the
#   product of the quality of life and the length of the period (in years). We wish to know the amount of QALY
#   accumulated by a person at the time of death, given the complete history of this person.
# Input: The first line of input contains a single integer N (1≤N≤100), which is the number of periods of constant
#   quality of life during the person’s lifetime. The next N lines describe the periods of life. Each of these lines
#   contains two real numbers q (0<q≤1), which is the quality of life in this period, and y (0<y≤100), which is the
#   number of years in this period. All real numbers will be specified to exactly one decimal place.
# Output: Return the QALY accumulated by the person. Your answer is correct if its absolute error does not exceed 10^(−3).
import sys

input = sys.stdin.read()
# Strip first line and then for every line
# Multiply the 2 whitespace separated numbers and
# Return the sum of the products
input.readline()

tot_qaly = 0.0

for line in input:
    nums = line.split()
    qaly = float(nums[0])
    years = float(nums[1])
    tot_qaly += qaly*years
print(tot_qaly)
