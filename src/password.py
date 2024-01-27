# Password Hacking
# https://open.kattis.com/problems/password
# TAGS: mathematics, greedy, sorting
# CP4: 5.5a, Probability, Easier
# NOTES:
"""
We just try the passwords in descending order of probability.

So need to reverse sort probabilities list so that we try the highest probability password first.

CARE! Using Python enumerate, start from 1 since we are finding expected value for the NUMBER OF GUESSES (first guess = 1, etc.)
"""
N = int(input())

ps = []

for _ in range(N):
    _, p = input().split()
    ps.append(float(p))
    
res = sum(i * x for i, x in enumerate(sorted(ps, reverse=True), 1)) 

print(res)