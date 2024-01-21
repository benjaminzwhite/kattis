# Paradox With Averages
# https://open.kattis.com/problems/averageseasy
# TAGS: array
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
A bit of reading comprehension/testcase reverse engineering to be 100% clear what is being asked for.

I first understood we wanted to get the ECON_AVG > CS_AVG, but in fact what it actually wants is whether: 

new_econ_avg > original_econ_avg

AND

new_cs_avg > original_cs_avg
"""
T = int(input())

for _ in range(T):
    input() # blank line
    n_cs, n_econ = map(int, input().split())
    cs = list(map(int, input().split()))
    econ = map(int, input().split()) # don't need to convert to list, only need to iterate once

    S_econ = sum(econ)
    S_cs = sum(cs)
    ref_avg_econ = S_econ / n_econ
    ref_avg_cs = S_cs / n_cs

    cnt = 0
    for student in cs:
        if (S_econ + student) / (n_econ + 1) > ref_avg_econ and (S_cs - student) / (n_cs - 1) > ref_avg_cs:
            cnt += 1

    print(cnt)