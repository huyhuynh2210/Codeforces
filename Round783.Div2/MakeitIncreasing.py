import sys

def slove(n,arr):
    b=[0]*len(arr)
    count=[]
    for i in range(0,n):
        b=[0]*len(arr)
        cou=0

        y=i
        while y!=0:
            while b[y-1]>=b[y]:
                b[y-1]=b[y-1]-arr[y-1]
                cou +=1
            y=y-1
        
        y=i
        while y!= n-1:
            while b[y+1]<=b[y]:
                b[y+1]=b[y+1]+arr[y+1]
                cou +=1
            y=y+1  
        count.append(cou)
    return min(count)

if __name__ == '__main__':
    n=int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    a=slove(n,arr)
    print(a)