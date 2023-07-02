import sys

A,B = (sys.stdin.readline()[::-1].split())[::-1]
if A>B:
    print(A)
else:
    print(B)