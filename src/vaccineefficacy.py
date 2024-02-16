# Vaccine Efficacy
# https://open.kattis.com/problems/vaccineefficacy
# TAGS: array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
N = int(input())

vaccinateds = 0
ctrl_group = 0

res= [[0, 0], [0, 0], [0, 0]] # infected with A/B/C - [with vaccine, without vaccine]

for _ in range(N):
    V, a, b, c = list(input())
    if V == 'Y':
        vaccinateds += 1
        for i, x in zip(range(3), (a, b, c)):
            if x == 'Y':
                res[i][0] += 1
        
    elif V == 'N':
        ctrl_group += 1
        for i, x in zip(range(3), (a, b, c)):
            if x == 'Y':
                res[i][1] += 1

for grp in res:
    treated, untreated = grp
    v_inf = treated / vaccinateds
    no_inf = untreated / ctrl_group
    if no_inf <= v_inf:
        print("Not Effective")
    else:
        print(100 * (no_inf - v_inf) / no_inf)