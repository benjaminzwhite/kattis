# Orderly Class
# https://open.kattis.com/problems/orderlyclass
# TAGS: array, nice
# CP4: 6.2f, Really Ad Hoc
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/orderlyclass.md
"""
s = input()
t = input()

l, r = 0, len(s) - 1
while l < len(s):
    if s[l] == t[l]:
        l += 1
    else:
        break
while r >= 0:
    if s[r] == t[r]:
        r -= 1
    else:
        break

if l <= r:
    segment = s[l:r+1]
    if segment[::-1] == t[l:r+1]:
        pair_cnt = 0
        l -= 1
        r += 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            pair_cnt += 1
        res = 1 + pair_cnt # CARE: +1 because you have the original_segment itself in the worst case as 1 option, even if no surrounding pairs

print(res)