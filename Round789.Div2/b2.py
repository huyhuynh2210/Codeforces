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


def countpack(n,s):
    f=s[0]
    count=1
    for i in range(0,n):
        if s[i]!=f:
            count+=1
            f=s[i]
    return count

def ss(n, s):
    count=0
    for i in range(0,n,2):
        if s[i]==s[i+1]:
            count+=1
            # print('i',i, count)
            # print('s', s[i], s[i+1])

    return count

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    s = list(str(sys.stdin.readline().rstrip()))
    ss1=s.copy()
    a = slove(n, s)
    a1=ss(n,ss1)
    if a==0:
        print(a,countpack(n,ss1))
    else:
        if a1==0:
            print(a, 1)
        else: print(a, a1)
