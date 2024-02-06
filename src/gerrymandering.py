# Gerrymandering
# https://open.kattis.com/problems/gerrymandering
# TAGS: basic
# CP4: 1.6o, Time Waster, Easier
# NOTES:
"""
Just follow the formulae basically
"""
P, D = map(int, input().split())

votes = [[0, 0] for _ in range(D + 1)] # 0 is dummy due to 1 based indexing of Districts

for _ in range(P):
    d, A, B = map(int, input().split())
    votes[d][0] += A
    votes[d][1] += B

wa, wb, V = 0, 0, 0

for district_result in votes[1:]:
    A, B = district_result
    V += (A + B)
    if A > B:
        curr_wa = A - (int((A + B) / 2) + 1)
        print("A", curr_wa, B)
        wa += curr_wa
        wb += B
    else:
        curr_wb = B - (int((A + B) / 2) + 1)
        print("B", A, curr_wb)
        wa += A
        wb += curr_wb

print(abs(wa - wb) / V)