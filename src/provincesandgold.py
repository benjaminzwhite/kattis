# Provinces and Gold
# https://open.kattis.com/problems/provincesandgold
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
"""
A bit of reading comprehension
"""
G, S, C = map(int, input().split())

total = 3 * G + 2 * S + C

# CARE! for res1 need to have possibility that total is less than 2, so can't even buy the Estate
res1 = next(v for s, v in((8, "Province or "), (5, "Duchy or "), (2, "Estate or "), (-1, "")) if s <= total)

res2 = next(t for s, t in((6, "Gold"), (3, "Silver"),(0, "Copper"))if s <= total)

print(res1 + res2)