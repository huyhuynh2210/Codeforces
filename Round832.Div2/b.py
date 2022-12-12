import sys


def solve(n):
    ar = ['B','A','N']*n
    
    c=0
    i,j=0, 3*n-1
    res=[]
    while i<j:
        while i < j and ar[i] != 'B': i += 1
        while i < j and ar[j] != 'N': j -= 1
        if i >= j: break
        c += 1
        res.append([i+1, j+1])
        i += 1
        j -= 1
    
    print(c)
    for i in range(len(res)):
        print(res[i][0],res[i][1])
    
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    
    solve(n)
    
