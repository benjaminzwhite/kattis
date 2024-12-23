# Canvas Line
# https://open.kattis.com/problems/canvasline
# TAGS: array, greedy
# CP4: 9.cons, Construction
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/canvasline.md
"""
N = int(input())

canvases = []
for i in range(N):
    l, r = map(int, input().split())
    canvases.append((l, r))

p = int(input())
PEGS = list(map(int, input().split()))

cnt = []
peg_idx = 0
flg = 1

for l, r in canvases:
    curr_cnt = 0
    while peg_idx < p and PEGS[peg_idx] < r:
        if l <= PEGS[peg_idx]:
            curr_cnt += 1
        peg_idx += 1
    if peg_idx < p and PEGS[peg_idx] == r:
        curr_cnt += 1
    if curr_cnt > 2:
        flg = 0
    cnt.append(curr_cnt)

cnt += [0, 0, 0, 0, 0]

PEGS = set(PEGS)
TO_ADD = set()
for i, (l, r) in enumerate(canvases):
    if l in TO_ADD:
        cnt[i] += 1

    greedy = r
    if cnt[i + 1] >= 2:
        greedy -= 1
    
    while cnt[i] < 2:
        TO_ADD.add(next(x for x in range(greedy, -1, -1) if x not in PEGS | TO_ADD))
        cnt[i] += 1

if flg:
    print(len(TO_ADD))
    print(*TO_ADD)
else:
    print("impossible")