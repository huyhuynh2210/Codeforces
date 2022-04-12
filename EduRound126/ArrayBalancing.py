import os
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline())

    for _ in range(0, t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().strip().split()))
        b = list(map(int, sys.stdin.readline().strip().split()))

        for i in range(0, n):
            if a[i] > b[i]:
                a[i], b[i] = b[i], a[i]

        sum = 0
        for i in range(0, n-1):
            sum = sum + abs(a[i]-a[i+1]) + abs(b[i]-b[i+1])

        print(sum)
