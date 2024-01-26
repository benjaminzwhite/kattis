# Detailed solution for Kattis - The Paladin

[Problem statement on Kattis](https://open.kattis.com/problems/thepaladin)

This is a nice dynamic programming exercise with some tricky edge cases to consider; it is also good practice for implementation.

## Tags

dynamic programming

## Solution

The solution for odd length is quite easy to notice: it's always to just greedily repeat the lowest "double pairing" of e.g. `ab + ba` i.e. the pairing with lowest **total `ab + ba` cost.**

The result then is to repeat it `ababab|MIDDLE_ODD_CHAR|bababa` and the total cost is `k//2 * (total_pairing_cost)` e.g. here there are 3x `ab`'s and 3x corresponding `ba`'s symmetrically on the other side of the palindrome.

---

While implementing this simple solution, I realised why the exercise is rated higher: for **even** length **you cannot always do this simply strategy
because you must always have a "central pairing" like `ababa|CC|ababa` WHICH MUST BE SYMMETRIC/INVOLVE A REPEATED CHAR.**

Now, you can't just greedily find the "first half" `ababa` and then decide to add its cost to the lowest cost `CC` either, because you need to satisfy a "matching condition": for example, if you just locally choose `ababa` and locally choose `CC`, then you will end up with the 2 rune pairs at the boundaries: `aC` and `Ca`, **and these 2 rune pairs need to be valid options also for your solution to actually be possible.**

So first I tried modifying the easy greedy approach, for odd lengths, to also work with even lengths by working outwards - I wanted to scan for all paired chars `CC`, then work outwards, like `aCCa, bCCb, xCCx, ...` depending on whether `(aC, Ca)` exists etc. but this ended up being complicated so I restarted and solved the odd and even lengths cases together with dynamic programming.

### Dynamic programming notes

The `dp` state is `dp[snd_position_in_palindrome][snd_char_option]`, where `snd_position` ranges over `idx = 1,2.... LAST_INDEX`.

The `LAST_INDEX` is (since we are only processing **half** of the palindrome, due to symmetry) `k//2 - 1 + maybe a 1 or not` depending on odd/even and inclusive/exclusive range (careful with this! It's a potential off-by-one tripping point - see comments in the AC code below).

You are trying to place each rune pair, conditioning on the `snd_char` occuring in idx `1,2,3...`.

You will try all `fst_char` and `snd_char` options `(a,b,c..)`, then lookup whether a pair `(fst, snd)` is indeed a valid rune char pair, and if so update the `dp` cost accordingly.

The result is the min total cost having reached the `LAST_INDEX`, but there are still also some additional little Implementation details and edge cases to think about.

### Implementation notes

The dp is "half" (rounding down depending on odd/even total length) the size of the input `k` by symmetry of the palindrome, so need to make sure we consider the **total cost** we are computing at each index, i.e. we need to also include the cost of the "symmetric" pair: `total cost = (a,b) + (b,a)` **where we note these 2 pairs' ab/ba costs may NOT be the same.**

For the first pair, i.e. `fst_position == 0, snd_position == 1` you **DO NOT** add the dp cost: just initialize dp by trying all valid pairs `(fst, snd)` as the first pair in the growing palindrome.

Also (see notes above on even vs odd case): after you have calculated all possible dp options, you need to - for the **EVEN `k` CASE only** - "rule out" all options that cannot be achieved in practice due to it requiring a middle pair with repeated char: i.e. you need to check for each dp option whose last char before the middle-symmetry line is `'a','b','c',...'z'` **that there is indeed the pair `('a','a'), ('b','b'),...` as an option.**`

For example; if best res up to this step is `abc|d` but `(d, d)` does not exist, then `abc|dd|cba` is **not** in fact a valid option, so `dp["abcd"]` goes back up to `INF` and the next best option, say `xch|g` might be now the best "actually achievable" option if `(g, g)` exists etc. etc.

For the rune pair lookup, below I encode the `(fst, snd)` costs in a 26x26 `fst_x_snd` array by encoding each char in `'abcd....xyz'` as `0,1,2...25` by taking `ord(c) - 97`.

Finally, with my approach I need to handle the `k = 2` case separately. See the code below with comments to explain why.

## AC code

```python
n, k = map(int, input().split())

# lookup array for the rune pair costs
fst_x_snd = [[float('inf')] * 26 for _ in range(26)]
for _ in range(n):
    fst_snd, cost = input().split()
    fst = ord(fst_snd[0]) - 97 # a = 0
    snd = ord(fst_snd[1]) - 97
    fst_x_snd[fst][snd] = int(cost)

dp = [[float('inf')] * 26 for _ in range(k+5)] # k+5 is sentinel value

# See notes: LAST_INDEX and potential for off-by-one errors:
# This is the LAST_INDEX (*INCLUSIVE*) UP TO WHICH WE TRY TO PLACE THE snd_char
# e.g. in abc|dd|cba <- EVEN k=8, LAST_INDEX = 4 - 1 + (0) = 3, and indeed we will try to place snd_char in idx 1,2,3 but not 4.
# e.g. in xyz|m|zyx  <- ODD k=7, LAST_INDEX = 3 - 1 + (1) = 3, and indeed we try to place snd_char in idx 1,2,3 but not 4.
LAST_INDEX = k // 2 - 1 + (k % 2 == 1) 

for snd_position_in_palindrome in range(1, LAST_INDEX + 1):
    for fst_char_option in range(26):
        for snd_char_option in range(26):
            # try insert all pairs  (fst_char, snd_char) so that snd_char is in snd_position_in_palindrome
            extend_prev_palindrome = fst_x_snd[fst_char_option][snd_char_option] + fst_x_snd[snd_char_option][fst_char_option]
            
            # if this snd_position is ANYTHING OTHER THAN THE FIRST PAIR WE ARE PLACING e.g. if position > 1
            # then we need to add the dp cost of the growing palindrome to this position also, that ENDS WITH the fst_char
            if snd_position_in_palindrome > 1:
                extend_prev_palindrome += dp[snd_position_in_palindrome-1][fst_char_option]
            
            dp[snd_position_in_palindrome][snd_char_option] = min(dp[snd_position_in_palindrome][snd_char_option], extend_prev_palindrome)

# See notes: FOR EVEN STRINGS, YOU MUST MODIFY DP OPTIONS SO THAT THEY MUST HAVE A CENTRAL DOUBLE PAIR
# I do this by adding, to each dp cost ending with snd_char, the cost of the double pair (snd_char, snd_char)
# This cost will be INF (in the fst_x_snd array) if the pair doesn't exist, so this step will assign dp = INF to any results which
# cannot be made to "end-in-the-middle" with any double char pair
# e.g. if best result up to this step is abc|d but (d, d) does not exist, then abc|dd|cba is NOT in fact a valid option, so goes back up to INF
if k % 2 == 0:
    for snd_char_option in range(26):
        dp[LAST_INDEX][snd_char_option] += fst_x_snd[snd_char_option][snd_char_option]

# The result is the min total cost having reached the LAST_INDEX
res = min(dp[LAST_INDEX])

# UPDATE: noticed while testing my solution before submitting:
# My approach doesn't handle the case where k=2
# --> Just need to look for min cost of all (char, char) pairs in this case
if k == 2:
    for snd_char_option in range(26):
        res = min(res, fst_x_snd[snd_char_option][snd_char_option]) # i.e. check min cost among: ('a','a'), ('b','b'), ...., ('z','z')

# CARE! make sure to print -1 if res is INF, corresponds to no valid solution after the dp calculation
print(res if res < float('inf') else -1)
```