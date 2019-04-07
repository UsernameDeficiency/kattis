# Input consists of a single integer N (1≤N≤100).
# Output the entire wizard’s spell by counting from 1 to N, giving one number, space, and “Abracadabra” per line.
import sys
for i in range(int(sys.stdin.readline())):
    print(i + 1, "Abracadabra")