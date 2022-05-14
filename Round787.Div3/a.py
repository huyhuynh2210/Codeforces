import sys


def slove(a,b,c,x,y):
    if a-x<0:
        c=c+a-x
        if c<0:
            return 0
    if b-y<0:
        c=c+b-y
        if c<0:
            return 0
    return 1


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    a,b,c,x,y = map(int, sys.stdin.readline().strip().split())

    res = slove(a,b,c,x,y)
    if res==1:
        print('YES')
    else: print('NO')