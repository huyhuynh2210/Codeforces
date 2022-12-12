import sys

def sum_s(s):
    sum=0
    for i in range(0,len(s)-1):
        sum=sum+int(s[i]+s[i+1])
    return sum


def start_end(s,n):
    start =0
    end=0
    i=0
    while i<n:
        if s[i]=='1':
            start =i
            break;
        i+=1
    i=0
    while i<n:
        if s[i]=='1':
            end =i
        i+=1
    return start,end

def solve(n,k,s):
    start,end=start_end(s,n)
    a,b=start,end
    if start == end:
        if end+k>=n-1:
            print(1)
            return
        if end-k<=0:
            print(10)
            return
        print(sum_s(s))
        return

    sl =list(s)
    if end+k>=n-1 and k>0:
        sl[end]='0'
        sl[n-1]='1'
        k=k-(n-end-1)
    if start-k<=0 and k>0:
        sl[start]='0'
        sl[0]='1'
            
    print(sum_s(sl))
        
    return




t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n,k = map(int, sys.stdin.readline().rstrip().split())
    s = str(sys.stdin.readline().rstrip())

    solve(n,k,s)
