# Collatz Conjecture
# https://open.kattis.com/problems/collatz
# TAGS: interpreter
# CP4: 5.2e, Number Systems/Seqs
# NOTES:
"""
Not very DRY but I didn't understand the additional requirement about the "stop when reach 1,4,2,1..." so
I implemented it in incremental steps.

Basically AFAICT it's saying "stop generating new terms after you reach 1 for the first time"
"""
while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break

    A_, B_ = A, B
    da, db = {}, {}
    sa, sb = 0, 0
    while True:
        if A != 1:
            da[A] = sa
        elif 1 not in da:
            da[1] = sa
        if B != 1:
            db[B] = sb
        elif 1 not in db:
            db[1] = sb
        if A in db:
            print(f"{A_} needs {da[A]} steps, {B_} needs {db[A]} steps, they meet at {A}")
            break
        elif B in da:
            print(f"{A_} needs {da[B]} steps, {B_} needs {db[B]} steps, they meet at {B}")
            break
        else:
            collatz = lambda n: n // 2 if n % 2 == 0 else 3 * n + 1
            if A != 1:
                A = collatz(A)
                sa += 1
            if B != 1:
                B = collatz(B)
                sb += 1