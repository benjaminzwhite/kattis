# Drinking Song
# https://open.kattis.com/problems/drinkingsong
# TAGS: basic, formatting
# CP4: 1.4h, Easy
# NOTES:
"""
CARE! Some tricky edge cases with plural/singular etc
"""
N = int(input())
beverage = input()

for l in range(N, 0, -1):
    if l > 1:
        print(f"{l} bottles of {beverage} on the wall, {l} bottles of {beverage}.")
        print(f"Take one down, pass it around, {l-1} bottle{(l>2)*'s'} of {beverage} on the wall.")
    
    elif l == 1:
        print(f"{l} bottle of {beverage} on the wall, {l} bottle of {beverage}.")
        print(f"Take it down, pass it around, no more bottles of {beverage}.")
    
    if l != 1:
        print()