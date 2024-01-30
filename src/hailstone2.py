# Hailstone Sequences
# https://open.kattis.com/problems/hailstone2
# TAGS: basic
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
Collatz sequence but it asks for length of the sequence, including final 1, rather than 
the number of ops to reach 1, so there's a +=1 compared to "usual" answer
"""
n = int(input())
cnt = 1

while n > 1:
    cnt += 1
    if n % 2:
        n = 3 * n + 1
    else:
        n //= 2

print(cnt)