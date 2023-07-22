import sys

size,k=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
ans=[]

def merge_sort(A):
    n=len(A)
    if n<=1:
        return A
    else:
        mid=(len(A)+1)//2
        left=merge_sort(A[:mid])
        right=merge_sort(A[mid:])
        return merge(left,right)

def merge(left,right):
    merged = list()
    lpoint, rpoint=0,0

    while len(left) > lpoint and len(right) > rpoint:
        if left[lpoint] > right[rpoint]:
            merged.append(right[rpoint])
            ans.append(right[rpoint])
            rpoint +=1
        else:
            merged.append(left[lpoint])
            ans.append(left[lpoint])
            lpoint +=1

    while len(left)>lpoint:
        merged.append(left[lpoint])
        ans.append(left[lpoint])
        lpoint += 1

    while len(right) >rpoint:
        merged.append(right[rpoint])
        ans.append(right[rpoint])
        rpoint +=1
        
    return merged

merge_sort(A)

if len(ans) >= k:
    print(ans[k-1])
else: print(-1)