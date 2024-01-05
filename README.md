# Kattis

Solutions to Kattis competitive programming exercises, mainly in Python 3. 

I also write detailed solution pages for particularly interesting exercises that I solve (see list with links in below section).

Many of the non-trivial exercises have a `NOTES` comment in source file with thought process/reasoning/observations.

PM me with any comments or questions.

## General notation

I try to keep same variable names as used in the Kattis problem statement, unless they are really confusing.

Otherwise I try to stick to the following notation when solving exercises:
<details>
<summary>Click to expand general notation for variables</summary>

```
s : a string
c : a single character
d : a dictionary/hashmap
res : whatever the final result is
inps : if inputs require some kind of processing
curr,prev,best : when doing some kind of updating of current vs. previous vs. overall best values
cnt : when counting something
seen : when storing some kind of lookup of previously seen values, visited nodes in a graph, etc.
flg : a flag boolean for exiting loops or tracking if conditions are met
t,T,tc,TC : testcases
q,Q : queries
x,xs : generic names for moving through an iterable
r,c,R,C,dr,dc : current row/column, number of rows/columns in a grid, change in row/column
moves : allowed moves in some kind of grid or maze, e.g. [(-1,0), (0,1)]
board,grid : state of some kind of input maze/game board/grid configuration
acc : accumulator/range sum
dp : dynamic programming array
goods,bads : for combinatorics exercises when counting good/bad objects or states
stk : a stack
q,pq : queue, priority queue of some kind
ss,mm,hh : when working with dates and times
hi,lo,mid : when binary searching
PRECOMPUTE,LOOKUP,REF : in exercises with multiple queries of a precomputed answer
```
</details>

## Exercises with detailed solution pages

Exercises which I found particularly interesting for some reason, and decided to write-up a solution page:

- [Lucky Draw - kattis: luckydraw](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/luckydraw.md)

<details>
<summary>Exercises to write-up</summary>
  
- Ocean Monument
- Lopsided Lineup
- Swap Space
- Exits in Excess
- Srednji
- Factorial Power
- Wolf
- ETA
- Ada Loveslaces
- Sequential Manufacturing
- Please, Go First
- Accounting aka Bokforing
- Distance
- Dams in Distress
- Farey Sums
  
</details>
