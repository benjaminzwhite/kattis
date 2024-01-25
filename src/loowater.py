# The Dragon of Loowater
# https://open.kattis.com/problems/loowater
# TAGS: greedy
# CP4: 3.4a, Greedy (Classical)
# NOTES:
"""
- Got WA first submit due to not including ! in output string, need good glasses to solve O_o
"""
while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    
    dragons = [int(input()) for _ in range(n)]
    knights = [int(input()) for _ in range(m)]
    dragons = sorted(dragons)
    knights = sorted(knights)

    ik = 0
    res = 0
    flg = True
    for d in dragons:
        while ik < len(knights) and knights[ik] < d:
            ik += 1
        if ik < len(knights):
            res += knights[ik]
            ik += 1
        else:
            print("Loowater is doomed!")
            flg = False
            break

    if flg:
        print(res)