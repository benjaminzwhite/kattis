# Detailed solution for Kattis - Please, Go First

[Problem statement on Kattis](https://open.kattis.com/problems/pleasegofirst)

This is a really cool array processing kind of problem, especially to find a *O(n)* solution.

## Tags

proof, array

## Solution

The groups are constrained by their rightmost member, iterate from r-to-l, assign all group members the `score` corresponding to current longest wait - this variable is decremented by the group size of each preceding group:

e.g. with the sample test (chars and their rightmost group member's index BEFORE AND AFTER the rearrangement process):

```
A b 9 A A b 2 b C 2 ->  9 A A A b b b C 2 2   <--- group labels
4 7 2 4 4 7 9 7 8 9 ->  0 3 3 3 6 6 6 7 9 9
                               ^^^^---- these are scores in final string
   ^^^^------ these are the "scores" in initial string
```

Initially `curr_longest_wait` is `9`:

So iterating r-to-l over the input `s` you treat Group labelled '2' which has `cnt = 2` members: their new position saves `2 * (9 - 9) = 0`

Update `curr_longest_wait` to `7` (which you get from `9 - 2` above, where 2 is because theere were 2 members in PREVIOUS treated group).

Now, still moving r-to-l, treat next Group which is labelled 'C' which has `cnt = 1` members: their new position saves `1 * (old_score:8 - "new_score = curr_longest_wait":7) = 1` point, etc.

## AC code

```python
T = int(input())

for _ in range(T):
    _ = input()
    s = input()

    d = {}

    for i,x in enumerate(s):
        # store HOW MANY PEOPLE ARE IN EACH GROUP, and SCORE i.e. RIGHTMOST INDEX for each group
        if x not in d:
            d[x] = (1, i)
        else:
            cnt, score = d[x]
            d[x] = (cnt+1, i)

    seen = set()
    curr_longest_wait = len(s)-1
    savings = 0

    for x in s[::-1]:
        if x in seen:
            continue
        seen.add(x)
        cnt, score = d[x]
        savings += cnt * (score - curr_longest_wait)
        curr_longest_wait -= cnt

    print(savings * 5) # you have to multiply the number of saved positions by 5 seconds for some reason
```