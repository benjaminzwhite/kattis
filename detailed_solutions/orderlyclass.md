# Detailed solution for Kattis - Orderly Class

[Problem statement on Kattis](https://open.kattis.com/problems/orderlyclass)

This looks like a combinatorics exercise but it is in fact simpler - also the problem statement is a bit confusing, so it might help to clarify it here.

## Tags

array

## Solution

As mentioned, I thought it was really hard to parse explanation since it introduces `a_i` and `b_i` but it's not clear what they are. Here is a very straightforward reformulation instead:

"You have a string `s` and a string `t`; can you obtain `t` from `s` by selecting a **single, contiguous**, substring of `s`, and flipping it? If so, how many ways are there to do this?"

Examples:

```
s = abcJKLxyz
t = abcLKJxyz  -> yes, flip the substring JKL to get LKJ

s = abcJKLccc
t = abcLKJccc  -> yes, flip the substring JKL to get LKJ. But, now, can also flip cJKLc, to get cLKJc
```

The reasoning is as follows: Since **there is only one flip allowed**, the only way 2 chars can differ between `s` and `t` is **if they are part of the flipped segment**.

So iterate left to right along `s` and `t`: look for first `mismatch_left_index` `l` (in example above this would be `s[l=3]` pointing to char J and `t[l=3]` pointing to char L).

Then, same argument as above, right to left along `s` and `t` for first `mismatch_right_index` `r` (above this would be `r=5`).

Check whether `s[l:r+1] == t[l:r+1]` **reversed** (i.e. in case of `s = aaaaWXYZaa` and `t = aaaaWOOZaa` your `l,r` will book-end the correct candidate substring `s[4:8]` and `t[4:8]` but `WXYZ != WOOZ[::-1]` so this situation is **impossible** to obtain with one exchanage).

If so, at this stage, there is currently `1` way to do the single flip.

Now, **you can possibly expand the number of ways**, i.e. in example above going from "JKL" to "cJKLc" **only if the** "surrounding chars" on either side are identical; as if so they are not affected/satisfy the flipping operation also "for free":

Example:

- With `s = abcdJKLdczz`, `t = abcdLKJdczz` you find the core string JKL <-> LKJ, **ok** it is flippable at that size.
- Then you try +/- 1 either side: dJKLd <-> dLKJd OK, then try +/-2: cdJKLdc <-> cdLKJdc OK
- But when you try +/- 3 either side: bcdJKLdcz <-IS NOT-> bcdLKJdcz since b does not match z on either side

## AC code

```python
s = input()
t = input()

l, r = 0, len(s) - 1
while l < len(s):
    if s[l] == t[l]:
        l += 1
    else:
        break
while r >= 0:
    if s[r] == t[r]:
        r -= 1
    else:
        break

if l <= r:
    segment = s[l:r+1]
    if segment[::-1] == t[l:r+1]:
        pair_cnt = 0
        l -= 1
        r += 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            pair_cnt += 1
        res = 1 + pair_cnt # CARE: +1 because you have the original_segment itself in the worst case as 1 option, even if no surrounding pairs

print(res)
```
