import sys

def find_str(strr, s,i):
    for y in range(i,len(s)):
        if s[y]==strr:
            return y

def _swap(s,idx,i):
    end=s[idx]
    if end=='a':
        return s
    if end=='b':
        for i in range(idx,i,-1):
            if s[i-1]=='a' and s[i]=='b':
                s[i],s[i-1]=s[i-1],s[i]
        return s

    if end=='c':
        for i in range(idx,i,-1):
            if s[i-1]=='b' and s[i]=='c':
                s[i-1],s[i]=s[i],s[i-1]
        return s


def solve(n,s,t):
    for i in range(0,n):
        if s[i]!=t[i]:
            strr=t[i]
            index=find_str(strr,s,i)
            if index is None:
                print('NO')
                return
            else:
                s=_swap(s,index,i)
            if s[i]!=t[i]:
                print('NO')
                return
    
    print('YES')
    return 


q = int(sys.stdin.readline().rstrip())
for _ in range(0, q):
    n = int(sys.stdin.readline().rstrip())
    s = list(map(str, sys.stdin.readline().strip()))
    t = list(map(str, sys.stdin.readline().strip()))

    solve(n,s,t)