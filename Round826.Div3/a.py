import sys


def solve(a, b):
    dic = {
        'S' : 1,
        'M' : 2,
        'L' : 3       
    }
    if dic[a[-1]] > dic[b[-1]]:
        print('>')
        return
    if dic[a[-1]] < dic[b[-1]]:
        print('<')
        return
    x = a.count('X')
    y = b.count('X')
    if dic[a[-1]] == dic[b[-1]]:
        if x>y:
            if dic[a[-1]]!=1:
                print('>')
                return
            else: 
                print('<')
                return
        
        if x<y:
            if dic[a[-1]]!=1:
                print('<')
                return
            else: 
                print('>')
                return
        if x==y: 
            print('=')
            return
    return
    



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    solve(a, b)
