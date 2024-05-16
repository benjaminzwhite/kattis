# Array of Discord
# https://open.kattis.com/problems/arrayofdiscord
# TAGS: array, nice, improve
# CP4: 9.cons, Construction
# NOTES:
"""
TODO: IMPROVE: I didn't try to refactor my first solution, surely can make it DRYer and clearer, avoid all the flags and breaks etc

Basically all you need to do is check that 2 adjacent x's have same len (else move on to next pair, since can never meet the criterion)

Then so long as head of a,b are not 1,9 respectively you can either increment the former to 9 or decrement the latter to 1 respectively

I handle the single digit cases clunkily, maybe a more elegant way to do it?
"""
n = int(input())
xs = list(input().split())

flg = False
for i, (l, r) in enumerate(zip(xs, xs[1:]), 1): # enumerate from 1, i points to RIGHT element in l,r in xs
    ll = len(l)
    lr = len(r)
    if ll != lr:
        continue
    elif ll == 1:
        if l != '0':
            xs[i] = '0'
            flg = True
            break
        elif r != '9':
            xs[i - 1] = '9'
            flg = True
            break
    else:
        a, b = l[0], r[0]
        if a == '1' and b == '9':
            continue
        else:
            if a != '1':
                tmp = '1' + r[1:]
                xs[i] = tmp
                flg = True
                break
            else:
                tmp = '9' + l[1:]
                xs[i - 1] = tmp
                flg = True
                break

if flg:             
    print(*xs)
else:
    print("impossible")