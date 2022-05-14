import sys
import math

def slove(n, arr):
    dic =dict()
    for i in arr:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    a=dic[max(dic, key=dic.get)]
    if 0 in arr: 
        return n-(dic[0])
    if a>=2: return n

    return n+1


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    a = slove(n, arr)
    print(a)
