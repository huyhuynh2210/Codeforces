import sys


def solve(l,r,x,a,b):
    if a==b:
        print(0)
        return
    
    if (a+x>r and a-x<l) or (b+x>r and b-x<l):
        print(-1)
        return
    
    if a+x<=b or a-x>=b:
        print(1)
        return
    
    if (a<b and (b+x>r and a-x<l)) or (a>b and (a+x>r and b-x<l)):
        print(3)
        return
   
    print(2)
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    l,r,x = map(int, sys.stdin.readline().strip().split())
    a,b = map(int, sys.stdin.readline().strip().split())
    solve(l,r,x,a,b)
    
