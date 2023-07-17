import sys
N=int(sys.stdin.readline())
def recursion(s, l, r,count):
    count+=1;
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1,count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)

for i in range(N):
    s = sys.stdin.readline().rstrip()
    S=str(isPalindrome(s))
    S=S.replace(',','').strip("()")
    print(S)
