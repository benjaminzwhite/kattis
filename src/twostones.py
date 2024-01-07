# Take Two Stones
# https://open.kattis.com/problems/twostones
# TAGS: logic, game, proof
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
Parity argument - Alice's winning state involves an Odd number (1,3,5...) of Odd (len = 1) sequences

Given a current state, removing 2 adjacent stones DOES NOT CHANGE THE PARITY OF THE NUMBER OF ODD SEQUENCES

e.g.  XXXXXX -> X..XXX we go from 0->2 Odd sequences (0 and 2 are both even)
e.g.  XXXXXX -> XX..XX we go from 0->0 Odd sequences (0 and 0 are both even)
e.g. XXXXXXX ->X..XXXX we go from 1->1 Odd sequences (1 and 1 are both odd)
e.g. XXXXXXX ->XX..XXX we go from 1->1 Odd sequences (1 and 1 are both odd)

So Alice wins iif the INITIAL state involves an Odd number of Odd sequences

-> since initial state is 1 contiguous seqence of lentgh n, this implies initial 
   value of n must be Odd for Alice to win, Even for Bob to win
"""
N = int(input())

if N % 2:
    print("Alice")
else:
    print("Bob")