# Laptop Sticker
# https://open.kattis.com/problems/laptopsticker
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
wc, hc, ws, hs = map(int, input().split())

if wc - 2 >= ws and hc - 2 >= hs:
    print(1)
else:
    print(0)