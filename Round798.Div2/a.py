import sys

def cal_c(k,ar_chuan,br):
    c=[]
    n=len(ar_chuan)
    m=len(b)

    ngan=round(n/k)-1

    return c

def solve(n,m,k,a,b):
    ar=sorted(a)
    br=sorted(b)
    c=[]
    start_a = 0
    start_b = 0
    nn,mm=n,m
    while nn>0 and mm>0:
        end_a= min(start_a+k,n)
        end_b=min(start_b+k,m)

        arr=ar[start_a: end_a].copy()
        for y in range(len(arr)):
            if arr[y]<br[start_b]:
                c.append(arr[y])
                start_a+=1
                nn-=1
            else:
                break

        arr=br[start_b:end_b].copy()
        for y in range(len(arr)):
            if arr[y]<ar[start_a]:
                c.append(arr[y])
                start_b+=1
                mm-=1
            else:
                break
    print(c)
    return 



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n,m,k = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(str, sys.stdin.readline().strip()))
    b = list(map(str, sys.stdin.readline().strip()))
    
    solve(n,m,k,a,b)
    
