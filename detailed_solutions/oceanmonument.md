# Detailed solution for Kattis - Ocean Monument

[Problem statement on Kattis](https://open.kattis.com/problems/oceanmonument)

A really nice exercise where you can find an analytical solution, that maybe the authors missed, using some cool combinatorics techniques.

## Tags

mathematics, combinatorics

## Solution

As mentioned, this problem has small input values `g, e < 20`, so I'm guessing the authors were intending for a computational solution (dynamic programming or maybe even simulation approach?), but in fact you can solve this analytically for any value of `g, e`.

What is the "intuition" for looking for such an analytical solution? For me personally, drawing the combinations of `g` and `e` on paper made me think immediately of classic combinatorics problems of paths in a grid (i.e. if you have a `N x M` rectangle grid, there are `comb(N+M, N)` shortest paths from `(0,0)` to `(N,M)` I mean).

For the solution below, I'll also be mentioning "reflecting paths" which turned out to be very difficult to draw in ASCII here O_o. So I recommend to read e.g. this page [https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem](https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem) and/or search for "reflection method combinatorics" and make sure you understand, then the reasoning below will be much clearer I hope. Also draw the examples if you get confused, it's much clearer when you see it on paper.

There are some special cases for some values of `g, e` but for now we'll look at the general case - for now assume `e>0` and `g>0`, let's say **g = 2, e = 3**.

1. **You will always need to remove all elders**, e, which will always require therefore **E = 3 "elder missions"**
2. **Each E mission creates a new g**, so you will always end up with an **effective number of g's = g + E**. So here, 2+3 = 5 g's are in the problem effectively.
3. The way you process pairs of g's is by "reducing them" (lookup a `foldl` illustration picture from Haskell for example [here](https://user-images.githubusercontent.com/875834/56535678-4ad4c280-652a-11e9-99bb-710de7cb3e1a.png)):

```
5 g's

     g g g g g
      V / / /
       V / /
        V /
         V

reduced to 1 g, in 4 steps/"G missions"
```

**so it will take 5-1 = 4 "G missions" to end up in a room having cleared the last 2 g's**

4. So the optimal solution, before thinking about sequencing, **will always require E elder missions and G guardian missions, where G = e + g - 1** (CARE! see exception, later, for the cases with g=0 or e=0)

Now the combinatorics part: **how many ways are there to combine/sequence these E and G's ?**

In the concrete case g=2, e=3 we have 3 E's and 4 G's to sequence. This should make you think of lattice paths:

Naively the answer is, at first, just `comb(4+3, 3)`, i.e. the usual number of shortest paths between `(0,0)` and `(4,3)` in `G x E` space.

**However, there is a constraint/restriction that applies in this situation:**

- The original starting state is something like: g,g,e,e,e
- so you **can** perform 1 G mission before doing any E missions
- but you **cannot** perform 2 G missions before doing any E missions **because there won't be sufficiently many g's !!**

Similarly, you can do 2 G's after 1 E, but you **cannot** do 3 G's before 2 E's.

How can we modify the combinatorics result to account for this? This is where we can think of using the reflection method as mentioned earlier.

Do this on paper:

- Draw `G x E` space with the target point `(4,3)`
- Draw a dotted line ...... call it "uncrossable line": in this example it is given by `G=1,E=0 G=2,E=1 G=3,E=2 etc` i.e. the `E = G-1` line
- Draw a solid **shifted by +1 line** _____ call it "BAD line"

Now in other words you are looking for number of ways to get to `(4,3)` in `G x E` space **SUBJET TO CONDITION** that you never cross the ..... "uncrossable line".

**Using the reflection method insight**: you can therefore put the "BAD paths" in one-to-one correspondence with all the paths that **do touch the BAD line** _____ **and that start from the** "Reflection Point" i.e. the mirror image of the origin `(0,0)` with respect to the BAD line _____

(again, easy to draw on paper but impossible to ASCII O_o, just think of the example in the Ballot Problem linked earlier. Be careful though, don't confuse the uncrossable line, with the BAD line, which ends up being shifted +1, many website illustrations are unclear about this)

So in our example above, the BADS paths are in 1-1 correspondence with all paths from the reflection point - the reflection point ends up being therefore at `(2, -2)` to the target `(4, 3)`

**There are therefore `comb(4+3, 2)` BAD PATHS**

Putting it all together:

- there are `ALLS = comb(4+3, 3)` paths from `(0,0)` to `(4,3)`
- there are `BADS = comb(4+3, 2)` paths from `(0,0)` to `(4,3)` **that at some point have "too many G moves i.e. require more g's than currently available in the system"**

And so the answer we want is just `ALLS - BADS`.


### Generalizing the above walkthrough

Now generalizing the specific example g=2, e=3: how do you find the offset of the BADS line in general:

e.g. for g=3, e=4

- CAN do 1 G before any E end with -> g=2
- CAN do 2 G before any E end with -> g=1
- CANNOT do 3 G before any E -> currently at g=1 not enough to perform G mission

e.g. for g=5, e=18371

- CAN do 1 G....
- ...
- CANNOT do 5 G before any E

So in general the "uncrossable line" is given by (g-1), that's the max number of G moves possible before doing an E.

- therefore the bads line in general is given by (g-1)+1 i.e. it is given by g itself
- and therefore the reflection point is always located at (g,-g) in GxE space

So the general formulas are coming from following steps. Given g = 3, e = 7:

- E = e = 7
- G = e+g-1 = 9
- bad/reflection point is (g,-g) = (3,-3) in GxE grid
- ALLS = paths from (0,0) to (G,E) is comb(G+E, G) = comb(7+9, 9)
- BADS = paths from (3,-3) to (G,E) is comb(G+E, G - reflect_g) = comb(7+9, 9-3) in this case

### Handling cases with g = 0 or e = 0

The combinatorial approach above gives 0 as the answer when g = 0, or e = 0. But this isn't correct:

1. The answer is 1 for the case e=0, since you just reduce all the g's 2 at a time in g-1 steps
2. When g=0, e>0 **the answer is just a Catalan number** [https://en.wikipedia.org/wiki/Catalan_number](https://en.wikipedia.org/wiki/Catalan_number), since it's number of ways to make a path of "ups and downs" in the usual way except instead of Catalan(E) it's going to be Catalan(E-1) because the first move is forced (as is the second i.e. it has to be "up/E" but that's already incorporated into the Catalan definition)

**So for g=0 answer is `comb( 2 * (e-1), (e-1) ) // (e-1 + 1)`**

## AC code

```python
from math import comb

T = int(input())

for _ in range(T):
    g, e = map(int,input().split())

    if e == 0:
        print(1)
    elif g == 0:
        print(comb(2 * (e - 1), (e - 1)) // ((e - 1) + 1))
    else:
        # using capital letters to match the variables in the notes O_o
        E = e
        G = e + g - 1
        
        ALLS = comb(E + G, G)
        BADS = comb(E + G, G - g)
        
        print(ALLS - BADS)
```