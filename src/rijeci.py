# Riječi
# https://open.kattis.com/problems/rijeci
# TAGS: basic, fibonacci
# CP4: 5.4a, Fibonacci Numbers
# NOTES:
"""
- basic Fibonacci calculation
"""
K = int(input())

a, b = 0, 1

for _ in range(K-1):
    a, b = b, a+b
    
print(f"{a} {b}")