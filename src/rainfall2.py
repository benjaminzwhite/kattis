# Rain Fall
# https://open.kattis.com/problems/rainfall2
# TAGS: physics, simulation, logic
# CP4: 0, Not In List Yet
# NOTES:
"""
CARE! T2 is a time "DELTA/DIFFERENCE" not a time "position" as you might expect, especially given that T1 is a time position. 
IMHO unclear and confusing variable name choice for a physics based exercise.

---

To find the reasoning for the 'range' stuff (why the possibility of a low and high value) you should focus on the testcase with H == L:

If, at observation time, you find that the level is EXACTLY at the leak level, then you have 1 extra possibility that you cannot rule
out (well, unless you look on the floor to see water everywhere lol):

It is possible that the rainfall amount is *just the right amount* to have reached the leak_line at just the right time as you observe it.

So theoretically the minimum possible is L, the leak line amount.

The theoretical maximum is the "physics" case you solve, i.e. where the water has fallen into the container in excess of the leak line
and has leaked out. This obviously means a higher amount of rainfall consistent with the observation

---

Main physics solution:

-> let P be rainfall rate, so the total amount W of water that falls is P * T1

1) Work back from end state to state at T1:
   At T1 + T2 (CARE! T2 is a TIME DELTA: STUPID NOTATION) the height is H but K * T2 water has leaked since T1, so the amount at T1
   would have been H(T1) == H + K * T2

2) Work forwards from start of rainfall to T1:
   At T1, when the rainfall stops, P * T1 fallen into container (and some has leaked out)
   While rain is falling there are 2 regimes: while the bottom of the container is filling up, there is 0 effective leak rate
   After reaching the level of the leak, water flows in at rate P and out at rate K, so effective leak rate is P-K
   At T1, the observed level would therefore be:

   P * TIME_TO_FILL_UP_TO_LEAK_LINE + P_effective * (TOTAL_RAINFALL_TIME - TIME_TO_FILL_UP_TO_LEAK_LINE)
   ------------VV-----------------    ----VV---         -------------------VV-------------------
       this is the level L              P - K           T1               -      L/P  since rainfall rate P is constant


So this gives, setting 1) == 2):  H + K * T2 = L + (P - K) * (T1 - L / P) which you solve for P   

So you solve: T1 * P**2 - (H + K*T2 + K*T1) * P + K*L == 0
"""
L, K, T1, T2, H = map(float, input().split())

# easy case: 
# if observed_water_level < leak_level - there never was enough water to leak out, so observed level IS the total rainfall
if H < L:
    print(H, H)
else:
    a = T1
    b = -(H + K * T2 + K * T1)
    c = K * L
    P = (-b + (b * b - 4 * a * c)**0.5) / (2 * a)
    res = P * T1
    if H == L: # see NOTES: this is the possibility of having just arrived as the rainfall just stopped exactly at L
        print(L, res)
    else:
        print(res, res)