import sys

def print_res(a, ar):
    res = []
    
    i=0
    while i<n-1:
        if a[i] == ar[i] and a[i+1]==ar[i+1]:
            res.append([i+1,i+1])
            if i ==n-2:
                res.append([n,n])
        else:
            res.append([i+1,i+2])
            i+=1
        i+=1
        
        
    print(len(res)) 
    for i in range(len(res)):
        for j in range(len(res[i])):
            print(res[i][j], end= ' ')
        print('')
    
            

def solve(n, a):
    ar = a.copy()
    if n%2 == 1:
        print(-1)
        return
    
    tru = sum(ar)/2
    if tru>0:
        i=1
        while i<n:
            if ar[i]>0:
                ar[i] = (-1)*ar[i]            
                tru-=1
                i+=1
            if tru==0:
                break
            i+=1
             
    if tru<0:
        i=1
        while i<n:
            if ar[i]<0:
                ar[i] = (-1)*ar[i]            
                tru+=1
                i+=1
            if tru==0:
                break 
            i+=1
            
    print_res(a, ar)
    return
    

t = int(sys.stdin.readline().rstrip())

for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    solve(n, a)
    
