# Pea Soup and Pancakes
# https://open.kattis.com/problems/peasoup
# TAGS: basic, interpreter
# CP4: 1.4i, Still Easy
# NOTES:
n = int(input())

flg = False

for _ in range(n):
    k = int(input())
    restaurant = input()
    soup, pancakes = False, False
    for _ in range(k):
        item_name = input()
        if item_name == "pea soup":
            soup = True
        if item_name == "pancakes":
            pancakes = True
    if (soup and pancakes):
        print(restaurant)
        flg = True
        break

if not flg:
    print("Anywhere is fine I guess")