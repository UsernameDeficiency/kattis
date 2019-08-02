# If the input string contains two consecutive occurrences of the letter s,
# output "hiss". Otherwise, output "no hiss".
import sys

in_word = sys.stdin.readline()
if in_word.find("ss") != -1:
    print("hiss")
else:
    print("no hiss")

# "manual" solution for fun
# s_last = False
# for char in in_word:
#     if char == "s":
#         if s_last:
#             print("hiss")
#             sys.exit()
#         s_last = True
#     else:
#         s_last = False
# print("no hiss")
