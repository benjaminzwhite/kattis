# Detailed solution for Kattis - Stacking Up

[Problem statement on Kattis](https://open.kattis.com/problems/stackingup)

A cool exercise: I think the initial solution approach is quite easy to get, but the implementation is tricky and makes it worth changing perspective to get an easier solution approach.

## Tags

array, logic, interpreter

## Solution

If you think about working from left to right e.g.

`[3, 4, 11, 5]`

then you realise quickly that, if you try to make exactly the first value, 3, then when you try to make 4 the process for 4 will involve some number of + operations, which by the problem statement, causes **all previous numbers on the stack to -= 1**.

So in other words, the "real" value of 3 that you should aim to make should reflect the number of + operations that will take place in the future, **after** it has been processed itself.

So you quickly get the idea to work through the list `[3, 4, 11, 5]` **backwards:** you can accumulate the number of + operations that you use for each value 5 then 5+11 then 5+11+4, so that you know the "extra" needed to add to 3 so that it reflects the -1's **ahead of it**.

My first implementation of this idea was a bit clumsy:

I was trying to make up the individual values e.g. `5, 11, 4, 3` (reversed order compared to input) with some complex steps which could involve having, for each value, a "mini-stack" with more than 2 elements on it at any given time. This would lead to e.g. trying to make 11 itself as something like `[4,4,4] -> [3] 4+4 = 8 -> [3,8] => 3+8 = 11`, and I was trying to implement this with really complex accounting, since with this approach *you also need to track, within the ministack* how many + operations you perform for '11' itself. For example in the case above `[4,4,4]` will lead to `[3,8]` due to one + operation to get 4+4 so thats why the ministack for 11 is `[4,4,4]` not `[3,4,4]` -> sum == 11.

I stepped back and resolved in a cleaner way, based on the same fundamental idea though:

**The simplification is that:** if you just make up the individual values 5,11,4,3 the *obvious way* like the "binary log/matrix exponent multiplication" style i.e. you repeatedly divide by 2 if x is even or substract 1 if x is odd, **then you will never have a mini-stack with more than 2 elements on it, so you will never have to account for + operations on the ministack for any single individual value**.

This is the key simplification; it means you can handle individual x values in a self-contained way, and track the accumlated + operations and update it **between** x values (rather than while doing the current x value, which is very complicated to track O_o)

So for example if x = 11 you do `11 -> -1 = 10 -> //2 = 5 -> -1 = 4 -> //2 = 2 -> //2 = 1`.

This corresponds *in reverse* to doing the operations:

```
add 1: 1 --> stk == [1]
duplicate, then add: 1d+ --> stk == [1,1], --> [] 1+1+2 --> [2]  <=== note how there are no "leftover" items on stack to -1 adjust
duplicate then add: 1d+d+ --> [2] --> [2,2] --> [] 4 --> [4]     <=== no leftover on stack when you +
add 1 then add: 1d+d+1+ --> [4] --> [4,1] --> [5]
etc.
```

So that's what makes the huge difference in implementation of the same basic good idea - now you can just focus on tracking the `accumulated_plus_operations` and for subsequent x values, you use that to "correct" the value of `x -> x_ = x + acc_plus_ops` to account for the number of plus operations needed for all later values in the list.

### Implementation notes

It's easy to get lost: you build each `x_` **down** from `x_` to `1` using the "binary log/matrix exponent multiplication" process, then this corresponds to the operations you need to perform **in reverse** to build **up** from `1` to `x_`.

Finally, the final `res` string is obtained from joining all individual `x_` strings, **taken in reverse order** (the **elements**, don't reverse the processed strings anymore, they are good at this point!)

### Debug code for checking solutions

Here's a quick debug/checker to make sure the res strings matches the input.

```python
def check(s):
    stk = []
    for c in s:
        if c == '1':
            stk.append(1)
        elif c == 'd':
            stk.append(stk[-1])
        elif c == '+':
            tmp = stk[-1] + stk[-2]
            
            stk = [x - 1 for x in stk[:-2]]

            # not sure this ever is needed in my solution approach:
            # always end up having x_ >= x at all stages so no 0's on stack?
            stk = [x for x in stk if x != 0]
            
            stk.append(tmp)
        else:
            continue
    return stk
```

## AC code

```python
n = int(input())

xs = list(map(int, input().split()))

ops = []
acc_plus_ops = 0 # how many times have we needed to perform + operation prior to this current x value
for x in xs[::-1]:
    x_ = x + acc_plus_ops
    curr_ops = []
    
    # do the "binary log/matrix power" type decomposition of x_:
    while x_ != 1:
        if x_ % 2 == 1:
            curr_ops.append("1+")
            acc_plus_ops += 1
            x_ -= 1
        else:
            curr_ops.append("d+")
            acc_plus_ops += 1
            x_ //= 2
    
    # now x_ == 1: so "end" the process with the '1'
    # (since we are working backwards this INITIALIZES the st process)
    curr_ops.append('1')
    
    ops.append(curr_ops[::-1]) # CARE! Remember to reverse the curr_ops!

# remember to REVERSE THE ORDER in which you produce the string, since we produced the tokens right to left
#             -----------------------VVVVVV--------------------
res = ''.join(''.join(x) for x in ops[::-1])

print(res)
```