import sys
from collections import deque

case = int(sys.stdin.readline())
for i in range(case):
    count=0
    N,M = map(int,sys.stdin.readline().split())
    que=deque(map(int,sys.stdin.readline().split()))
    while len(que)!=0:
        max_value=max(que)
        temp = que.popleft()
        M-=1
        if max_value == temp:
            count+=1
            if M<0:
                print(count)
                break        
        else:
            que.append(temp)
            if M<0:
                M=len(que)-1
