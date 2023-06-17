import sys
i=int(sys.stdin.readline())
s_list=[]
for j in range(i):
    S=sys.stdin.readline()
    s_list.append(S[0]+S.strip()[-1])
print(*s_list,sep='\n')