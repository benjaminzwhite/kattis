# Interesting Integers
# https://open.kattis.com/problems/interestingintegers
# TAGS: mathematics, number theory, brute force, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE: I think you can solve more efficiently with modular arithmetic and the extended Euclidean algorithm

---

Writing out e.g.:

G3 = G2 + G1
G4 = G3 + G2 = (G2+G1) + G2 = 2*G2 + G1
G5 = G4 + G3 = (2*G2+G1) + (G2+G1) = 3*G2 + 2*G1
G6 = G5 + G4 = (3*G2+2*G1) + (2*G2+G1) = 5*G2 + 3*G1
                                         ^      ^
                                         |      |

you see how the Fibonacci numbers appear, because the coeffs of G(i), G(i-1) satisfy Fibonacci recurrence and start as 1x 1x.

So you are looking to express n ==  F_i * b + F_i_-_1 * a, with the smallest possible b multiplier and a > 0.

CARE! note the weird b and a order, I was getting wrong answer due to the exercise's notation choice (b multiplies the *first* term and a the *second*)

So, a brute force approach is: just try to remove F_i in descending order from n, in increasing multiples i.e. b=1,2,3...
Then check that leftover n - F_i * b is divisible by the next smaller fib number F_i_-_1. 
You can break immediately since b is guaranteed to be smallest possible result at this point since have done in decreasing size of the F_i.
"""
# --- Precompute Fibonacci numbers ---
N_MAX = 10 ** 9
F = [0, 1]
x, y = 0, 1
while y < N_MAX:
    x, y = y, x + y
    F.append(y)

F_i_MAX = len(F) - 1

# --- Queries ---
T = int(input())
for _ in range(T):
    n = int(input())
    found = False
    i = F_i_MAX
    while not found:
        b = 1
        Fbig, Fsmall = F[i], F[i - 1]
        # CARE! need strictly >0 here, and not >=0, since it wants a to be nonzero i.e cant have n = b*something + 0*_
        while not found and (m := n - b * Fbig) > 0:
            a, r = divmod(m, Fsmall)
            if r == 0 and a <= b:
                print(a, b)
                found = True
                break
            b += 1
        i -= 1