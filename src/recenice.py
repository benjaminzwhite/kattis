# Rečenice
# https://open.kattis.com/problems/recenice
# TAGS: dict, string
# CP4: 2.3f, Hash Table (map), H
# NOTES:
"""
Most of the code is making the d which encodes {k:v} -> {number_as_int:number_as_spoken_string}

Implementation note (for Python):

Since dict keys are created in order 1,2,3...998,999 and SINCE DICT IS STABLE IN PYTHON
then you can iterate over d.items() directly and the keys will still be in ascending order
"""
# -- Precompute the lookup dict --
d = {k:v for k, v in zip(range(1, 20), "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}

tens = {k:v for k, v in zip(range(20, 90 + 1, 10), "twenty thirty forty fifty sixty seventy eighty ninety".split())}

for n in range(20, 100):
    a, b = divmod(n, 10)
    if b == 0:
        d[n] = tens[n]
    else:
        tmp = tens[a * 10] + d[b]
        d[n] = tmp

for n in range(100, 1000):
    a, b = divmod(n, 100)
    if b == 0:
        tmp = d[a] + "hundred"
        d[n] = tmp
    else:
        tmp = d[a] + "hundred" + d[b]
        d[n] = tmp

# -- Queries --
N = int(input())

len_without = -1 # because of the $ sign which should NOT count in total length so start count at -1 instead of 0
sentence = []
for _ in range(N):
    s = input()
    sentence.append(s)
    len_without += len(s)

# exercise wants the SMALLEST value of v which matches the condition
# (see Implementation Note for why we can just iterate over d.items() instead of looking up k for k in range(1, 999 + 1))
for k, v in d.items():
    if len_without + len(v) == k:
        res = v
        break

for i, x in enumerate(sentence):
    if x == '$':
        sentence[i] = res

print(' '.join(sentence))