# Number Colosseum
# https://open.kattis.com/problems/numbercolosseum
# TAGS: array, stack
# CP4: 0, Not In List Yet
# NOTES:
N = int(input())
xs = list(map(int, input().split())) # actually, don't need to list()

stk = []
for x in xs:
    stk.append(x)
    while len(stk) >= 2 and stk[-2] * stk[-1] < 0:
        x = stk.pop()
        y = stk.pop()
        winner = x + y
        if winner != 0:
            stk.append(winner)

if not stk:
    print("Tie!")
else:
	res = "Negatives" if stk[0] < 0 else "Positives"
    print(f"{res} win!")
    print(*stk)