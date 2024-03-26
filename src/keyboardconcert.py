# Keyboards in Concert
# https://open.kattis.com/problems/keyboardconcert
# TAGS: greedy, logic, proof, improve
# CP4: 3.5f, DP level 1
# NOTES:
"""
TODO: IMPROVE:

Current version is a bit clunky due to modifying from a start version that ended up not working:

In first version I was deleteing from the [instruments_that_reach_this_point] list. Then I modified, and I recreate a [tmp] list
and add to it each iteration - it's clunky but helped me debug and get AC.

-> better implementation might just be to have a boolean array and to update it - as long as at least one instrument is True can
keep going, else just reset the array to "True if current note can be played" etc

---

Proof:

Imagine at any given timepoint there are multiple instruments that are possible for this current note; the best one to pick is
the one which will take you the furthest before needing another switch, always. Why?

         1  2  3  4  5  6
     A   y  y  n  n  y  |y
     B   y  n  n  n  y  |y
     C   y  y  y  y  y  |n

At t=1 you can choose A,B,or C: picking C will be the right choice since it requires its first switch at the LATEST t (3,2,6 for A,B,C respectively)
Why is this always the global optimal choice? Because by assumption, all the other choices (A,B here) will have ALREADY HAD AT LEAST 1 (and possibly more)
switches by t=6, so by transitioning from C to A or B you will be in the same current state as A or B, but with either the same OR FEWER total switches made.
(update: actually I think it will always be strictly FEWER since e.g. if A is not able to play note at t =3, then it switches from y to n and then again from n to y at some later time
so in any case being in state A would require at least 1 more switch that being in C up to time t=6 - values are chosen for concreteness, principle is general afaict)

---

Implementation:
 
-> you can maintain a list of all the instruments that are still valid up until the current time, t, as a function of t:
   with the above example that would look like [A,B,C], then [A,C], then [C],[C],[C], [] <--- good streak runs out at t=6 so the longest you can go
   without switching based on any initial choice of A,B,C is to reach t=6. So at t=6 you just reset this tracking list: you create at t=6
   a new list WITH ALL THE INSTRUMENTS THAT ARE ABLE TO PLAY THE CURRENT NOTE notes[t=6], and repeat the process.
-> To avoid lots of lookup, create 2 mappings: the instrument info which allows to see whether a given instrument can play a current note
-> and also, a notes info mapping; whenever you need to reset the [] list above, notes info[note_at_time_t] gives you all
   possible instruments that are known to play that note (e.g. in the above example, we would get notes_info[note at t=6] = [A,B])
"""
INSTRUMENTS, NOTES = map(int, input().split())

INSTRUMENT_INFO = {}
NOTES_INFO = {}
for i in range(INSTRUMENTS):
    _, *xs, = map(int, input().split())
    INSTRUMENT_INFO[i] = set(xs)
    for x in xs:
        if x not in NOTES_INFO:
            NOTES_INFO[x] = []
        NOTES_INFO[x].append(i)

notes = list(map(int, input().split()))

switches = 0

instruments_that_reach_this_point = NOTES_INFO[notes[0]][:] # initialize the "[A,B,C] list" described above

for note in notes[1:]:
    tmp = []
    for instrument in instruments_that_reach_this_point:
        if note in INSTRUMENT_INFO[instrument]:
            tmp.append(instrument)
    if not tmp: # this corresponds to reaching the t=6 situation described above
        switches += 1 
        instruments_that_reach_this_point = NOTES_INFO[note][:] # fast lookup which instruments can play the current note at "t=6" CARE! make sure you [:] copy !!!
    else:
        instruments_that_reach_this_point = tmp # CARE! don't forget this step!!

print(switches)