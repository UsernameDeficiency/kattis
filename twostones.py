# Input: The input contains an integer N (1≤N≤10000000), the number of stones.
# Output: Output the winner, “Alice” (odd) or “Bob” (even), on a line.
import sys
print("Bob") if int(sys.stdin.readline()) % 2 == 0 else print("Alice")
