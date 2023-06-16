import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
print(sum(A)*100/max(A)/N)