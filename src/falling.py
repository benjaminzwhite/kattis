# Falling Mugs
# https://open.kattis.com/problems/falling
# TAGS: mathematics, simulation
# CP4: 3.2i, Math Simulation, Harder
# NOTES:
"""
CARE! they want you to print (n1 = smaller value, n2 = larger value) for the output 
"""
D = int(input())
flg = True

for d in range(1, int(D ** 0.5) + 1):
    if D % d == 0:
        m_minus_n = d
        m_plus_n = D // d
        two_m = m_plus_n + m_minus_n
        two_n = m_plus_n - m_minus_n
        if (two_m % 2 == 0) and (two_n % 2 == 0):
            M = two_m // 2
            N = two_n // 2
            if M ** 2 - N ** 2 == D:
                print(N, M) # need to print the smaller value, N, first and the larger value, M, second
                flg = False
                break

if flg:
    print("impossible")