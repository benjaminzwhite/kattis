# Detailed solution for Kattis - Envious Exponents

[Problem statement on Kattis](https://open.kattis.com/problems/enviousexponents)

Nice exercise, you need to think a bit about the binary representation of the numbers - it helps to solve via a "brute force" approach first, then notice some patterns.

## Tags

binary

## Solution

### Initial solution experimentation

Imagine starting at `N` and incrementing `N` by 1, and for each `N'` count how many set bits, until you reach first with set bits = `k`. This will surely give you the smallest `N' > N` that satisfies the k-set-bits requirement.

However can't do it manually of course for large numbers i.e. can't try +1, +2, +3,... when `N = 10**18`

So experimentally tried doing this and recorded what happens e.g. with `N = 50` and `k = 2`:

```
bin(N) = 110010  <- note N has b=3 set bits/bitcount

N+1, N+2... below:

50 = 110010  3 N=50 SO START AT N+1 AS FIRST POSSIBLE CANDIDATE:
51 = 110011  4
52 = 110100  3
53 = 110101  4   
54 = 110110  4   
55 = 110111  5   
56 = 111000  3
```

Observations: Here we have that `target_k` is `< b=3` bits in the original `N=50`.
- The only wat we can get the bit count in `N` to decrease relative to `n` is wen we can finally toggle the least significant set `1`
- You can see this above, as bitcount falls from `51` to `52` as we go from `110011` to `110100` and from `110111` to `111000`

(note that these 2 examples are not representative: in general you can have trailing **unset** `0`s also: `100011000 -> 100100000` is the first way to decrement bitcount, and here we have trailing `0`'s in initial `N`)

I implemented the above using strings/arrays:

1. Move from "right to left" of string (LSB to MSB) and when you start encountering `1`'s:
2. ...while you keep encountering `1`'s ...., keep moving left
3. Finally encounter a `0` (unset bit) -> toggle to `1`, and flip all the `1`'s you just saw to `0`

### Better implementation discovery

While implementing this and studying output, I realised that all I am doing in the end is *adding* the *value* corresponding to the least significant set bit: that is what addition is actually doing in binary, it automatically handles the carrying behavior I was implementing in strings e.g.:

Consider `142 = 10001110`; my string approach moving right to left sees `0` then `1`, set `"in_block_of_1s_Flag"=True`, keep looking for `1`'s : `0,1,1,1,0`, *STOP* -> replace with `00001`, and end up with string `{100} + [10000]` where here we have symbolically `{the unchanged part}`, and `[the changed part]`.

Now do the same but with the **insight that this is just addition of the least significant set bit**:

`142 = 10001110`; LSSB is "2" ie `2**1` i.e. 1th bit -> so take `N' = N + 2 = 144` -> `144` in binary is `10010000`, same result as above.

**Important:** everything above is for when you want to reduce the bitcount of a given `n` to a *smaller value* `k`: this will reduce the bitcount of `n` in the optimal way, but now you might over shoot so, in general you need a 2nd greedy algorithm that works
for when `k` is `>` than the bitcount of the current number.

So for example if `N=50` and `k=5`, what is the approach?

**This is much easier**; you just flip  `k - bitcount(N)` `0` bits to `1` from LSB to MSB; this ensures the resulting number is as small as possible:

e.g. if `N` originally has 3 set bits, how will the above approach produce the smallest number with 5 > 3 set bits:

```
N=50 110010 3 SET BITS 
N=51 110011 4 SET BITS
N=55 110111 5 SET BITS <-- smallest N' > N with 5 set bits
```

For this 2nd algorithm therefore, I also implemented with a string-based approach (easier that the first one): basically have a `"bits_to_flip = k - bit_count(original_n)"` total, and moving right to left, flip each `0` that you encounter and decremement the remaining `"bits_to_flip"` by 1

### Final notes for implementation

- Remember Kattis Python 3.8 has no built-in `bitcount` (need 3.10).

Spent a bit of time with bit twiddling resources to find out ways to avoid using the string based approaches (for the 2 steps described above):

#### Part 1: `bit_count` is `> k`:

You want to find the *rightmost set bit* i.e. the rightmost 1 in the "string", then **add this value** to `n` (see discussion example with `142 + 2 = 144` above)

bitwise: `n & ~(n-1)` finds rightmost set bit, so will add this to `n` to produce the `10001110 -> 10010000` behavior.

- Note this might *undershoot* so you need the Part 2 greedy correction step below.

#### Part 2: `bit_count` is `< k`:

You want to find the *rightmost unset bit* i.e. the rightmost 0 in the "string" and toggle it to 1:

bitwise: the usual way to do this is to set `n = n | (n+1)`

e.g. if `n = 9 == 1001` then  `n | (n+1) = 11 = 1011`, if `n = 10 == 1010` then `n|(n+1) = 11 = 1011`, etc.

**Note:** edge case; I checked that this works for when there are "no rightmost 0's" i.e. `n = 15 = 1111`

```
test_n = 15
print(bin(test_n)[2:])
res = test_n|(test_n+1)
print(bin(res)[2:]) <--- produces 11111 as expected OK 
```

## AC code

```python
n, k = map(int, input().split())

n += 1 # !!! important: we want N' > STRICTLY GREATER than N (You will fail testcases e.g. input 12,2 produces 12 if you allow N' >= N instead of N' > N)

# no Python 3.10 so DIY n.bit_count()
while (DIY_n_bit_count := bin(n).count('1')) != k:
    if DIY_n_bit_count > k:
        # SEE Part 1 NOTES: bitwise find rightmost set bit, and add this value to n
        # see notes: this is e.g.
        # N = 142 = 10001110
        #                 ^____ want to add 2**1 = 2 since this is rightmost set '1' bit: which you get from N & ~(N-1)
        # N' = 142+2 = 144 = 10010000
        val_of_rightmost_set_bit = (n & ~(n - 1))
        n += val_of_rightmost_set_bit
    else:
        # SEE Part 2 NOTES: bitwise set rightmost unset bit to 1
        n = (n | (n + 1))

print(n)
```