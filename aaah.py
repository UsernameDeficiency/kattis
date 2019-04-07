# The input consists of two lines. The first line is the “aaah” Jon Marius is able to say that day. The second line is
# the “aah” the doctor wants to hear. Only lowercase ’a’ and ’h’ will be used in the input, and each line will contain
# between 0 and 999 ’a’s, inclusive, followed by a single ’h’.
# Output “go” if Jon Marius can go to that doctor, and output “no” otherwise.
import sys
ah0 = sys.stdin.readline()
ah1 = sys.stdin.readline()
print("go") if len(ah0) >= len(ah1) else print("no")
