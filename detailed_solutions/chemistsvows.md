# Detailed solution for Kattis - Chemist's Vows

[Problem statement on Kattis](https://open.kattis.com/problems/chemistsvows)

This is a fairly straightforward dynamic programming exercise, but the idea is cute - also you can make your own "extra homework" by finding an efficient way to scrape the needed chemical symbols!

## Tags

dynamic programming

## Solution

My first solution was to implement recursive function but I hit the Python recursion limit for large inputs.

Here is the recursive function for clarity, and for comparing with the bottom-up implementation:

```
from functools import lru_cache

def solve(s):
    @lru_cache(maxsize=None)
    def rec(i):
        if i >= len(s):
            return True
        
        one_b = s[i:i+1] in REF
        two_b = s[i:i+2] in REF

        if not (one_b or two_b):
            return False

        one = rec(i+1)
        two = rec(i+2)

        return (one_b and one) or (two_b and two)   
    
    return rec(0)
```

So the AC code is just the bottom-up implementation of the above logic.

## AC code

```python
REF = {'cr', 'xe', 'c', 'br', 'h', 'ta', 'lr', 'at', 'o', 'sc', 'si', 'li', 'ds', 'la', 'zr', 'se', 'rg', 'po', 's', 'mo', 're', 'lu', 'es', 'os', 'cn', 'np', 'nb', 'am', 'tm', 'w', 'pb', 'cm', 'rf', 'no', 'mt', 'na', 'pr', 'n', 'rh', 'ba', 'pt', 'au', 'sg', 'p', 'ac', 'cd', 'f', 'sm', 'k', 'cu', 'cf', 'ga', 'ra', 'ge', 'ir', 'yb', 'co', 'v', 'kr', 'ce', 'ne', 'te', 'ag', 'mg', 'pd', 'db', 'zn', 'md', 'u', 'in', 'th', 'ar', 'cs', 'fm', 'tb', 'tl', 'pa', 'ti', 'er', 'mn', 'cl', 'bh', 'be', 'rn', 'hs', 'sn', 'nd', 'bk', 'b', 'fr', 'gd', 'hf', 'bi', 'ru', 'fe', 'i', 'fl', 'ni', 'pu', 'rb', 'he', 'al', 'lv', 'dy', 'hg', 'sr', 'as', 'y', 'ho', 'sb', 'eu', 'tc', 'pm', 'ca'}

T = int(input())
for _ in range(T):
    s = input()
    
    dp = [False] * (len(s) + 10) # sentinel value
    dp[0] = s[0] in REF
    
    if len(s)>1:
        dp[1] = dp[0] and s[1] in REF or s[:2] in REF

    for i in range(2, len(s)):
        if dp[i - 1] and s[i] in REF:
            dp[i] = True
        if dp[i - 2] and s[i - 1:i + 1] in REF: # CARE! make sure you are looking BEHIND AT PREVIOUSLY COMPUTED dp VALUES FOR i' < i
            dp[i] = True

    if dp[len(s) - 1]: # can you make it to the last char in the string
        print("YES")
    else:
        print("NO")
```
