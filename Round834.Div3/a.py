import sys


def solve(ar):
    st = 'Yes'*int(len(ar)/3+4)
    if ar in st:
        print('YES')
    else:
        print('NO')
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    ar = str(sys.stdin.readline().strip())
    solve(ar)
    
