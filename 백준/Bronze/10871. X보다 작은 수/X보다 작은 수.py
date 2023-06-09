N,X=map(int,input().split())
A=list(map(int,input().split()))
sum=''
for i in range(N):
    if A[i]<X:
        sum+=str(A[i])+' '
print(sum)