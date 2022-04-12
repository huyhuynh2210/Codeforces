import sys
import math
import os

def search_2x(v):
  for y in range(1,16):
    x=v*(2**y)
    if x%32768==0:
      return y

n = int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().strip().split()))
for v in arr:
  res=[]
  count=0
  i=0
  while i<15:
    if v%32768==0:
      res.append(count)
      break
    else:
      res.append(count+ search_2x(v))
    v=v+1
    count=count+1
    i+=1
  print(min(res), end=' ')