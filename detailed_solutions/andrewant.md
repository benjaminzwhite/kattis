# Detailed solution for Kattis - Andrew the Ant

[Problem statement on Kattis](https://open.kattis.com/problems/andrewant)

A classic puzzle with a nice twist - you need to find which ant(s) is the actual one that falls off the log last.

## Tags

logic

## Solution

### First part of solution

I use what I call the "Mario Kart Ghost" trick: imagine the ants are ghosts - when they bump into eachother, they  pass right through instead of changing directions. So the longest distance for any of the ghost ants to fall off is their original distance from the edge that they are aimed at.

Now split this into the 2 directions (unlike with the standard version of this problem where you just care about the `max_distance` to any edge):

- `max_left_distance_travelled` = max(all leftfacing ants to x=0)
- `max_right_distance_travelled` = max(all rightfacing ants to x=L)

Of course the **overall** result is the max of these 2, but you can use them separately for the next part.

### Second part of solution

Here you have to work out which ant is the **actual** (not the "ghost ant" now) ant that fall(s) off last:

1. Since each ant collision starts with a R facing and L facing and produces a R facing and L facing: **the total number of ants moving L and the total number of ants moving R is invariant**
2/ So in total, if `acc_L` is number of leftmoving initially, then `acc_L` ants will, after all collisions, fall off the left edge. Similarly for `acc_R`rightmoving ants.
3/ **If you think about it physically, or draw the actual dynamics out, the collision process always turns the first `acc_l` ants on the beam to being the final `acc_l` ants that fall off the left edge**, see illustration below:

```
<-   ->   <-   -> -> -> -> ->   <-   <-   Initial state: there are 4 leftmoving ants and 6 rightmoving ants
a    b    c    d
```

Above, `a` clearly falls of left edge. So does `b`, it bumps into `c` and there are no more righmoving ants to its left to swap direction with. `c` also falls off left edge: it bumps into `b`, then if you resolve the complex colliions between all the stuff on the right, it will eventually encounter `a <-` and will bump off it, so move leftwards again, and fall off etc.

A clearer general proof is: an ant, e.g. `b`, cannot fall off righwards so long as there are "leftmoving ants ahead of it" (in this case to its right)

The number of leftmoving ants ahead of each ant changes as you process the arr from l to r:

- After a, there are 3 remaining leftmoving ants not accounted for
- After b, b will have turned into a leftmoving and and flipped a later leftmoving ant to rightmoving, so there are 2 leftmoving ants unaccounted for
- After c, (which in this case has flipped from its original direction), c will have turned into a leftmoving and and flipped a later leftmoving ant to rightmoving, so there are 1 leftmoving ants unaccounted for
- After d, (which in this case has flipped from its original direction), d will have turned into a leftmoving and and flipped a later leftmoving ant to rightmoving, so there are 0 leftmoving ants unaccounted for

So indeed it is the first 4 ants that end up as leftmovingm i.e. 4 being equal to the **initial number** of leftmoving ants overall 

So putting this together:

Since the first `acc_L` ants end up being the ones that fall off the left edge, and the last `acc_R` ants are those that fall off the right edge, then in the **sorted ants list**, look up the `acc_L`'th ant, and the **minus** `acc_R`'th ant - **note: this is just the `(acc_L + 1)`st ant of course.**

```
  abcd|efghij    <-- here we have the initial config of the ants, and there are acc_L = 4 leftmoving and acc_R = 6 rightmoving
                 <-- by the above, abcd will fall off the LEFT edge, efghij will fall of the RIGHT edge
     ^|^         

!! So the only 3 cases/possibilities for "last ant on stick" are ant: d, e, or ants: d==e if they take the same time to fall off
```

In the above, ant d is in **position** `acc_L` and ant e is in **position** `- acc_R` from the right, i.e. `acc_L + 1` from the left.

### Implementation

Implementing the above logic - careful `acc_L` is a **position**, so `index - 1` if you use indexing:

Given that you have computed: `max_left_distance_travelled` and `max_right_distance_travelled`, the max distance travelled by any ant is `max(max_left, max_right)`.

Then check if:

1. `max_left > max_right`: then we are in situation "d" in the illustration above i.e. the actual ant that travels the max_distance is the "last" of the `acc_L` first ants
2. `max_right > max_left`: we are in situation "e" above
3. `max_right == max_left`: we are in situation "d == e" above, both the ants d and e travel `max_distance`

**NOTE:** after rereading my comments, it's a `max_time` rather than `max_distance` but same logic, the speed is 1 distance/time so it all works out.

## AC code

```python
while True:
    try:
        L, num_ants = map(int, input().split())
        
        ants = []
        acc_L, acc_R = 0, 0
        max_left_time, max_right_time = -1, -1
        for _ in range(num_ants):
            x, direction = input().split()
            x = int(x)

            if direction == 'L':
                acc_L += 1
                max_left_time = max(max_left_time, x) # ant travels leftwards from x to 0 so distance = x-0 = x
            else:
                acc_R += 1
                max_right_time = max(max_right_time, L-x) # ant travels rightwards from x to L so distance = L-x
            
            ants.append((x, direction))

        ants = sorted(ants)

        max_time = max(max_left_time, max_right_time)
        res = f"The last ant will fall down in {max_time} seconds - started at "
        
        # check the 3 cases
        if max_left_time > max_right_time:
            # find the acc_L'th ant -> in INDEX acc_L-1 in the sorted ants list:
            res += f"{ants[acc_L - 1][0]}."
        elif max_right_time > max_left_time:
            # find the -acc_R'th ant ==> same as acc_L+1th ant, which is in INDEX acc_L+1-1 = acc_L O_o
            res += f"{ants[acc_L + 1 - 1][0]}."
        else:
            # both the ants 'd' and 'e' abcd|efghij  fall off at same time
            res += f"{ants[acc_L - 1][0]} and {ants[acc_L + 1 - 1][0]}."

        print(res)

    except:
        break
```