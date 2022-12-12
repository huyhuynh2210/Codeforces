import sys


def solve(ar, n):
    countA = ar.count('A')
    countQ = ar.count('Q')
    if countA<countQ or ar[-1]=='Q':
        print('No')
        return
    A = 0
    Q = 0
    for i in range(n):
        if ar[i] == 'Q':
            if A>=Q:
                A=0
                Q=0
            Q+=1
        else:
            A+=1
            
    if A>=Q:
        print('Yes')
    else: 
        print('No')            
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    ar = str(sys.stdin.readline().strip())
    solve(ar, n)
