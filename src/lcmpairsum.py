# LCM Pair Sum
# https://open.kattis.com/problems/lcmpairsum
# TAGS: mathematics, number theory, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/lcmpairsum.md
"""
T = int(input())
for testcase in range(1, T + 1):
    C = int(input())
    # -- S(n) is multiplicative; init to 1 and multiply *=
    # -- n is product of its prime factors so init to 1 also
    S_n, n = 1, 1
    for _ in range(C):
        prime, exp = map(int, input().split())
        prime_power = prime ** exp
        n *= prime_power
        S_n *= 2 * (1 - prime ** (exp + 1)) // (1 - prime) + 2 * exp * prime_power # see notes

    # -- S(n) = 2*f(n) - 2*n = 2*(f(n) - n)
    # Since we have multiplied C times i.e. performed C multiplications to get S(n) from its multiplicative
    # components S(n) = S(p1**exp1 * p2**exp2 ...) etc
    # then we have picked up C EXTRA factors of 2, relative to S(n) = 2*f(n) - 2*n = 2*(f(n) - n), so remove those
    rescaled_S_n = S_n // 2 ** C
    # now f(n) = rescaled_S_n + n
    f_n = rescaled_S_n + n
    BIGMOD = 10**9 + 7 # I forgot this and noticed just before submitting - you should do %= during calculations but Python bigint works anyways
    print(f"Case {testcase}: {f_n % BIGMOD}")