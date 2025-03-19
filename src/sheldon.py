# Sheldon Numbers
# https://open.kattis.com/problems/sheldon
# TAGS: mathematics, combinatorics, binary, brute force
# CP4: 5.2e, Number Systems/Seqs
# NOTES:
"""
Generate all compatible binary numbers combinatorially:

0) for each binary string length L (i.e. 1,2,3,4... => 1,0 / 00,01,10,11/ etc)  [lower and upper range: bin(low), bin(high) inclusive]
1) Pick the A-unit size to be 1,2,3....L (1 since need at least one occurence of A)
2) Pick the B-unit size to be 0,1,....
3) Try satisfy the "packing conditions": 2 options:
3)1) ABAB = L -> need L % (A+B) == 0
3)2) ABABA = L -> need L % (A+B) == A
4) check that the resulting valid string, converted to int, is within low <= x <= high; if so cnt += 1 

---

Implementation notes: 

For the step 4) update:

better to just append all x's to candidates[] as you generate them then take set() to avoid duplicates, rather than track cnt += 1, 
because there are multiple ways of generating the same final x value

e.g. A=1,2,3 and B=0 and L = 3 all lead to 111,111,111] and adjusting the cnt +/- duplicates is tricky
"""
low, high = map(int, input().split())

L_min = len(bin(low)[2:])
L_max = len(bin(high)[2:])
candidates = []
for L in range(L_min, L_max + 1):
    for A in range(1, L + 1):
        for B in range(L + 1):
            q, r = divmod(L, A + B)
            if r == 0:
                x = (A * '1' + B * '0') * q # case with ABABAB ending on B
                candidates.append(int(x, 2))
            if r == A:
                x = (A * '1' + B * '0') * q + A * '1' # case with ABABABA ending on A
                candidates.append(int(x, 2))

res = sum(low <= x <= high for x in set(candidates))

print(res)