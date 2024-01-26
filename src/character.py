# Character Development
# https://open.kattis.com/problems/character
# TAGS: basic
# CP4: 5.4d, Others, Easier
# NOTES:
"""
Just count all subsets but ignore/remove subsets of size 0 (cnt=1) and size 1 (cnt=n)
"""
n = int(input())

if n < 2:
    print(0)
else:
    print((1 << n) - n - 1) # CARE! need brackets in Python due to << precedence