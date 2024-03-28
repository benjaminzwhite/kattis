# Star Battles I
# https://open.kattis.com/problems/starbattles1
# TAGS: grid, array
# CP4: 2.2c, 2D Array, Easier
# NOTES:
REGIONS = {k:[] for k in map(str, range(10))}
MOVES = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr or dc)]

region_info = [input() for _ in range(10)]
star_info = [input() for _ in range(10)]

flg = True
for r, row in enumerate(star_info):
    if row.count('*') != 2:
        flg = False
    for c, cell in enumerate(row):
        if cell == '*':
            for dr, dc in MOVES:
                if 0 <= (r_ := r + dr) < 10 and 0 <= (c_ := c + dc) < 10 and star_info[r_][c_] == '*':
                    flg = False
            curr_region = region_info[r][c]
            REGIONS[curr_region].append((r, c))

for col in zip(*star_info):
    if col.count('*') != 2:
        flg = False

if all(len(v) == 2 for v in REGIONS.values()) and flg:
    print("valid")
else:
    print("invalid")