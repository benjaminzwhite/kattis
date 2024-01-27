# Army Strength (Hard)
# https://open.kattis.com/problems/armystrengthhard
# TAGS: logic
# CP4: 1.4h, Easy
# NOTES:
"""
- Since you always remove weakest, the only relevant battle is the last one between the weakest of Godzilla and Mecha
- The tie breaker means that Godzilla wins if his max_g >= max_m while Mecha needs max_m > max_g
"""
T = int(input())

for _ in range(T):
    input()
    NG, NM = map(int, input().split()) # not needed, left variable names for clarity
    xs_g = map(int, input().split())
    xs_m = map(int, input().split())
    
    if max(xs_m) > max(xs_g):
        print("MechaGodzilla")
    else:
        print("Godzilla")