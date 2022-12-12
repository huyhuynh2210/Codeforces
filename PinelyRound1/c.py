from collections import Counter
import sys


def solve(n,ar):
    i=[]
    j=[]
    for x in range(n):
        for s in range(len(ar[x])):
            if ar[x][s]=="1":
                i.append(x+1)
                j.append(s+1)
    print(i,j)
    d={}
    for x in j:
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    print(d)
    
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    ar=[]
    for _ in range(n):
        ar.append(str(sys.stdin.readline().strip()))
    solve(n,ar)
    
