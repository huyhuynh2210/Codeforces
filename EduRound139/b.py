import sys


def solve(n,st):
    res =st[0]
    for i in range(1,n-1):
        if st[i:i+2] in res:
            print('YES')
            return
        else:
            res=res+st[i]
    
    print("NO") 
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    st = str(sys.stdin.readline().strip())
    solve(n,st)
    
