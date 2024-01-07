# Basic Programming 1
# https://open.kattis.com/problems/basicprogramming1
# TAGS: basic
# CP4: 1.4j, Medium
# NOTES:
"""
- match case not currently available since Python 3.8 on Kattis
"""
N, t = map(int, input().split())

A = list(map(int, input().split()))

if t == 1:
    print("7")
if t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")
if t == 3:
    tmp = sorted(A[:3])
    print(tmp[1])
if t == 4:
    print(sum(A))
if t == 5:
    print(sum(x for x in A if x % 2 == 0))
if t == 6:
    alph = "abcdefghijklmnopqrstuvwxyz"
    print(''.join(alph[x%26] for x in A))
if t == 7:
    i = 0
    seen = set()
    flg = True
    while flg:
        if i in seen:
            print("Cyclic")
            flg = False
            break
        
        seen.add(i)
        i = A[i]
        
        if i >= N:
            print("Out")
            flg = False
            break
        
        if i == N-1:
            print("Done")
            flg = False
            break