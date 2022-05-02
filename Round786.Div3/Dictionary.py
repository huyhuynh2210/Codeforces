import sys

def init():
    dic = dict()
    index =1
    for i in range(97,123):
        for y in range(97,123):

            if i==y:
                continue
            else: 
                str = chr(i)+chr(y)
                dic[str]= index
                index+=1
    return dic    

def slove(s):
    return dic[s]

dic=init()
t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    s = str(sys.stdin.readline().rstrip())

    a = slove(s)
    print(a)