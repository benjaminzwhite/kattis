# Raðir - radir
# https://open.kattis.com/problems/radir
# TAGS: logic, dict
# CP4: 3.2c, Three+ Nested Loops, E
# NOTES:
"""
My first solution was slow so resolved after thinking it through a bit:

You are looking to form a sequence of 3 ascending cards, so the insight to solve efficiently is that 
YOU DON'T NEED TO DETERMINE THE OPTIMAL STRATEGY, since that strategy will "always be possible":

THE EARLIEST MOMENT YOU FIND THAT AT LEAST ONE 3-SEQUENCE HAS OCCURED IN THE DRAW-CARDS-RECORD,
then you know that you COULD HAVE OBTAINED THIS using *SOME* discard strategy/choices.

IT DOESN'T MATTER THE SPECIFICS - just pretend you are a time traveller:

e.g. if first 3-sequence that appears is 4 hearts 5 hearts 6 hearts, then the optimal strategy is hold to on
to those 3 cards as soon as each one appears, that's it 
(with "future knowledge" of the fact that this will turn out to be the earliest-appearing 3-sequence)

---

Implementation notes:

So based on the above logic:

- Maintain a set() (or dict with None values whatever) for each of the 4 "colors" '1', '2','3','4'
- For each input you get, (color C / value v), check if IN THE DICT, under key=C, the values -1,-2 appear, or -1,+1, or +1,+2 
- These are the only 3 ways of getting a sequence with the desired 3-sequence increasing pattern, including the current element being processed
"""
n, p = map(int, input().split())

d = {'1':{}, '2':{}, '3':{}, '4':{}}

res = None
for t in range(n):
    C, v = input().split()
    v = int(v)
    d[C][v] = None # not very good practice - it's just to record that v is now in the dict for color C
    if (v - 1 in d[C] and v - 2 in d[C]) or (v - 1 in d[C] and v + 1 in d[C]) or (v + 1 in d[C] and v + 2 in d[C]):
        res = t + 1 - p
        break

if res is None:
    print("neibb")
else:
    print(max(1, res))