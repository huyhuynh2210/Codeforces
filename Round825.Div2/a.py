import sys


def solve(n, a, b):
    count_a = a.count(0)
    count_b = b.count(0)
    if a==b:
        return 0
    if count_a == count_b | n==1:
        return 1
    count=0
    for i in range(n):
        if a[i]!=b[i]:
            count+=1
    return min(min(abs(count_a-count_b), abs(n-count_a-(n-count_b)))+1, count)
    



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solve(n, a, b))
