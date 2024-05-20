# Association for Computing Machinery
# https://open.kattis.com/problems/acm2
# TAGS: sorting
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
IMHO the exercise statement is missing an explanation of *what the penalty scoring is* ??

When I did ctrl-F "penalty" in the description the first result is in the Inputs section, and it says
"... so you have penalty of 330 minutes as per ICPC rules" O_o

So you have to reverse engineer given examples or look up online if you don't participate in ICPC competitions.
(even then, it's hard to find a clear statement on the ICPC site - I just found instead an old codeforces blog
where it was explained: you just accumulate total time spent on all exercises up until that point)
"""
N, p = map(int, input().split())
xs = list(map(int, input().split()))

first = xs[p]
del xs[p]
xs = [first] + sorted(xs)

actual_time = 0
acc_penalty = 0
solved = 0
i = 0
while i < N:
    if xs[i] + actual_time <= 300:
        actual_time += xs[i]
        acc_penalty += actual_time
        solved += 1
        i += 1
    else:
        break

print(solved, acc_penalty)