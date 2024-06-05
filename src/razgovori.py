# Razgovori
# https://open.kattis.com/problems/razgovori
# TAGS: array, sorting, logic
# CP4: 0, Not In List Yet
# NOTES:
"""
The specific house numbers don't matter, just their left to right ordering:

Sort the number_of_calls by the order in which they appear left to right - do a drawing to visualize:
The example here is for sorted number_of_calls = 1,2,5,2,4 (see the vertical lines of 'x' below)
Calls are represented as ---


          x--?                 
          x-?        x--?   .
          x----?     x----? .
       x--x------x---x--?   .
    x--x--x------x---x----? .
                                <-- NOTE HERE THE VERTICAL LINE OF . AT THE RIGHT
                                    IMAGINE A DUMMY RIGHTMOST "WALL" WITH A "DETECTOR WITH 0 CALLS"
                                    THIS IS TO TRIGGER PROCESSING AT END OF ARRAY

Focus on the ---, known calls that pass through detectors from left to right:

WHENEVER A "RIGHT" DETECTOR HAS FEWER CALLS THAN PREVIOUS "LEFT" DETECTOR, the L -> R calls must
have terminated SOMEWHERE IN BETWEEN

-> the specifics of where they terminated are irrelevant, so I put ? in drawing above.
-> the point is that, tracking calls-that-actually-ended allows you to fix the lowerbound on how many calls there are
-> so in the above, going from 5-calls-detected to 2-calls-detected we know that 3 ACTUAL phone calls ended somewhere in between those 2 detectors
-> then as we then increment 2,to 4 calls, we can't say anything (in principle the 2->4 calls could be: 2->0 2 distinct calls , then 0->4 +4 distinct calls for a total of 6
   or it could be that the 2->4 is due to just delta=+2 new calls (as illustrated above)
   => in the optimal case you are reusing as many previously detected calls as possible, that's what the current approach implements
-> the rightmost wall is basically a detector with 0 calls, after all REAL detectors have been processed: that way, as illustrated above,
   any calls that occured on current left_value will be terminated , so we account for the l-r = l-0 = l actual calls that ended after the rightmost REAL detector (here 4 see the 4 ?'s)
"""
detectors, houses = map(int, input().split()) # dont need number of houses

xs = []
for _ in range(detectors):
    detector_num, calls = map(int, input().split())
    xs.append((detector_num, calls))

xs = sorted(xs, key=lambda x:x[0]) # sort from left to right according to the order of the detectors
xs.append(("LAST_ELEMENT_DUMMY", 0)) # see illustration above, dummy detector to the right of all real detectors, which detects 0 calls -> triggers processing of last real interval

res = 0
for (_, l), (_, r) in zip(xs, xs[1:]):
    if r < l:
        # how many calls must have terminated in this previous range: l - r
        res += l - r

print(res)