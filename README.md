# Kattis

Solutions to Kattis competitive programming exercises, mainly in Python 3. 

I also write [detailed solution pages for particularly interesting exercises](#exercises-with-detailed-solution-pages) that I solve (see list with links in below section).

Many of the non-trivial exercises have a `NOTES` comment in source file with thought process/reasoning/observations.

Email me with any comments or questions.

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
- [Swap Space - kattis: swapspace](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/swapspace.md)
- [Sequential Manufacturing - kattis: sequentialmanufacturing](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/sequentialmanufacturing.md)
- [Exits in Excess - kattis: exitsinexcess](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/exitsinexcess.md)
- [Please, Go First - kattis: pleasegofirst](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/pleasegofirst.md)
- [Farey Sums - kattis: fareysums](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/fareysums.md)
- [Lopsided Lineup - kattis: lopsidedlineup](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/lopsidedlineup.md)
- [Distance - kattis: distance](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/distance.md)
- [Factorial Power - kattis: factorialpower](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/factorialpower.md)
- [Burizon Fort - kattis: burizonfort](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/burizonfort.md)
- [Johnny Applesack - kattis: applesack](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/applesack.md)
- [Accounting a.k.a. Bokforing - kattis: bokforing](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/bokforing.md)
- [Jumping Yoshi - kattis: jumpingyoshi](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/jumpingyoshi.md)
- [Ada Loveslaces - kattis: adaloveslaces](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/adaloveslaces.md)
- [Digit Division - kattis: digitdivision](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/digitdivision.md)
- [Integer Estate Agent - kattis: estate](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/estate.md)
- [The Paladin - kattis: thepaladin](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/thepaladin.md)
- [Srednji - kattis: srednji](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/srednji.md)
- [Left and Right - kattis: leftandright](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/leftandright.md)
- [Dams in Distress - kattis: damsindistress](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/damsindistress.md)
- [Sums - kattis: consecutivesums](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/consecutivesums.md)
- [Divisible Subsequences - kattis: divisible](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/divisible.md)
- [Joyless Game - kattis: joylessgame](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/joylessgame.md)
- [Powers and Modulus - kattis: powers](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/powers.md)
- [Clock Construction - Kattis: clockconstruction](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/clockconstruction.md)
- [Divisibility Shortcut - Kattis: shortcut](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/shortcut.md)
- [Eko - Kattis: eko](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/eko.md)
- [The Sound of Silence - Kattis: sound](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/sound.md)
- [Escape from Enemy Territory - Kattis: enemyterritory](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/enemyterritory.md)
- [Happy and Unhappy Numbers - Kattis: happyandunhappynumbers](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/happyandunhappynumbers.md)
- [Alehouse - Kattis: alehouse](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/alehouse.md)
- [Razbibriga - Kattis: razbibriga](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/razbibriga.md)
- [Common Factors - Kattis: commonfactors](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/commonfactors.md)
- [ICPC Team Selection - Kattis: icpcteamselection](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/icpcteamselection.md)
- [Boiling Vegetables - Kattis: vegetables](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/vegetables.md)
- [Spiderman - Kattis: spiderman](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/spiderman.md)
- [Wolf - Kattis: wolf](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/wolf.md)
- [Tram - Kattis: tram](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/tram.md)
- [Envious Exponents - Kattis: enviousexponents](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/enviousexponents.md)
- [Canvas Line - Kattis: canvasline](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/canvasline.md)
- [Kratki - Kattis: kratki](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/kratki.md)
- [Logland - Kattis: logland](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/logland.md)
- [Low Power - Kattis: low](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/low.md)
- [Stop Counting! - Kattis: stopcounting](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/stopcounting.md)
- [Chemist's Vows - Kattis: chemistsvows](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/chemistsvows.md)
- [Research Productivity Index - Kattis: researchproductivityindex](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/researchproductivityindex.md)
- [Combination Lock - Kattis: combinationlock](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/combinationlock.md)
- [Financial Planning - Kattis: financialplanning](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/financialplanning.md)
- [Svada - Kattis: svada](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/svada.md)
- [Orderly Class - Kattis: orderlyclass](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/orderlyclass.md)
- [ETA - Kattis: eta](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/eta.md)
- [Delft Distance - Kattis: delftdistance](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/delftdistance.md)
- [Irrational Division - Kattis: irrationaldivision](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/irrationaldivision.md)
- [Pianino - Kattis: pianino](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/pianino.md)
- [Reservoir - Kattis: reservoir](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/reservoir.md)
- [LCM Pair Sum - Kattis: lcmpairsum](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/lcmpairsum.md)
- [Eidam-Sand Lair - Kattis: eidamsandlair](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/eidamsandlair.md)
- [Andrew the Ant - Kattis: andrewant](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/andrewant.md)
- [Cake - Kattis: cake](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/cake.md)
- [Frogger - Kattis: frogger](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/frogger.md)
- [Mathemagicians - Kattis: mathemagicians](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/mathemagicians.md)
- [Antenna Analysis - Kattis: antennaanalysis](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/antennaanalysis.md)
- [Divisors - Kattis: divisors](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/divisors.md)
- [Abandoned Animal - Kattis: abandonedanimal](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/abandonedanimal.md)
- [Gladiators - Kattis: gladiators](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/gladiators.md)
- [Zbrka - Kattis: zbrka](https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/zbrka.md)

<details>
<summary>Current list of exercises to write-up</summary>
  
- Ocean Monument
- Brick Wall (redo the dynamic programming approach)
  
</details>
