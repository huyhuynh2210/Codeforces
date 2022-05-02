import sys


def slove(s, t):
    if t=='a':
        return 1
    if len(t)>1 and 'a' in t:
        return -1
    return 2**len(s)


q = int(sys.stdin.readline().rstrip())
for _ in range(0, q):
    s = str(sys.stdin.readline().rstrip())
    t = str(sys.stdin.readline().rstrip())

    a = slove(s,t)
    print(a)