# Are You Listening?
# https://open.kattis.com/problems/areyoulistening
# TAGS: mathematics, geometry
# CP4: 8.7e, Geometry+CS
# NOTES:
"""
You don't actually need to brute force and try all answers; here is explanation:

You are allowed to be within 2 but not 3 of the radii of the other points, [ps].

So I find the distances to the centres of all the other points, then for each centre-distance, remove the RADIUS of that "radar point"
-> this determines whether you are inside that radar's catchment area

If you sort these effective distances (i.e. distance to the circumference/boundary of the radar zone) then you want the 3rd smallest of
these distances, which is what sets the max range of your own broadcast circle
(i.e. this allows you to touch 1st and 2nd closest radar areas, but otherwise you will reach a 3rd circle)

CARE! If distances[2] is NEGATIVE it means you are already within range of 3 devices (see problem statement): so return 0 in this case.
("Note that this range may be 0 if the broadcast device it already within the range of three listening devices.")
"""
cx, cy, n = map(int, input().split())

ps = []
for _ in range(n):
    x, y, r = map(int, input().split())
    ps.append((x, y, r)) # you can process these directly into distances[] list as done below, but this step is for clarity

distances = []

for (x, y, r) in ps:
    # distance from us to the centre:
    d = ((cx - x)**2 + (cy - y)**2)**0.5
    # distance from us to the circum
    d_cir = d - r
    distances.append(d_cir)

distances = sorted(distances)

res = int(distances[2])

if res <= 0:
    print(0)
else:
    print(res)