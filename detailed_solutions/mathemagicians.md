# Detailed solution for Kattis - Mathemagicians

[Problem statement on Kattis](https://open.kattis.com/problems/mathemagicians)

A nice reasoning puzzle.

## Tags

logic

## Solution

Think about it like a necklace with beads: focus on some part of a given necklace:

```
...OOOOOxxxxOOOO....
```

You can always "shift the boundaries" of any region of x's so long as there is at least one 'O' on each end:

```
...OOOOOxxxxOOOO....
...OOOOOOxxxOOOO....
...OOxxxxxOOOOOO....
...OOOOOOxOOOOOO.... <-- can reduce region size down to 1 if you want
...OOOOOOOOOOOOO.... <-- can reduce region size down to 0 also
```

Note however that you **cannot create any new regions**:

```
...OxxxxxO..
      ^___ if you want a 'O' to appear here (i.e. create 1->3 regions)
           you need an 'O' on either immediate L or R -> if you pursue this recursively, you find that you essentially have to "flood fill"
           all the way to the closest 'O' on the left or the right:
           ...OOOxxxO...
                 ^____ now this x is adjacent with an 'O' so can itself be flipped to O => but now of course, doing so will merge it into the left region of O's and not create a new one
```

So the relevant thing to focus on is the **boundaries between regions** in the beginning and end strings:

- if there are FEWER regions in the end than the beginning, then it is always possible (can always merge ends and -1 a region: ...OxxxO... => ...O|OOO|O... )
- if there are MORE regions in the end than the beginning then it is NEVER possible (can't create regions)

Then consider some **edge cases**: if there are the exact same number of regions in start and end:

```  
XXOOXXOOOOXX
XOOOOXOXXXXX
```
Then as per the fundamental "boundary shifting operation" you can **always** match the ending **as long as there is at least one "free" location to move around with**:

```
(think of it as an empty space/placeholder):
XOOOXXX

to

XXXXOXX
```

the above can be done because you can fill up to `XXXOXXX`, then change right X to O, `XXXOOXX`, then resume with the last X->O: `XXXXOXX`.

This was only possible because of the "free location". **Meanwhile as the testcase shows, if you have e.g.**:

```
XOXO

to

OXOX
```

you need to pick one of the chars in the beginning string to flip first - whichever one you pick: `OOXO`,`XXXO`,`XOOO`,`XOXX` you **reduced the number of boundaries** to do so, and you will never be able to create it back again i.e. the configuration forces you into an operation that reduces number of boundaries, therefore you can't increase back to match the end state's number of boundaries.

So in summary this can be expressed as "number of boundaries needs to be < size of string".

Also, by the above reasoning: since you are focussing on boundaries, and in any cases the only way to "flip" anything is to use a boundary, it follows logically that you must have at least 1 boundary to perform any number of changes.

Since the input says that "It is guaranteed that not every mathemagician is happy with their hat color in the beginning" this means that the number of changes needed to perform is always non-zero, so by the above logical reasoning, **there must be at least one boundary in the beginning string in all cases** else you can never perform any flips to get the changes started.

### Clarification

Rereading my notes, there's a part that is unclear about the number of boundaries < size of string: focus on a particular testcase that I used while debugging:

```
beginning = "OXOXOX"
end = "XXXXXX"
```

In this case, the beginning_boundaries are == 6 which is == len(beginning) so my original claim/solution that:
```
if 0 < boundaries_e <= boundaries_b < n:
    print("yes")
else:
    print("no")
```

would return `no` when the answer is clearly `yes`.

The reason is that the "0 < boundaries b < n" condition is only relevant in the case where `boundaries_e == boundaries_b`, so these 2 clauses should be **separate**:

if `boundaries_e < boundaries_b` (as in above testcase), even if `boundaries_b == n`, you can still *merge* the regions and "lose" regions, that's OK. However if `boundaries_e == boundaries_b`, this is when you need `boundaries_b < n`, so that (see paragraph in the nots above) you can indeed "have space to move around".

## AC code

```python
n = int(input())
beginning = input()
end = input()

boundaries_b = sum(c1 != c2 for c1, c2 in zip(beginning, beginning[1:] + beginning[0]))
boundaries_e = sum(c1 != c2 for c1, c2 in zip(end, end[1:] + end[0]))

if boundaries_e < boundaries_b:
    print("yes")
elif boundaries_e == boundaries_b:
    # need to check that you have "space to move around" see notes
    if 0 < boundaries_b < n:
        print("yes")
    else:
        print("no")
else:
    # boundaries e > boundaries_b is always impossible
    print("no")
```