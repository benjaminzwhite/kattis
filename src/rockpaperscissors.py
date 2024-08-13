# Rock-Paper-Scissors Tournament
# https://open.kattis.com/problems/rockpaperscissors
# TAGS: interpreter
# CP4: 1.6d, Game (Others), Harder
# NOTES:
"""
Simple just lots of weird input conditions, float formatting, etc.
"""
blank_line = False

while True:
    nk = input()
    if nk == '0':
        break
    
    if blank_line:
        print()
    
    n, k = map(int, nk.split())
    blank_line = True
    
    wins = [0] * (n + 1)
    losses = [0] * (n + 1)
    
    for _ in range(k * n * (n - 1) // 2):
        pa, a, pb, b = input().split()
        pa = int(pa)
        pb = int(pb)
        if a == b:
            continue
        game = f"{a[0]}{b[0]}"
        if game in {"pr", "rs", "sp"}:
            wins[pa] += 1
            losses[pb] += 1
        else:
            wins[pb] += 1
            losses[pa] += 1
    
    for player in range(1, n + 1):
        total = wins[player] + losses[player]
        if total == 0:
            print("-")
        else:
            res = wins[player] / total
            print(f"{round(res, 3):.3f}")