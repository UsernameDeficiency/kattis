# A set of pieces should contain: 1 king, 1 queen, 2 rooks, 2 bishops, 2 knights and 8 pawns.
# The input consists of 6 integers on a single line, each between 0 and 10 (inclusive).
# The numbers are, in order, the numbers of kings, queens, rooks, bishops, knights and pawns.
# Output should consist of 6 integers on a single line; the number of pieces of each type Mirko should add or remove.
# If a number is positive, Mirko needs to add that many pieces. If a number is negative, Mirko needs to remove pieces.
import sys
correctPieces = [1, 1, 2, 2, 2, 8]
foundPieces = [int(i) for i in sys.stdin.readline().split()]
for i in [x - y for x, y in zip(correctPieces, foundPieces)]: print(i, end=' ')
