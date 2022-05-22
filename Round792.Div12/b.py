import sys

def slove(a,b,c):
    z=c
    y=b+z
    x =y+a
    return x,y,z



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())

    x,y,z = slove(a,b,c)
    print(x,y,z)
