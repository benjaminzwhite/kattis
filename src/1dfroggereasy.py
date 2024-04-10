# 1-D Frogger (Easy)
# https://open.kattis.com/problems/1dfroggereasy
# TAGS: array, interpreter
# CP4: 0, Not In List Yet
# NOTES:
"""
A bit overranked compared to actual difficulty - maybe because of some tricky reading comprehension:

- s is 1 indexed

- all the stuff about |k| absolute k +- for left/right: it's just "add the value in the xs array", which will be - or + accordingly

- the case for left and right isn't illustrated in the testcases so you have to guess the interpretation; does the game end:
B) when you WOULD make a move that takes you off board ? or
A) after you make a move that DOES take you off the board (i.e. +1 count compared to option A) ?

-> the exercise expects interpretation B), so you make the off-board move
"""
n, s, m = map(int, input().split())
xs = list(map(int, input().split()))

cnt = 0
seen = set()

while True:
    curr = xs[s - 1] # s is 1-based index
    if s - 1 in seen:
        print("cycle")
        break
    seen.add(s - 1)
    if curr == m:
        print("magic")
        break
    s = curr + s
    cnt += 1
    if s < 1:
        print("left")
        break
    if s > n:
        print("right")
        break

print(cnt)