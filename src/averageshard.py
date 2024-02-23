# Paradox With Averages (Hard)
# https://open.kattis.com/problems/averageshard
# TAGS: mathematics
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
My solution for the Easy version passes this, so presumably was supposed to do a brute force for easy version O_o

So code is same as averageseasy.py
"""
T = int(input())

for _ in range(T):
    input() # blank line
    n_cs, n_econ = map(int, input().split())
    cs = list(map(int, input().split()))
    econ = map(int, input().split())

    S_econ = sum(econ)
    S_cs = sum(cs)
    ref_avg_econ = S_econ / n_econ
    ref_avg_cs = S_cs / n_cs

    cnt = 0
    for student in cs:
        if (S_econ + student) / (n_econ + 1) > ref_avg_econ and (S_cs - student) / (n_cs - 1) > ref_avg_cs:
            cnt += 1

    print(cnt)