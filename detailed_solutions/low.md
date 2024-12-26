# Detailed solution for Kattis - Low Power

[Problem statement on Kattis](https://open.kattis.com/problems/low)

Interesting binary search variant; indeed, according to Kattis metadata it was ICPC World Finals 2013 exercise.

## Tags

binary search, greedy

## Solution

The solution involves binary search on `d` where `d` is (as given in problem statement):

- "find:the smallest number `d` such that you can allocate the batteries so that the difference of power outputs of the two chips in each machine is at most `d`"

I reasoned about the placement strategy and unblocked my approach once I said to myself "what is the benefit of making the value of `d` larger" then I realised while looking at a sorted array what happens:

If you take a sorted array of the battery powers:

`[11, 13, 18, 30, 107, 112, 150, 160, 190, 1100, 1161, 2223]`

The overall smallest battery, here `B=11`, will obviously be the smallest in some chip on some machine, since there are no smaller batteries.

Now, assuming you are trying to pack the batteries such that `d <= 10`, for example, you move rightwards: `13` satisfies (`13-11 <= 10`), as does `18`, but `30` does not.

**You should pick the first battery which satisfies (i.e. greedy) - why?:**

Because each battery you skip, rightwards, can only go "above" the batteries to its left (since they are the only batteries smaller than the skipped ones)
If you "skip" a battery which satisfies difference `<= d` for a latter one which has `difference > difference' <= d`, you don't achieve any better packing
since the skipped battery must now be paired off with the +1 right battery which would have been closer to the `difference'` battery anways i.e. a valid choice - **a bit confusing to explain, here is example:**

`1  5  7  10 `

Suppose here you are trying to satisfy difference `<= (d=8)`

Then greedy is `1+5`, move to `7`, look rightwards, find `10` and pair `7+10` - OK.

If you decide to skip `5` and pair `1+7`, then you notice that `5` is further away from `10` (since it is to the left of `7` i.e. you skipped a smaller value `5` for larger `7` so `5` is **further** from later values)

- in this case the pairing does still work `1+7`, `5+10` - OK
- but if you had had `1 5 7 16`, then trying to skip `5` to somehow pair `1+7`, would leave you with `5+16` which **does not work** `(> 10)`, whereas the greedy pairing `1+5`, `7+16` **does work**. 

**So it is never better, but may be worse, to deviate from greedy choice at each step.**

Second observation: you see therefore that, as you implement above steps, you will only ever add *adjacent values* as "bottom/smallest" batteries in an optimal solution.

Why ? Because if e.g. in `[10,23,30]` with `d=5`, you find that `10` vs `23` does **not** work, then `10` vs `30` will surely not work either.

So each time you fail to find an adjacent valid greedy pair, what is happening to the "leftover" batteries? Answer: **these are the ones that must be stacked upon some previous minimal batteries in some previous chip.**

- This is the key observation!: **There is a limited number of such "space" to accept these leftover batteries**.

e.g. `[2,5,10,30,41,42,....]` with trying `d = 4`: and let's say we are in the `k=3` batteries per chip configuration

```
1. find pair 2,5 OK : assign to first machine as MACHINE1: chip1:[2 _ _ ], chip2:[5 _ _ ]

2. now test pair 10,30: can these be the 2 mimimal batteries for 2 new chips on 1 new machine?
   -> NO since 30-10 > d=4
   
   ===>>> So now we have that the battery 10 will NEVER BE THE MIMIMAL BATTERY IN ANY SUBSEQUENT CHIP, SO IT MUST SOMEHOW BE PLACED
   ON TOP OF A PREVIOUS MINIMAL CHIP:

   currently we have  MACHINE1:  chip1:[2 _ _ ], chip2:[5 _ _ ], so a total of 4 _ spaces for batteries >= 5
   
   -> at this point, we can place 10 in one of thse 4 locations, and now have 3 _ spaces remaining

3. now test pair 30,41: exact same reasoning as 2), 30 will have to go in a _ empty space: OK because we have 3 _ remaining, now down to 2.
   MACHINE1:  chip1:[2 10 30 ], chip2:[5 _ _ ] <-- note you could equally well do MACHINE1:  chip1:[2 10 _ ], chip2:[5 30 _ ], doesnt matter, since all the values from now on are >= 5, its only the NUMBER of spaces that is relevant

4. Finally we test new pair 41,42 and this satisfies requirement, so we can START A NEW MACHINE#2 with 2 chips:
   MACHINE1:  chip1:[2 10 30 ], chip2:[5 _ _ ]
   MACHINE2:  chip1:[41 _ _ ],  chip2:[42 _ _ ]

   ===>>> and now we have += our spare_capacity by +4, going to a total of 6 now.
```

So this is what determines "how far we can move ahead in sorted battery list" looking for new pairs to start new machines: you can only move forward so long as you have spare capacity to place the un-pairable batteries (like `10`, `30`, .. in the walkthrough example above).

### Implementation note

In code below, the `spare_capacity` is the variable described in the walkthrough example.

After submission, I noticed that updating the `assigned_machines += 1` and checking for `assigned_machines == machines` at the end is **not needed to get AC**

So basically it seems if you can always keep `spare capacity > 0` throughout array of `xs`, then it's logically equivalent to having the required number of machines (not 100% sure I can prove this off the top of my head, but it's AC with code commented out - I left it for reference)

## AC code

```python
machines, batteries_per_chip = map(int, input().split()) # n, k in text: was getting confused by variable names so changed

xs = sorted(map(int, input().split()))

num_batteries = len(xs)

lo = 0
hi = 9 * 10**9

while lo < hi:
    curr_d = (lo + hi) // 2 # see NOTES for what we are binary searching on

    i = 0
    ok = True
    
    #assigned_machines = 0 <=== THIS DOESNT ACTUALLY WORK/NEEDED, SEE IMPLEMENTATION NOTE

    spare_capacity = 0 # see notes above: this is the current cnt of total _ in which to place un-pairable batteries (this + and - as you go through xs)
    while i < num_batteries - 1: # Note: need -1 because are comparing i+1 with i
        if xs[i + 1] - xs[i] <= curr_d:
            # this pair can serve as the 2 minimal chips of a new machine, if needed
            # assigned_machines += 1  <=== THIS DOESNT ACTUALLY WORK/NEEDED, SEE IMPLEMENTATION NOTE
            spare_capacity += 2 * batteries_per_chip - 2 # each machine has 2 chips with batteries_per_chip batteries: we place the 2 minima, and have 2*b-2 leftover _ spaces
            i += 2 # we move on to next unused battery
        else:
            i += 1 # we cannot use the LEFT battery (see example with 10,30 and 30,41 <-- note in 30,41 we end up using 41 with 42, it is the LEFT/smaller one that is ruled out)
            spare_capacity -= 1 # we must place this unpairable battery somewhere in an existing _
            if spare_capacity < 0:
                ok = False
                break

    #if (assigned_machines == machines) and ok: <=== THIS DOESNT ACTUALLY WORK/NEEDED, SEE IMPLEMENTATION NOTE
    if ok
        # curr_d works and can try a SMALLER curr_d inclusive:
        hi = curr_d
    else:
        # curr_d does NOT work so move range
        lo = curr_d + 1

print(lo)
```
