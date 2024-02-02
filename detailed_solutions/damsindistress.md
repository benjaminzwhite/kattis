# Detailed solution for Kattis - Dams in Distress

[Problem statement on Kattis](https://open.kattis.com/problems/damsindistress)

This is a very creative and interesting exercise. It is important to read the problem statement carefully, in particular that:

"The network of dams and the war camp form a rooted tree" as this simplifies the processing of the elements. Also note that the inputs are given to you in a "nice" order.

## Tags

tree, logic, array

## Solution

The key insight you need is to realise that you can solve "locally", for each node, because of the fact that the network of dams is a tree (so, in particular, it is a directed acyclic graph - you can order the nodes by the relation "is_upstream_of" within a given connected path in the tree, and every dam has only one `parent` i.e. one dam immediately downstream of it).

Initially, starting at the base camp, the minimum water needed to flood the camp (`min_water` in code below) is the value `w` given by the test case input.

Then, working "upstream/away from the base camp", for each dam I just compare the result of "how much water this dam needs to burst" to current `min_water`: now, if the current dam - even if it bursts - would **not** match the amount of downstream water needed to break all downstream dams to target, then clearly some excess water needs to arrive at this dam.

**If you pretend that there are NO upstream dams, so that Freya must add the FULL needed amount of water at this dam,** then you can record this "full Freya amount" i.e. the difference between the `downstream_needed` amount and the current dam's `capacity`.

But then, since there are in fact some upstream dams, you continue the algorithm: you check whether you can "contribute" to this full Freya amount using some of the upstream dams. This might therefore reduce the full amount that Freya would need to add to some lower amount (maybe even 0).

### Implementation note

I used long variable names in code below to make things clear. I used a `nodes` dict for simplicity: just to be able to use the 1-base indexing (You can use an array instead, just be careful with indexing errors).

## AC code

```python
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
```