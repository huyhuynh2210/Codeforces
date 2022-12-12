import sys


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def solve(a, n):
    pos_of_val = [-1]*1001
    for i in range(n):
        pos_of_val[a[i]] = i+1
    
    res = -1 
    for i in range(1001):
        for j in range(i, 1001):
            if gcd(i,j)==1 and pos_of_val[i]>-1 and pos_of_val[j]>-1:
                res = max(res, pos_of_val[i]+pos_of_val[j])    
    print(res)
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    solve(a, n)
