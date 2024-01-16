# Detailed solution for Kattis - Johnny Applesack

[Problem statement on Kattis](https://open.kattis.com/problems/applesack)

This is an original greedy-algorithm problem that was good practice for reasoning about why a greedy approach works.

## Tags

logic, greedy

## Solution

- If you have `n <= k` apples then the best you can do is walk forwards with `1` (partially or fully) full bag and pay `1` per unit distance, so you can travel a total of `n` steps
- If you have **more** than `k` apples, you have a 2nd option: try to move some number of apples to some intermediate distance then perform option 1
(I recommend you draw example with e.g. `13` apples and bag size `5` - for each distance `0,1,2,3,4...` plot the total amount of apples you could bring to that location)

How to study this option 2? Well, to get any number of apples to some distance `d`, you first have to get them all to distance `1` so the analysis 
of option 2 reduces to studying how to move a pile of apples `1` single distance - for any other intermediate distance and any intermediate number of apples above, you will be bottlenecked by moving all apples from initial pile to a pile at distance `+1` in any case.

Now:

- It will require `ceil(n/k)` trips to move all the apples from `d=0` to `d=1`; each trip costs `1` apple cost, so total cost is `ceil(n/k)` apples.
- **This is the key greedy observation step:** you are now in a new initial condition with `n_new = n - ceil(n/k)` apples and you have gained +1 total distance. **If `n_new >= k` then you have made a good choice since option 1 is still available (you can fill a k-sack) but now you will be able to perform it with +1 total distance already baseline.**
- So keep performing option 2 until you first have `n_new <= k` apples then walk the rest of the distance with your last k-sack filled with `n_new` apples.

### Implementation notes

After implementing this logic I noticed I was off-by-one with the given testcase - it requires some reading comprehension to understand why:

"Help Johnny figure out how many kilometers he can travel" is what is written in statement, but it's actually asking you **"at which barrier do you get STOPPED"** essentially, so the idea is you DO walk the +1 final distance only to get stopped at the barrier there where you first run out of apples.

So for example the `n = 0` apples case would mean you can actually travel *1* rather than 0 distance, since you first encounter a tollbooth AFTER 1 distance travelled.


## AC code

```python
from math import ceil

n, k = map(int, input().split())

distance = 0
while n > k:
    n -= ceil(n / k) # greedily perform option 2
    distance += 1

distance += n # perform option 1 with leftover apples

# See implementation notes, need to +1 to get number of first toolbooth you encounter where you will run out of apples.
distance += 1

print(distance)
```