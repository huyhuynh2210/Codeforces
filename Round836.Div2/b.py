import sys


def solve(n):
    # ar=[2,2,2,2,2,2,2,2,2]
    
    # so=ar[0]
    # for i in ar[1::]:
    #     so = so^i
    #     print(so, end =' ')
    # print()
    
    if n==1:
        print(1)
        return
    if n==2:
        print('1 3')
        return
    if n%2==0:
        print('1 3 '+ '2 '*(n-2))
        return
    else:
        print('2 '*n)
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    solve(n)
