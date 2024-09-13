# Flag Quiz
# https://open.kattis.com/problems/flagquiz
# TAGS: array, string
# CP4: 2.2d, 2D Array, Harder
# NOTES:
"""
Reading comprehension: it is min-max edit difference between zipped arrays 
"""
question = input()
N = int(input())

answers = []

for _ in range(N):
    a = input()
    answers.append(a)
    
to_process = [x.split(', ') for x in answers]

res = []
min_incog = float('inf')

for i in range(N):
    max_incog = -1
    for j in range(N):
        if i == j:
            continue
        curr_incog = sum(1 for a, b in zip(to_process[i], to_process[j]) if a != b)
        if curr_incog > max_incog:
            max_incog = curr_incog
    if max_incog < min_incog:
        min_incog = max_incog
        res = [i]
    elif max_incog == min_incog:
        res.append(i)

for i in res:
    print(answers[i])