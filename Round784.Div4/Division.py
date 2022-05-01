import sys
t = int(sys.stdin.readline())

def slove(a):
    if a<=1399:
        return 4
    elif a<=1599:
        return 3
    elif a<=1899:
        return 2
    else: return 1


for _ in range(0, t):
    a = int(sys.stdin.readline())
    res=slove(a)
    print('Division '+str(res))