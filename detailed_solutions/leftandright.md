# Detailed solution for Kattis - Left and Right

[Problem statement on Kattis](https://open.kattis.com/problems/leftandright)

This is an elegant logic reasoning/algorithmic puzzle.

## Tags

logic

## Solution

Every time you see an `R` you want a number that is guaranteed to be to the "left of" i.e. **smaller than next one**, so if you always print the lowest "unused number" (see below for explanation of this) you will satisfy this requirement **and this will satisfy the overall requirement of string being the lexicographically smallest** (because you will always have the smallest valid candidate earlier than any other possible candidates).

Every time you see an `L` you want a number that is guaranteed to be to the "right of" i.e. **larger than next one**. Now, however, if you always print the **largest** "unused number", you will get a valid answer **but you are not guaranteed to get the lexicographically earliest overall result.**

```
R L L R L
1 6 5 3 4 2
```

For example, with the above illustrated testcase you are "using up 6" too soon, since the current descent of which 6 is the first element only has 3 elements (here 6,5,3) and could have been achieved instead with `4,3,2` where `4,3,2 < 6,5,3` lexicographically.

So you need to "lookahead" with the `L` chars, until you encounter another `R`, and determine what the length of this "descent substring" is (in the above example, the first descent substring just after `1` : `1 _ _ _ ....` is identified by the sequence `LLR` and will be of length 3 and needs to go in the `_ _ _`)

Once you know this length, X, then you find the X (`X = 3` in the example above) smallest available numbers and then append them **IN REVERSED ORDER** to get the lexicographically smallest available valid candidate that fits.

### Implementation notes

Based on the notes above, the entire logic in the code below is involved in keeping track of which numbers have been used (you can do this just by tracking the smallest available number at all times) and what the length of the current descent substring is, then updating these values correctly as the sequence is processed.

Also, useful trick: I append a dummy `R` char to the end of the input which will trigger the processing of the last "real" range in the input.


## AC code

```python
n = int(input())
s = input()
s += 'R' # IMPLEMENTATION: dummy R will trigger the last ("real") range processing, then stop.

res = []
smallest_avail, curr_descent_size = 1, 0
for c in s:
    if c == 'L':
        curr_descent_size += 1
    else:
        tmp = list(range(smallest_avail + curr_descent_size, smallest_avail - 1, -1)) # CARE! note range is REVERSED: i.e. want [4,3,2] not [2,3,4]
        res.extend(tmp) 
        smallest_avail += curr_descent_size + 1
        curr_descent_size = 0

for x in res:
    print(x)
```