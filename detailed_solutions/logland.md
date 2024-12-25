# Detailed solution for Kattis - Logland

[Problem statement on Kattis](https://open.kattis.com/problems/logland)

Mainly a logic/binary reasoning exercise - it reminded me a bit of combinatorics "stars and bars" counting techniques, where you create "fake objects" to make the exercise easier to work with.

## Tags

binary, logic, proof

## Solution

I found it clear if you think about **gluing 2 real coins to form 1 "fake" coin of a higher denomination**.

1. Start with lowest (WLOG say 1's 2's 4's... are all available > 0, doesn't change anything)

2. If the number of lowest coins is **odd** then you can never make up the odd coin leftover (since there are no smaller denominations, we are at lowest). Therefore, add `1 * 2**lowest_exponent` i.e. `1 * lowest_coin`

3. If the number of lowest coins is `> 0` though, and once you have "removed" the odd coin, you have an **even** number leftover:

Say WLOG you have seven `1's` -> remove the odd `1`, and have 6 leftover.

- glue these `1's` together to form fake `2's` -> with 6 `1's` you can form up to 3 fake `2's` if needed for **later on in the process**.

- treat these fake `2's` as real `2's` so imagine bringing them to the next bigger "bank vault" (or w/e it is) e.g. if looking ahead there are `35` real `2's`, well without any "glued" ones, you would have to leave 1 of the `2's` behind to get `35 - 1 = 34` and then divided `34 // 2`; but, since you do have at least one glued fake 2, you can imagine bringing that with you and adding it to the pile to make `35 + 1 = 36` and fairly dividing `36 // 2`

Observation 1: **note that** this is only relevant if: the number of **real coins** is odd, and you have **at least one `"previous_size"` glued coin** e.g. `35` real `2's` and `>0` "1+1 = fake 2" allows you to create an even number, `36`, of `2's`.

Note also: you aren't "spending" any of these coins as you go from 1,2,4... so all that matters is the total amount of glued coins that you could in principle bring to each larger denomination.

Observation 2: **note that you are constantly "halving" the value of accumulated previous glued coins as you move to larger amounts**:

i.e. after step #2 above, you have `3` fake `2's` (formed from `6` real `1's`) and now you have `35` real `2's` to play with: so, you add both these piles together, to form `3+35 = 38` `2's`, and glue them pairwise, giving you `38 // 2 = 19` "glued 4's" for the next bank etc.


## AC code

```python
BIGMOD = 10**9 + 7

N = int(input())
xs = list(map(int, input().split()))

res = 0
glued_coins = 0
for exp, real_coins in enumerate(xs):
    if (real_coins % 2 == 1) and (glued_coins == 0): # see Observation 1 above, you don't have at least one glued coin to add to the ODD PILE of real_coins to allow fair division by 2
        res += pow(2, exp, BIGMOD) # exponents go up to exp = 2**30 so need to take modular power
    glued_coins = (glued_coins + real_coins) // 2 # see Observation 2 above, your N=glued_coins of value 2**exp now are merged with M real_coins of value 2**exp, to form (N+M)//2 "new glued coins" of value 2**(exp+1) ready for the next larger bank vault

print(res % BIGMOD)
```
