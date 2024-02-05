# Dunglish
# https://open.kattis.com/problems/dunglish
# TAGS: mathematics, combinatorics
# CP4: 8.7h, Mathematics+Other
# NOTES:
"""
The combinatorics part is quite simple; then there is some string formatting/output requirements.

For each word, store the number of correct and incorrect assignments as [c, i] value associated to the word as key in the dict, d = {k:v}

Then go through input sentence: for each word, lookup in d how many correct assignments it has and increase combinatorial
product by *= num_correct_assignments.

ALSO, increase number of ALL ASSIGNMENTS (i.e. correct + incorrect) by *= (correct + incorrect)

We then get the BAD ASSIGNMNETS by inclusion exclusion -> total - correct = incorrect assignments

---

Implementation notes:

Need to default initialize the dict with [0, 0] values:
-> each time you see a word to process, if it is not in d already, assign it a value of [0, 0], then can incremement

Also, don't need to store the inputs - can just process on the fly (I noticed after submitting code below, a[] is not used).
"""
n = input()

s = input()

m = int(input())

a = []
for _ in range(m):
    a.append(input())

d = {} # k:v will be ---> word:[correct_assignments, incorrect_assignments]
translation = {}

for line in a:
    w, w_english, tf = line.split()
    if w not in d:
        d[w] = [0, 0]
    if tf == "correct":
        d[w][0] += 1
    else:
        d[w][1] += 1
    translation[w] = w_english

corrects = 1
total = 1
for w in s.split():
    corrects *= d[w][0]
    total *= (d[w][0] + d[w][1])

incorrects = total - corrects

if (corrects == 0) and (incorrects == 1):
    print(' '.join(translation[w] for w in s.split()))
    print("incorrect")
elif (corrects == 1) and (incorrects == 0):
    print(' '.join(translation[w] for w in s.split()))
    print("correct")
else:
    print(corrects, "correct")
    print(incorrects, "incorrect")