import sys

N,K=map(int,sys.stdin.readline().split())
coins=[]
count=0

for i in range(N):
    coins.append(int(sys.stdin.readline()))

for i in range(len(coins)-1,-1,-1):    
    if K//coins[i] == 0 :
        continue
    else:
        count+= K//coins[i]
        K -= coins[i] * (K//coins[i]) # rest charge
    if K==0:
        break
        
print(count)