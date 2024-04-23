# Dams in Distress
# https://open.kattis.com/problems/damsindistress
# TAGS: tree, logic, array, nice
# CP4: 3.5g, DP level 2
# NOTES:
"""
Nice exercise - I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/damsindistress.md
"""
n, w = map(int, input().split())

nodes = {} # dict k:v is {parent: water needed to flood entire path down to target}
nodes[0] = w  # -> initialize with node0 which is the base camp, which can always be directly flooded with w water
# The point of the exercise is "Can we do better than this amount, w, by breaking some upstream dams ?"

min_water = w # this is storing the min poss result in loop

for node_id in range(1, n + 1):
    parent, capacity, curr_level = map(int, input().split())    
    downstream_needed = nodes[parent]
    this_dam_water_needed = capacity - curr_level
    if downstream_needed > capacity: # Even if you break this dam, it would not suffice alone to break downstream dams...
        this_dam_water_needed += (downstream_needed - capacity) # ... so pretend that Freya adds the full amount needed "here" so that the amount flowing downstream is just enough to meet current total needed requirement
    min_water = min(min_water, this_dam_water_needed)
    nodes[node_id] = this_dam_water_needed

print(min_water)