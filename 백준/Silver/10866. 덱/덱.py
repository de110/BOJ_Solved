import sys
from collections import deque

class dq:
    def __init__(self):
        self.items = deque()

    def push_front(self,items):
        self.items.appendleft(items)
    def push_back(self,items):
        self.items.append(items)
    def pop_front(self):
        if len(self.items)!=0:
            return self.items.popleft()
        else:
            return -1

    def pop_back(self):
        if len(self.items)!=0:
            return self.items.pop()
        else:
             return -1

    def size(self):
        return len(self.items)

    def empty(self):
        if len(self.items)==0:
            return 1
        else: return 0

    def front(self):
        if len(self.items)!=0:
            return self.items[0]
        else: return -1

    def back(self):
        if len(self.items)!=0:
            return self.items[-1]
        else: return -1

dq=dq()

N = int(sys.stdin.readline())
for i in range(N):
    order = sys.stdin.readline()
    if 'push_front' in order:
        order,n=order.split()
        dq.push_front(n)
        
    elif 'pop_front' in order:
        print(dq.pop_front())
        
    elif 'front' in order:
        print(dq.front())
    
    if 'push_back' in order:
        order,n=order.split()
        dq.push_back(n)
        
    elif 'pop_back' in order:
        print(dq.pop_back())

    elif 'back' in order:
        print(dq.back())
        
    if 'size' in order:
        print(dq.size())
    if 'empty' in order:
        print(dq.empty())