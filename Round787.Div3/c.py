import sys
  

def slove(s):
    if len(s)==1:
        return 1
    if '1' not in s and '0' not in s:
        return len(s)
    for i in range(len(s)):
        if s[i]=='1':
            a=i
        if s[i]=='0':
            b=i
            break
    if '0' not in s:
        return len(s)-a
    if '1' not in s:
        return b+1

    return b-a+1

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    s = str(sys.stdin.readline().rstrip())

    a = slove(s)
    print(a)