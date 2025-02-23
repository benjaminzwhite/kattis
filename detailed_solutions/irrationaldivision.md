# Detailed solution for Kattis - Irrational Division

[Problem statement on Kattis](https://open.kattis.com/problems/irrationaldivision)

A very interesting game logic exercise and case-based analysis to find a proof that works.

It may help to draw the odd/even cases and rotate on paper 90 degrees when following the solution below.

## Tags

logic, proof

## Solution

The only way to score is to have a shape with "odd x odd" since otherwise if there is an even dimension, there will be
as many white as black squares so net 0. The absolute score of such a board is "1 delta" i.e. +1 or -1 depending on if there is
1 more black or white square respectively.

If the expectation of any board were greater than 1 (in absolute units i.e if you could score -2, -3, ... or +2, +3, ... with a hypothetical strategy) then you could instead stop the game immediately by just taking the whole remaining board and, at worse, you would have a penalty of -1 (if the remaining board had an excess of 1 white over black) or 0 (if matched) or +1 (if excess of black over white).

So, by contradiction, **in optimal play therefore you will not handover a board that scores more than 1 for your opponent**.

- A: So the best strategy, if it exists, is to score +1 on your turn and to handover a board that must score -1 for your opponent, giving you +2 difference with opponent
- B: Next best is to score +1 and handover a board that scores 0, or score 0 and handover a board that scores -1 for opponent, giving you +1 difference with opponent
- C: Final best strategy is to score 0 and handover 0, or score +1 and handover +1 also, giving you 0 difference with opponent

There are no other possible scores with optimal strategies.

Now let's examine the cases that enable the various strategies listed above:

### Case 1: if `p` is even

Then you are in **C** since you must score a board that has 1 even dimension (total score 0) and either handover an "odd x even" or "even x even" board to opponent who also scores 0 at "worst" (i.e. at best for them)

### Case 2: if `p` is odd

#### Case 2, subcase: `q` is odd

You can always score 1 on your turn by taking an odd number of "columns" e.g. if p,q = 3,4 then you would take 3x1 or 3x3 etc.

By taking an odd number of columns, the opponent is basically given a "start position with a board with black <=> white positions flipped" (to see this, cut off your column and flip the board 90 degrees clockwise -> the topleft corner is now WHITE so the excess that existed in favor of black is now in favor of white).

So, **if you gave your opponent an even amount** for **their** `p'` dimension, (their `p'` is `old_q - how many columns you took`;just draw it, it's hard to show in ASCII) then the best they can do is 0 score

This case will occur (giving opponent even `p'` dimenion) if `q` **was odd** since you took an **odd** number of your `p` columns)

- So summary of this configuration: `p` is odd, `q` is odd -> you gain +1, handover e.g. `p * (q - ODD)` board, rotated 90 degrees -> opponent has a `(q - ODD) * p` board with white as their topleft, so they can only score 0
- Therefore `p odd, q odd` -> **score = +1**

#### Case 2, subcase: `q` is even

On the other hand, **if you gave your opponent an odd amount** for **their** `p'` dimension (i.e original `p` odd, original `q` **even**, you take odd number of columns to get +1 score and handover `p * (q - ODD)`, rotate 90 degrees -> opponent has `(q - ODD) * p` board with white as topleft square)

In this situation, if `q` was even, then opponent has therefore `p' * q'` with `p' = q - ODD` and `q' = p`, so **their** `p'` and `q'`  are both **odd**.

Since they now have an "odd x odd" board where the top-left is white, there is an excess of +1 **white** ie. if they take this entire board they score -1

So if they can't handover this -1 score to you, your total score will be `1 - (-1) = 2` difference since you have +1 they have -1

The only way to do this is to be able to handover to opponent an "odd x odd" square (now with white corner in top-left) because this is the only way you can continue this strategy such that they are forced to take the last (top-**right**) white square.

In other words, it's **the only way you can deny them** the "immediately end the game with score 0" option that would otherwise be available.

- If this isn't clear, draw it: you can see how it forces their strategy to become taking even number of columns that score 0 and you take even number of corresponding rows on your turn, always handing over a smaller `x * x` **odd square** until you handover `1 * 1` white square to opponent.

This "special" strategy is accessible on opponent's turn if they can take from their dimension an even number of "columns" such that the reduced amount leftover matches the smaller other dimension leftover:


```
     X|OXO     OXO
     O|XOX     XOX
     X|OXO     OXO___ if opponent cuts here they CAN give 3x3 oddsquare to you with O white in topleft
     O|XOX     XOX
     X|OXO     OXO
      ^__your first move

     X|OXOXOXO
     O|XOXOXOX        <--- now with the 3 * 7, the opponent CANNOT "cut" their 3-dimension DOWN to match 7 to form a 7*7 odd squre
     X|OXOXOXO
      ^__ your first move
```


## AC code

```python
p, q = map(int, input().split())

# Case 1: detailed in notes above
# p is even
if p % 2 == 0:
    print(0)
else:
    # Case 2: detailed in notes above
    # p is odd
    # Subcase: q is odd also:
    if q % 2 == 1:
        print(1)
    else:
        # Subcase: q is even:
        # Extra condition: can opponent, on their turn, cut their dimension DOWN to form an odd square to give back to you ?
        # If so, they can cancel your score
        if p > q:
            # e.g. p = 5, q = 4 -> opponent takes 1 col or 3 cols and leaves you seeing q-1 or q-3 * p rectangle:
            # e.g. WLOG 3*5 rectangle: you cut 2 of your "columns" and handover 3x3 oddsquare with white in topleft, which scores -1 for opponent
            print(0)
        else:
            print(2)
```
