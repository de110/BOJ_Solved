import sys
N,M=map(int,sys.stdin.readline().split())
list=list(range(1,N+1))
for k in range(M):
    i,j=map(int,sys.stdin.readline().split())
    temp=list[i-1]
    list[i-1]=list[j-1]
    list[j-1]=temp
print(*list)