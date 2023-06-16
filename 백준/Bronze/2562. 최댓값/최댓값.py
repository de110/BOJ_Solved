import sys
my_list=[int(sys.stdin.readline()) for i in range(9)]
print(max(my_list),my_list.index(max(my_list))+1)