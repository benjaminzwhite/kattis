# Detailed solution for Kattis - Wolf

[Problem statement on Kattis](https://open.kattis.com/problems/wolf)

An interesting reasoning exercise with some additional edge case and implementation logic also. It took me a while to find a proof that I was satisfied with, even if it takes a bit longer to explain.

## Tags

logic, game, proof

## Solution

### Proof

Basically, since the game ends immediately whenever 2 cards share a suit, you must postpone this event as long as possible:

1. Either until your opponent runs out of cards, or until you both run out of cards (both have 26 therefore) and place the 2 cards sharing a suit as the last pair
2. In all cases, if your opponent has more cards you cannot win (because even if you manage to stay in game until your last card, opponent has cards leftover so you do NOT have all 52 cards in your pile)

So the entire question really is:

- **Q: "Is it possible to arrange the 2 players' piles of cards such that no pair of same-suit occurs" (either at all, or until last pair in the case of 26 vs 26 cards) ?**

Let's prove statement **Q** by contradiction (assume I have `ME` number of cards and opponent has `OPP` number of cards):

- We have `ME > OPP` (since if `ME < OPP`, I lose in all cases as explained in `2` above) and `ME + OPP = 52`.

Suppose the answer is no; then in the arrangement where at least 2 cards occur in pairs of suits, take one of the pairs (and let the pair be **HEARTS** without loss of generality, just for the example shown below):

```
PILES

 ME: - - - - - - - xH - - - - - -  <== note we have ME > OPP cards hence the overhang of extra cards visible here
OPP: - - - - - - - yH - -  
                   ^^
                   occurence of a pair of same suits, here Hearts (H symbol)
```

Now, find a location (i.e. along the axis `- - -`) where **NO HEARTS OCCUR** - this may be a location with 2 cards, or just 1 card, depending on where the location occurs (see diagram above, only 1 card if you are in region of `ME` where you have more cards than opponent).

Now swap out any of those

- 2 cards from that pair, if you are in part where `ME` and `OPP` have cards 
- 1 card, if you are in the overhang where `ME > OPP` cards leftover

with any of the 2 hearts located at `xH` / `yH`. **The first pair now contains 1 Heart and 1 nonHeart and the "same suit pair" now contains only 1 Heart and 1 nonHeart.**

It just remains to prove that this operation is **ALWAYS** possible: i.e. that there is always a location where **NO HEARTS OCCUR** (again "HEARTS" is without loss of generality).

To prove is always possible: again, suppose it is not possible to find such a location - then this must mean that:

1. every single pair the entire distance of `OPP`, contains at least 1 HEART
2. every single card in the overhang `(ME - OPP)` is HEART also

This requires there to be `2 + (OPP-1) + (ME-OPP) = ME + 1`  total heart cards in the deck, **but this is a contradiction** since `ME > 52/2 = 26`, and `|HEARTS| == 13`.
 
(To be clear in this formula: `2` because you have 2 hearts `xH` `yH`, `OPP - 1` because you have `OPP - 1` pairs of `-` top and `-` bottom which would need to contain at least 1 heart, and finally `ME - OPP` becaue you have `ME - OPP` single cards which **all would need to be** Heart)

- Conclusion: therefore you **always win** if you have more cards than opponent, and **always lose** if you have fewer.

However we still need to consider the `N == 26` case, as there is an extra condition to check in that case:

If you have the **same number of cards, i.e. `N == 26` each**, in principle you can win (using the same logic as for the strict more-cards-than-opponent case), however you **STILL NEED TO BE ABLE TO "WIN" THE LAST SUIT-MATCH-PAIR FIGHT AT THE VERY END** i.e. you need to actually have one suit where you have a better card than your opponent: this will be the pair you place last in the rearranged decks

But be carefuly - not only do you need to have a card greater than the opponents of the same suit, you need to make sure that **OPPONENT ACTUALLY HAS AT LEAST ONE CARD OF THAT SUIT**. If you are not careful, you might return True if you have ALL the cards `1 -> 13` HEARTS for example, when in fact since opponent has NO hearts, you **CANNOT ACTUALLY BEAT THEM ON HEARTS PAIR**

(see Implementation Notes below on how I check all of this).


### Implementation Notes

I implement the `N == 26` case check by taking the `OPP` cards as being the set difference between `ME_CARDS` and `range(1, 13 + 1)`; then check that the smallest card in `OPP` cards is `<` largest of my cards, for at least 1 of the 4 suits: if so then you can beat them with that suit.

In the above, you need to check that the `max/min` is not an empty sequence i.e. need to handle the `default=` behavior:

- Assign a huge default value for the min(...) argument; that way if there is `None` and the `default=HUGE_NUMBER` gets used, the `min < max` will **fail** due to `HUGE_NUMBER < 13` being false
- Similarly, assign `0` value for the max(..) argument; that way if you don't have any cards of that suit, your max will be `0`, so `min(1,13+1) < 0` will be false also

This will handle the cases where either player has 0 cards of a given suit, for all suits.


## AC code

```python
ME_CARDS = int(input())

d = {k:set() for k in "CDHS"}

for _ in range(ME_CARDS):
    val, suit = input().split()
    d[suit].add(int(val))

flg = False
for suit in "CDHS":
    if min(set(range(1, 14)).difference(d[suit]), default=float('inf')) < max(d[suit], default=0):
        flg = True

if ME_CARDS > 26 or (ME_CARDS == 26 and flg):
    print("possible")
else:
    print("impossible")
```