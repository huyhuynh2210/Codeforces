import sys


def solve(n):
    if n<=10:
        print(n)
        return
    if n<=100:
        print(10+int(n/10)-1)
        return
    if n<=1000:
        print(19+int(n/100)-1)
        return
    if n<=10000:
        print(28+int(n/1000)-1)
        return
    if n<=100000:
        print(37+int(n/10000)-1)
        return
    if n<=1000000:
        print(46+int(n/100000)-1)
        return
    
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    
    solve(n)
    
