# Kafkaesque
# https://open.kattis.com/problems/kafkaesque
# TAGS: array
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
Count how many occurences of "decreases" there are: makes sense logically - any time there is a descent you must repass 1 more time
"""
n = int(input())

xs = []
for _ in range(n):
    xs.append(int(input()))
    
res = 1
for fst, snd in zip(xs, xs[1:]):
    if fst > snd:
        res += 1
        
print(res)