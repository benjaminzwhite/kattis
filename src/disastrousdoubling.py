# Disastrous Doubling
# https://open.kattis.com/problems/disastrousdoubling
# TAGS: basic
# CP4: 2.2i, Big Integer
# NOTES:
n = int(input())
removes = map(int, input().split())

have = 1
flg = True
for remove in removes:
    have *= 2
    have -= remove
    if have < 0:
        flg = False
        break

if flg:
    print(have % (10**9 + 7))
else:
    print("error")