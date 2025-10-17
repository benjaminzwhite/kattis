# Borðspil
# https://open.kattis.com/problems/bordspil
# TAGS: game, logic
# CP4: 0, Not In List Yet
# NOTES:
"""
My opponent can beat my strategy P,Q,R where P >= Q >= R are quantities in **descending order**, if he has
Q+1 + R+1 stones, since he just places +1 stone on each of pile Q and R.

i.e. opponent wins by picking my 2 lowest piles and placing +1 stone on that amount on both piles.
He picks my lowest 2 piles since these are the easiest ones to win.
I therefore have to make my 2 lowest piles as large as possible.

So which division strategy maximizes the number of stones needed by the opponent?

Suppose I have 20 stones: one approach would be P Q R = 10, 10, 0
then opponent needs 10+1 + 0+1 = 12 stones to win

Instead if I do P Q R = 7, 7, 6
then opponent needs 7+1 + 6+1 = 15 stones to win

In general if you "fair divide" then opponent will need roughly > 2/3 of your stones to win, with
other division strategies requiring a smaller fraction (and therefore worse).
"""
me, opponent = map(int, input().split())

q, r = divmod(me, 3)

needed = 2 * q

if r == 2:
    needed += 1 # if r==2 then we are in case like 20 where piles are 7,7,6 so 2nd largest pile will have size q+1 and 3rd largest will be of size q

needed += 2 # these are the +1 and +1 for opponent to win the 2 smallest piles

if opponent >= needed:
    print("Unnar")
else:
    print("Arnar")