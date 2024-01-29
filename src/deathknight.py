# Death Knight Hero
# https://open.kattis.com/problems/deathknight
# TAGS: basic, string
# CP4: 6.4a, String Matching
# NOTES:
n = int(input())

res = 0

for _ in range(n):
    s = input()
    if "CD" not in s:
        res += 1
        
print(res)