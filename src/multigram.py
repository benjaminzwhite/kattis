# Multigram
# https://open.kattis.com/problems/multigram
# TAGS: brute force
# CP4: 6.7a, Anagram
# NOTES:
s = input()

L = len(s)
flg = True

for d in range(1, L // 2 + 1):
    if L % d == 0:
        ref = sorted(s[:d])
        if all(sorted(s[i:i+d]) == ref for i in range(0, L, d)):
            print(s[:d])
            flg = False
            break
            
if flg:
    print(-1)