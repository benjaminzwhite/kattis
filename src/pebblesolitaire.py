# Pebble Solitaire
# https://open.kattis.com/problems/pebblesolitaire
# TAGS: string, game, logic, IMPROVE
# CP4: 8.2a, Harder Backtracking
# NOTES:
"""
IMPROVE

My current approach is simulation but I'm sure there must be a logic/proof-based
answer maybe involving binary representation of the board.
"""
from collections import deque

n = int(input())

for _ in range(n):
    s = input()
    q = deque([(s, 0)])
    seen = set()
    max_moves = 0
    
    while q:
        curr_s, curr_moves = q.popleft()
        if curr_s in seen:
            continue
        max_moves = max(max_moves, curr_moves)
        seen.add(curr_s)
        
        for i in range(len(s)):
            for k, v in {'-oo':'o--', 'oo-':'--o'}.items():
                if curr_s[i:i+3] == k:
                    s_ = curr_s[:i] + v + curr_s[i+3:]
                    q.append((s_, curr_moves + 1))
    
    res = s.count('o') - max_moves
    print(res)