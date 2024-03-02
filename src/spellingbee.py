# Spelling Bee
# https://open.kattis.com/problems/spellingbee
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
ref = input()

n = int(input())

for _ in range(n):
    t = input()
    if len(t) > 3 and not bool(set(t).difference(set(ref))) and ref[0] in t:
        print(t)