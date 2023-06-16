import sys
N,M=map(int,sys.stdin.readline().split())
list=list(range(1,N+1))
my_list=list
for k in range(M):
    i,j=map(int,sys.stdin.readline().split())
    if i-1 == 0:
        my_list[i-1:j]=list[j-1::-1]
    else:
        my_list[i-1:j]=list[j-1:i-2:-1]
print(*my_list)