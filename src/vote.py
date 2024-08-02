# Popular Vote
# https://open.kattis.com/problems/vote
# TAGS: basic, array
# CP4: 1.4i, Still Easy
# NOTES:
T = int(input())

for _ in range(T):
    n = int(input())
    xs = []
    for _ in range(n):
        xs.append(int(input()))

    most, total, winner = 0, 0, -1
    for i, x in enumerate(xs, 1):
        total += x
        if x > most:
            most = x
            winner = i
        elif x == most:
            winner = -1 # use -1 for cases with ties
    
    if winner == -1:
        print("no winner")
    else:
        if most > total / 2: # should compare 2*most > total for numerical stability
            print(f"majority winner {winner}")
        else:
            print(f"minority winner {winner}")