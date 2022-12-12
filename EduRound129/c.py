import sys
import math



def ss(aarr):
    ar_res=[]
    idx=0
    y=0
    while idx<len(aarr):
        while y<len(aarr) and aarr[idx]==aarr[y]:
            y +=1
        ar_res.append(idx)
        ar_res.append(y-1)
        idx=y

    return ar_res

def slove(n,a,b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    ar=a.copy()
    br=b.copy()
    if a_sorted == a and b_sorted==b:
        print(0)
        return
    
    arr=[]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if (ar[i] > ar[j]):
                ar[i], ar[j] = ar[j], ar[i]
                br[i], br[j] = br[j], br[i]
                arr.append([i,j])
    ss_idx=ss(ar)
    for i in range(0, len(ss_idx),2):
        start = ss_idx[i]
        end = ss_idx[i+1]
        if start == end:
            continue

        for x in range(start, end):
            for j in range(x + 1, end+1):
                if (br[x] > br[j]):
                    br[x], br[j] = br[j], br[x]
                    arr.append([x,j])
    if b_sorted==br:
        print(len(arr))
        for i in arr:
            print(i[0]+1,i[1]+1)
    else:
        print(-1)
    return


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b = list(map(int, sys.stdin.readline().rstrip().split()))

    slove(n,a,b)
