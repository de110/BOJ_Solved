import sys
B=[]
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
for i in range(N):
    B.append(A[i]/max(A)*100)
print(sum(B)/N)