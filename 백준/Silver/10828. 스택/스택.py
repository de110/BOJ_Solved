import sys

class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def empty(self):
        return int(not self.items)
    def top(self):
        if self.empty():
            return -1
        else:
            return self.items[-1]

stk = stack()

N=int(sys.stdin.readline())
for i in range(N):
    order=sys.stdin.readline()
    if 'push' in order:
        order,n=order.split()
        stk.push(n)
    if 'top' in order:
        print(stk.top())
    if 'size' in order:
        print(stk.size())
    if 'empty' in order:
        print(stk.empty())
    if 'pop' in order:
        print(stk.pop())