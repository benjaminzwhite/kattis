# Hunt The Wumpus
# https://open.kattis.com/problems/huntthewumpus
# TAGS: grid, geometry
# CP4: 2.2d, 2D Array, Harder
# NOTES:
from math import floor

s = int(input())

# NOTES: only slight gotcha is that the locations have to be DISTINCT
# so if you append first 4 values to a list from a given seed, you might 
# get duplicates - so add to set while you dont have 4 distinct values
wumpus_locations = set()
while len(wumpus_locations) < 4:
    s = s + floor(s / 13) + 15
    tmp = str(s)[-2:].zfill(2)
    wumpus_locations.add(tmp)

moves = 0
while True:
    try:
        guess = input()
        moves += 1
        if guess in wumpus_locations:
            wumpus_locations.discard(guess)
            print("You hit a wumpus!")
        # min distance
        if len(wumpus_locations) > 0:
            min_dist = min(abs(int(s[0]) - int(guess[0])) + abs(int(s[1]) - int(guess[1])) for s in wumpus_locations)
            print(min_dist)
    except EOFError:
        print(f"Your score is {moves} moves.")
        break