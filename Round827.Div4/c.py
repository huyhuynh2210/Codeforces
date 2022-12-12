import sys


def solve(arr):
    
    for i in arr:
        rc = i.count('R')
        if rc==8:
            print('R')
            return
                     
    rotated = list(list(i) for i in list(zip(*arr))[::])
    for i in rotated:
        bc = i.count('B')
        if bc==8:
            print('B')
            return
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    arr=[]
    for _ in range(9):
        arr.append(list(sys.stdin.readline().rstrip()))
    arr.pop(0)
    solve(arr)
