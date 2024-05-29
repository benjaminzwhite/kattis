# Detailed solution for Kattis - Clock Construction

[Problem statement on Kattis](https://open.kattis.com/problems/clockconstruction)

This is a quite highly ranked exercise, but which has a simple solution if you think about it and use a bit of geometrical visualisation.

## Tags

logic, array

## Solution

If 2 different pixels, p1 and p2, are always ON together and always OFF together in all possible pictures, then they could be "activated" by the same switch - this is what the exercise statement means by "pixel groups".

So it seems like a good idea to focus on pixels and record - for each pixel - which pictures it is ON in, and which pictures it is OFF in.

This defines a "pixel pattern group" behavior and **all pixels which share that pattern belong to the same group** (quite hard to explain in words, example below will make it clear, but basically the fundamental thing to look at is "how many different patterns are there of ON and OFF" and realise that **each pattern requires its own separate group**)

So, referring to the sample input: imagine stacking the `N = 3` pictures like a pile of papers and piercing through it perpendicularly with a cocktail stick at the location of each of the `H * W = 6` pixels: each such column that cuts through the `N = 3` images will define a binary on-or-off pattern of length `3`.

e.g. with the testcase, focusing on the top left pixel across `N = 3` pictures we have the column pattern : `* * .`, the top middle column pattern is `. * .`, the top right column pattern is `. . .`, etc.

If you do this for all `H * W = 6` pixels, you will find that there are `4` distinct such "column patterns" in the given testcase, which is the answer we are looking for.

Finally, for implementation/code below: all we are doing is some Python slicing to get these column patterns, by flattening the entire input to a single long string and then accessing the "column patterns".


## AC code

```python
N, H, W = map(int, input().split())

flattened_pictures = []
for _ in range(N * H):
    flattened_pictures.extend(input())

# the patterns now are the "period W * H" string slices in the flattened_pictures
patterns = [tuple(flattened_pictures[i::W * H]) for i in range(W * H)]

# take the set() to get the number of distinct groups
print(len(set(patterns)))
```