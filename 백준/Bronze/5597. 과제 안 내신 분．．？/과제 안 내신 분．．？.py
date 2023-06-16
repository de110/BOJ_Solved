import sys
m_list=[int(sys.stdin.readline()) for i in range(28)]
my_list=list(range(1,31))
for i in my_list:
    if i not in m_list:
        print(i)