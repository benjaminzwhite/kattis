# Game Rank 
# https://open.kattis.com/problems/gamerank
# TAGS: interpreter
# CP4: 1.6c, Game (Others), Easier
# NOTES:
"""
It's the Hearthstone ranking system
"""
s = input()

# stars[0] is dummy, so that we can have 1-based indexing --> stars[rank] = number of stars needed in each rank 1->25
stars = [-1] + [5] * 10 + [4] * 5 + [3] * 5 + [2] * 5

curr_rank = 25
curr_wins = 0
curr_stars = 0

legend = False # just for convenience, can just use curr_rank == 0 as flag boolean instead

for c in s:
    if c == 'W':
        curr_wins += 1
        curr_stars += 2 if (curr_wins >= 3) and (6 <= curr_rank <= 25) else 1 # NB: +2 stars if bonus requirement(s) are satisfied (there are 2 requirements, >=3winstreak AND 6<=25 curr rank)
        if curr_stars > stars[curr_rank]:
            curr_stars -= stars[curr_rank]
            curr_rank -= 1
            if curr_rank == 0:
                legend = True
                print("Legend")
                break
    elif c == 'L':
        curr_wins = 0 # reset winstreak to 0
        if curr_rank <= 20:
            if curr_stars > 0:
                curr_stars -= 1
            else:
                if curr_rank != 20:
                    curr_rank += 1
                    curr_stars = stars[curr_rank] - 1

if not legend:
    print(curr_rank)