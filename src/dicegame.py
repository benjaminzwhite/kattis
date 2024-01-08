# Dice Game
# https://open.kattis.com/problems/dicegame
# TAGS: mathematics, code golf
# CP4: 5.5a, Probability, Easier
# NOTES:
"""
- after solving using probability calculation, you can simplify significantly (if you want to code golf or get faster solution)

(see below for 2nd approach)
"""
# First approach
g1,g2,g3,g4 = map(int, input().split())
e1,e2,e3,e4 = map(int, input().split())

def exp_value(a,b):
    a, b = min(a,b), max(a,b)
    return sum(range(a, b+1)) / (b - a + 1)
    
gunnar = exp_value(g1,g2) + exp_value(g3,g4)
emma = exp_value(e1,e2) + exp_value(e3,e4)

if gunnar > emma:
    print("Gunnar")
elif gunnar == emma:
    print("Tie")
else:
    print("Emma")

# Second approach
# If you work out the exp_value using Gauss sum -> a+b * (b-a+1)//2 we find that:
# exp value = (g1+g2+g3+g4 / 2) i.e. the sum of inputs is all that is needed
"""
G = sum(map(int, input().split())) # don't need to divide by 2 since G & E both have same factor of 2
E = sum(map(int, input().split()))

if G > E:print("Gunnar")
elif G == E:print("Tie")
else:print("Emma")
"""