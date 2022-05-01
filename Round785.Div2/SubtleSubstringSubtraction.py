import sys

def diem(str):
    score=0
    for i in range(0, len(str)):
        score = score + ord(str[i])-96
    return score

def slove(s):
    Alice =0
    Bob=0
    a=len(s)

    if a==1:
        Bob=diem(s)
    elif a%2==1:
        if ord(s[0])>ord(s[a-1]):
            Alice = diem(s[0:a-1])
            Bob = diem(s[a-1])
        else:
            Alice = diem(s[1:a])
            Bob = diem(s[0])
    else:
        Alice = diem(s)
        Bob = 0

    return Alice, Bob


t = int(sys.stdin.readline())
for _ in range(0, t):
    s = str(sys.stdin.readline().rstrip())

    alice,bob=slove(s)
    if alice>bob:
        print('Alice '+str(alice-bob))
    else: print('Bob '+str(bob-alice))