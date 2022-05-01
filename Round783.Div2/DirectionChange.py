import sys
t = int(sys.stdin.readline())

def slove(n,m):
    if n*m==2:
        return 1
    elif (n==1 and m>2) or (m==1 and n>2):
        return -1

    if n==m:
        return 2*(n-1)
    else:
        a=(abs(n-m)/2) *4
        if (m+n)%2 == 0:
            return 2*(min(n,m)-1) +int(a)
        else: return 2*(min(n,m)-1) +int(a) -1

for _ in range(0, t):
    n,m = map(int, sys.stdin.readline().strip().split())
    a=slove(n,m)
    print(a)