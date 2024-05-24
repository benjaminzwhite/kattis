# Determining Nucleotide Assortments
# https://open.kattis.com/problems/nucleotides
# TAGS: sorting, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE: Solution is fine, just wondering if there is better/DRYer way to solve.

The underlying logic/solution is nasically a range query with 4 different items being counted.

Not 100% happy with how I implement sort-with-key:
I want to sort by "highest count score" and tiebreak by appearance order in ATGC (that's what exercise asks)
"""
s = input()

AS, TS, GS, CS = [0], [0], [0], [0]

for c in s:
    for xs in (AS, TS, GS, CS):
        xs.append(xs[-1])
    if c == 'A':
        AS[-1] += 1
    elif c == 'T':
        TS[-1] += 1
    elif c == 'G':
        GS[-1] += 1
    else:
        CS[-1] += 1

M = int(input())
for _ in range(M):
    l, r = map(int, input().split())
    aa = AS[r] - AS[l - 1]
    tt = TS[r] - TS[l - 1]
    gg = GS[r] - GS[l - 1]
    cc = CS[r] - CS[l - 1]

    tmp = sorted(zip([aa, tt, gg, cc], "ATGC"), key=lambda x: -x[0])
    print(''.join(t[1] for t in tmp))