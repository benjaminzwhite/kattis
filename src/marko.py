# Marko
# https://open.kattis.com/problems/marko
# TAGS: array
# CP4: 2.3e, Hash Table (map), E
# NOTES:
n = int(input())
words = [input() for _ in range(n)]
code = input()

d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
res = 0

for word in words:
    if all(c in d[n] for c, n in zip(word, code)):
        res += 1

print(res)