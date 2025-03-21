# Wimbledon
# https://open.kattis.com/problems/wimbledon
# TAGS: mathematics, combinatorics
# CP4: 0, Not In List Yet
# NOTES:
"""
Inclusion-Exclusion principle on "ALL = GOODS + BADS" 

ALL: matches with 2 players 1 umpire: sigma( product_over_i,j,k: a_i * a_j * b_k) = (a1 + a2 + a3 + ..)(a1 + a2 + a3...)(b1 + b2 + b3 + ...)
But we need to divide by 2 since "Two tennis matches are different if the sets of involved people are different."
and here so far we are treating these tuples as ordered tuples so a3,a77,b82 is counted differently from a77,a3,b82

ALL = sum(A) * sum(A) * sum(B) // 2 # divide by 2 to avoid double counting on A's

now do the BADS:

1) tuples a_i*a_j*b_k where i==j:

this is sigma( product_over_i,k: a_i**2 * b_k  ) = a_1**2 ( b1 + b2 + b3 + ...) + a_2**2 (b1+b2+b3...)
= sum(a**2 for a in A) * sum(B) // 2
CARE! again, //2 because we are double counting on A again

2) tuples a_i*a_j*b_k where i==k:

this is sigma( product_over_i,j: a_i*b_i * a_j) = a1b1 * (a1 + a2 + a3 +..) + a2b2 * (a1 + a2 + a3 ...)
= sum(a*b for a,b in A,B) * sum(A) // 2
CARE! again, //2 because we are double counting on A again

3) tuples a_i*a_j*b_k where j==k: this is the same as 2), just different indices
= sum(a*b for a,b in A,B) * sum(A) // 2
CARE! again, //2 because we are double counting on A again

Finally, by inclusion-exclusion principle:
We have counted the cases where i=j=k twice, so need to add them back:
How many are there? for i=1,2,..N we get a_i*a_i*b_i so this term is sum(a*a*b for a,b in A,B)
NOW, DO *NOT* // 2 THESE SINCE THEY ARE NOT BEING DOUBLE COUNTED
"""
N = int(input())

A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# ALL
res = sum(A) * sum(A) * sum(B) // 2 # //2 because double count

# remove BADS
# 1) tuples a_i*a_j*b_k where i==j:
res -= sum(a**2 for a in A) * sum(B) // 2 # //2 because double count

# 2) tuples a_i*a_j*b_k where i==k:
# 3) tuples a_i*a_j*b_k where j==k: this is the same as 2)
# NOTE: 2) == 3) so remove 2* the contribution of one of them:
res -= 2 * sum(a * b for a, b in zip(A, B)) * sum(A) // 2 # 2* because twice the same contribution for i==k,j==k and then //2 because double count

# Inclusion-Exclusion correction term, for the fact that we removed terms involving i==j==k twice
res += sum(a * a * b for a, b in zip(A, B))

print(res)