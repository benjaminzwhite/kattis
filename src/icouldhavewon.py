# I Could Have Won
# https://open.kattis.com/problems/icouldhavewon
# TAGS: game, logic, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE - maybe a logic/insightful general solution exists.

Below is just implementation as-asked.
"""
s = input()

res = []
for k in range(1, len(s) + 1):
    alice_wins, bob_wins = 0, 0
    alice_curr, bob_curr = 0, 0
    for c in s:
        if c == 'A':
            alice_curr += 1
        else:
            bob_curr += 1
        if alice_curr == k:
            alice_wins += 1
            alice_curr, bob_curr = 0, 0
        elif bob_curr == k:
            bob_wins += 1
            alice_curr, bob_curr = 0, 0
    if alice_wins > bob_wins:
        res.append(k)

L = len(res)
print(L)

if L > 0:
    print(*res)