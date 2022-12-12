import sys

def prefix_sum(a):
    res = [0]
    for i in range(0, len(a)):
        res.append(res[-1] + a[i])
    return res

n,q = map(int, sys.stdin.readline().rstrip().split())
p = list(map(int, sys.stdin.readline().strip().split()))
p=sorted(p,reverse=True)
p_sum = prefix_sum(p)

for _ in range(0, q):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    print(p_sum[x]-p_sum[x-y])


