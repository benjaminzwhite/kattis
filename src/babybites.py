# Baby Bites
# https://open.kattis.com/problems/babybites
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
"""
CARE! Don't need to try/except this part:

if x == "mumble" or int(x) == i:

due to lazy evaluation and putting the x == "mumble" check first (avoids int(x) error if x is a string)
"""
n = int(input())

flg = True
for i, x in enumerate(input().split(), 1):
    if x == "mumble" or int(x) == i:
        continue
    else:
        flg = False
        break
    
if flg:
    print("makes sense")
else:
    print("something is fishy")