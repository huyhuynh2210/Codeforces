import sys
import math

def slove(n, s):
    count=0
    cou=0
    pas = s[0]
    for i in range(0, n):
        cur=s[i]
        if pas == cur:
            cou+=1
        else:
            if cou%2==1:
                count +=1
                s[i]=pas
                pas=cur
                cou=0
            else:
                pas=cur
                cou=1
    return count


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    s = list(str(sys.stdin.readline().rstrip()))
    a = slove(n, s)
    print(a)
