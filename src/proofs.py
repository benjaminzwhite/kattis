# Proofs
# https://open.kattis.com/problems/proofs
# TAGS: set, string
# CP4: 2.3d, Hash Table (set)
# NOTES:
n = int(input())

d = set()
flg = True
for i in range(1, n + 1):
    a, c = input().split('->')
    if not a: # if not a then line is of form "-> CONCLUSION" which is taken to be an AXIOM THEREFORE TRUE
        d.add(c.strip()) # CARE! got W.A locally before submit until tried stripping whitespace, might not be relevant on Kattis itself though
    else: # if there is a, then a contains up to 5 assumptions - all of them need to have been previously "derived" or "axiomatically assumed" i.e. they need to be in set() d which tracks valid conclusions and axioms
        if all(assumption in d for assumption in a.split()):
            d.add(c.strip())
        else:
            print(i)
            flg = False
            break 
if flg:
    print("correct")