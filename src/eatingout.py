# Eating Out
# https://open.kattis.com/problems/eatingout
# TAGS: logic
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
Reading comprehension: I misunderstood English "no item is picked by everyone" on first submit.

I thought it means:

"Is there a way to pick the items such that there is an item that is not picked by everyone?"
(with this interpretation, answer is: if any(x < m for x in (a, b, c)) then return True)

However, the expected problem interepretation is actually:

Suppose e.g. m = 7, a = 5, b = 4. What can c be?

    1 2 3 4 5 6 7
  a x x x x x
  b       x x x x   <--- arrange B to create the FEWEST/MINIMUM NUMBER OF OVERLAPS WITH THE ITEMS CHOSEN BY A (since labels are irrelevant, assume a chooses 1->5, so b chooses downwards from 7->4, creating 2 OVERLAPS)
  c . . .     . .   <--- placing C in 4 or 5 will create a vertical column of 3 x's i.e. AN ITEM CHOSEN BY a AND b AND c. THIS IS WHAT WE WANT TO AVOID.

In above, c has 5 available . spots.
However, if you attempt to place in the column #4 or #5 you will create a column of 3 x's

Here, 5, the number of . is determined by:
5 = (m-a) + (m-b) = 2*m - a - b

---

Referring to above concrete example; in general we want:
c <= 2*m - a - b

which is just:

a + b + c <= 2 * m
"""
m, a, b, c = map(int, input().split())

if a + b + c <= 2 * m:
    print("possible")
else:
    print("impossible")