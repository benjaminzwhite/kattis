# Detailed solution for Kattis - Abandoned Animal

[Problem statement on Kattis](https://open.kattis.com/problems/abandonedanimal)

Really cool idea for an exercise. Also good practice for "solve the easiest relevant example" problem solving pattern: basically when you deliberately choose the simplest/most accessible answer that will get the job done.

## Tags

array, logic

## Solution

The starting observation is that, if the buying pattern can be done, **it must be able to be done greedily** i.e. if you buy as many items on the chronological list in the current shop, **you never decrease your chances of completing the list later** (you go into the next shop with fewer or equal number of the **same** remaining items to match as if you had chosen a non-greedy strategy).

Now, you aren't asked *how many ways you can do it*, so once you have checked that greedy works, all you need to do is find 1 other possible buying strategy, to bring total to at least 2, and this means that the item list is "ambiguous" i.e. there are more than 1 possible ways to achieve the item list.

I was trying to actually count the detailed number of paths/solutions through the shops, but while making the greedy function I realised you can reuse it: there is **always** 1 particular solution that, if it also exists, is very easy to determine: it is the strategy where you buy each item **at the last available shop**, whatever that may be, such that the entire solution is complete.

**This strategy is easy to implement**: it is obtained by a simple "time reversal" of the items and stores, and solving this new case greedily.

So, to clarify, first try to solve greedily: obtain the list of stores at which the greedy solution buys each item.

1. if this list has fewer entries than the number of items, then greedy solution does not work hence **no solution will work either**
2. if this list has same number of entries than number of items e.g. `[0,0,1,3,8]` means we bought all 5 items in stores `0,0,1,3,8` then greedy solution works so we continue to next step
3. perform the time reversal: try buy the "last to first item" at the "latest to earliest possible" stores.

If the solution produced by 3 is **same** as 2 then this means **all possible solutions** (which would involve buying at intermediate stores and delaying the greedy strategy, *in some complicated way that we don't care about !!*) will end up producing the same final store order, so the solution is **unique**.

But if the solution 3 is **different** to 2, then we have found that there are (at least) two different ways of solving the item list, so the problem is **ambiguous**.


### Implementation note

I forgot that, when calling `greedy()` backwards/time reversed, the "stores" that it sees have the "opposite" index to the ones recorded by forward `greedy()` i.e. if forward adds first store it is stored as `i_s = 0` but if backwards greedy adds "first store" as `i_s = 0`, **this is actually the last store in the forward list** !!

Bizarrely, the first few testcases pass with this error.

To fix: instead of checking `forward == backwards` as lists, just zip over the 2 lists, and check if the `f` in forward is equal to `N-1-b` for the `b` in backwards (this corresponds to e.g. store `0` in forward out of `N=4` stores being store `N-1-0 = store 3` in backwards list).

## AC code

```python
N = int(input())

K = int(input())

stores = [set() for _ in range(N)]
for _ in range(K):
    i, s = input().split()
    stores[int(i)].add(s)

M = int(input())

items = []
for _ in range(M):
    items.append(input())

def greedy(storelist, itemlist):
    S_MAX = len(storelist)
    I_MAX = len(itemlist)
    i_s, i_i = 0, 0
    res = []
    while i_s < S_MAX and i_i < I_MAX:
        while i_i < I_MAX:
            if itemlist[i_i] in storelist[i_s]:
                res.append(i_s)
                i_i += 1
            else:
                i_s += 1
                break
    return res

# Step 1 - try the greedy approach
forward = greedy(stores, items)
if len(forward) != M:
    print("impossible")
else:
    # Step 2 - try the backward/time reversed greedy approach
    backward = greedy(stores[::-1], items[::-1])
    # Step 3 - check the equality as described in notes
    # Update - see Implementation comment:
    # need to remember that the indices in backward are "N-1-i" w.r.t to forward stores list
    if all(f == N - b - 1 for f, b in zip(forward, backward[::-1])):
        print("unique")
    else:
        print("ambiguous")
```