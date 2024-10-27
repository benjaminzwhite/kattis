# Loo Rolls
# https://open.kattis.com/problems/loorolls
# TAGS: mathematics, recursion
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
Reading comprehension :

I returned to this several times, I had a hard time understanding the description

---

You start with 1 roll of size L and decrement it in blocks of size N.

If L is divisible by N, then the last (the L//N'th) use of paper will lead to a perfectly empty roll, so you go out and buy 1 new one and repeat infinity

However if L not divisble by N:
when you come to last use of paper, there won't be N left, but rather 0 < L%N < N  leftover.
-> you will need to take the remaining N - L%N you need to make up target N from elsewhere e.g. a 2nd roll of paper.
==>> IF THIS ROLL IS ALSO OF SIZE L, THEN FROM NOW ON YOU ARE GOING TO BE REMOVING PAPER, FROM THIS 2ND ROLL, IN INCREMENTS OF N_2 = (N - L%N) FOREVER:
     ===>> THIS IS THE RECURSION: if the **2nd ROLL** is evenly divisibly by (N - L%N), then it will possible to use it up exactly then refill
     ===>> HOWEVER IF IT IS NOT evenly divisble by (N - L%N) then RECURSE ONTO A 3rd ROLL WITH A UPDATED VALUE FOR N_3 = (N_2 - L%N_2) ETC ETC
 [note L stays the same throughout, all rolls are same size]
"""
def f(roll_size, effective_decrement_n, num_rolls):
    if roll_size % effective_decrement_n == 0:
        return num_rolls
    else:
        return f(roll_size, (effective_decrement_n - roll_size % effective_decrement_n), num_rolls + 1)
        
roll, decr = map(int, input().split())

print(f(roll, decr, 1))