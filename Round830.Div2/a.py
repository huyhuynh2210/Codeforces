import sys

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def solve(n, ar):
    loc = [1, 2, 3, 5 ,7 ,11, 13, 17, 19][::-1]
    if n ==1:
        if ar[0]==1:
            print(0)
            return
        else:
            print(1)
            return
        
    
    for i in range(n,0,-1):
        if gcd(ar[i-1], i)==1:
            print(n-i+1)
            return
    print(n)
    return
    

t = int(sys.stdin.readline().rstrip())
print(gcd(6,2))
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    ar = list(map(int, sys.stdin.readline().strip().split()))
    solve(n, ar)
    
