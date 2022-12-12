import sys


def solve(n,m):
    num_s = '9'*n
    num_ss = int('1'*(n+1))
    num_s = int(num_s)

    if num_s-num < 10**(n-1):
        print(num_ss-num)
        return
    print(num_s-num)
    return



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    num = int(sys.stdin.readline().rstrip())

    solve(n,num)
    