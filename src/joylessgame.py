# Joyless Game
# https://open.kattis.com/problems/joylessgame
# TAGS: game, logic, proof, nice
# CP4: 5.7a, Game Theory (Basic)
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/joylessgame.md
"""
T = int(input())

for _ in range(T):
    s = input()
    
    L = len(s)
    start_char = s[0]
    end_char = s[-1]
    
    if start_char == end_char:
        if L % 2 == 1:
            # start player - Chikapu - loses
            print("Bash")
        else:
            print("Chikapu")
    elif start_char != end_char: # NB: handles the edge case where s is of length 2 -> must have 2 distinct chars, so expect start player to lose -> OK
        if L % 2 == 1:
            # start player - Chikapu - wins
            print("Chikapu")
        else:
            print("Bash")