import sys
import string
S=list(sys.stdin.readline().rstrip())
alp=list(string.ascii_lowercase)
re=[-1 in range(26)]
for i in S:
    if i in alp:
        idx_alp=alp.index(i)
        idx_S=S.index(i)
        del alp[idx_alp]
        alp.insert(idx_alp,idx_S)
for i in alp:
    if str(i).isalpha():
        id_a=alp.index(i)
        del alp[id_a]
        alp.insert(id_a,-1)
print(*alp)