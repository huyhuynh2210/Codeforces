import sys


def slove(n):
    kitu=[]
    for i in n:
        if i not in kitu:
            kitu.append(i)
    print(kitu)
    s= len(kitu)
    char=n[0:s]
    for i in range(0,len(n),s):
        if char!=n[i:i+s]:
            return 0
    return 1


t = int(sys.stdin.readline())
for _ in range(0, t):
    n = str(sys.stdin.readline().rstrip())
    
    a=slove(n)
    if a==1:
        print('YES')
    else: print('NO')
    
