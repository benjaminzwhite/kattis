# Tour de France
# https://open.kattis.com/problems/tourdefrance
# TAGS: sorting, brute force
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
CARE! It has a kind of strict formatting requirement: "For each test case, output the maximum spread rounded to two decimal places."
but even if your answer is correct as float, rounded to 2 decimal places, you still need to format the decimal place:

For example if answer is 7.5, it seems that you need to print 7.50. Or if answer is 471 you need to print 471.00.

(I got WA on first submit, then used f"{max_spread:.2f}" instead of round(max_spread,2) and got AC, that was the only change.
"""
while True:
    fr = input()
    if fr == '0':
        break
    f, r = map(int, fr.split())
    fronts = list(map(int, input().split()))
    rears = list(map(int, input().split()))

    drive_ratios = []

    for n in rears:
        for m in fronts:
            drive_ratios.append(n / m)

    drive_ratios = sorted(drive_ratios)

    max_spread = -1
    for dr1, dr2 in zip(drive_ratios, drive_ratios[1:]):
        spread = dr2 / dr1
        max_spread = max(max_spread, spread)

    print(f"{max_spread:.2f}")