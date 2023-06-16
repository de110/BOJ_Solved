import sys
N,M=map(int,sys.stdin.readline().split())
m_list=list(0 for i in range(1,N+1))
for a in range(M):
    i,j,k=map(int,sys.stdin.readline().split())
    m_list[i-1:j]=list(k for l in range(i-1,j))
print(*m_list)