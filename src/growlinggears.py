# Growling Gears
# https://open.kattis.com/problems/growlinggears
# TAGS: mathematics, calculus
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
Just calculate derivative of the formula
"""
num_cases = int(input())

for _ in range(num_cases):
    n = int(input())
    best_gear = -1
    max_torque = -1
    
    for gear in range(1, n + 1):
        a, b, c = map(int, input().split())
        R_max = b / (2 * a)
        T_max = -a * (R_max**2) + b * R_max + c
        if T_max > max_torque:
            max_torque = T_max
            best_gear = gear
    print(best_gear)