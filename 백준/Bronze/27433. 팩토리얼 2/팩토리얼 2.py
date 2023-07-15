import sys
N=int(sys.stdin.readline())
def factorial(count):
    if count==1:
        return 1
    elif count==0:
        return 1
    return count*factorial(count-1)
print(factorial(N))