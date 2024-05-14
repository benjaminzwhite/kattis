# Plants vs Bad Guys
# https://open.kattis.com/problems/pvbg
# TAGS: basic
# CP4: 1.6c, Game (Others), Easier
# NOTES:
N = int(input()) # not needed actually

xs = map(int, input().split())

res = min(xs) + 1

print(res)