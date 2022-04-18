import sys
t = int(sys.stdin.readline())
for _ in range(0, t):
  n = int(sys.stdin.readline())
  arr=list(map(int,sys.stdin.readline().strip().split()))
  b=dict()
  for i in arr:
    if i in b:
      b[i] += 1
    else:
      b[i] = 1
  
  c=b[max(b, key=b.get)]
  count = 0
  if n==1:
    count=0
  else:
    while c<=n:
      if c==n:
        break
      if 2*c<=n:
        count=count+c+1
        c=2*c
      elif 2*c>n:
        count = count + c-(2*c-n)+1
        c=c+(c-(2*c-n))
  print(count)