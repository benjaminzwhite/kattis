# Scaling Recipe
# https://open.kattis.com/problems/scalingrecipe
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
n, recipe, need = map(int, input().split())

for _ in range(n):
    a = int(input())
    res = a * need // recipe
    print(res)