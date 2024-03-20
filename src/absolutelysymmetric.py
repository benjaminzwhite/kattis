# Absolutely Symmetric
# https://open.kattis.com/problems/absolutelysymmetric
# TAGS: mathematics, logic, proof
# CP4: 0, Not In List Yet
# NOTES:
"""
Consider two elements A_ij and A_ji of A:

1 In any K-decomposition of A into k absolutely symmetric matrices X_1,X_2,...X_k then the difference between A_ij and A_ji must equal the sum
  of the differences of (X_1, X_2...)_ij and (X_1, X_2...)_ji.

2 In turn, the differences of e.g. (X_1)_ij and (X_1)_ji must be EVEN (by the requirement of absolutely symmetric matrix: 
  their absolute values are identical so their values are either identical (so (X_1)_ij - (X_1)_ji == 0, EVEN) or they are
  negatives of eachother, in which case (X_1)_ij - (X_1)_ji == 2 * (X_1)_ij, EVEN also).

3 By 2, and 1, for A to have such a K-decomposition therefore it must ITSELF have all its transpose paired elements A_ij, A_ji have an EVEN difference since
  in any K-decomposition these pairwise differences will be obtained as a sum of even differences (see 2).

4 The necessary condition 3 is sufficient and allows for a k=2 construction in all cases: for each tranpose pair of elements A_ij, A_ji consider their
  average A_ij + A_ji // 2. (By assumption this is integer valued since A_ij and A_ji have same parity) 
  Create the first X_1 matrix with these average values.
  Then, take the delta values A_ij - average, A_ji - average, and assign these to a second X_2 matrix.
  By construction the X1+X2 decomposition satisfies the requirements. Since A itself does not satisfy the absolutely symmetric requirement, then k=1
  decomposition does not exist so k=2 is minimal as required. 

5 !!! HOWEVER !!! There is a degenerate case where the delta values of 4 above are ALL 0 for all pairs A_ij, A_ji -> this corresponds to A itself being a symmetric matrix in the usual sense.
  Then a k=1 "decomposition" is possible; it's just A itself.

UPDATE STEP -5-
Actually (see Implementation note below): for 5 the input matrix itself can be Symmetric or Absolutely Symmetric already and will satisfy requiremnets so k=1 suffices.

---

Implementation note:

Got a WA on first submits - I was getting 1 test wrong after first 30. After debugging, I was failing on case where input matrix A itself
satisfies the requirements; the way I was checking for whether A is absolutely symmetric was wrong:

I used this testcase to debug:
0 -1
1 0
"""
n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

A_itself_is_absolutely_symmetric = True # see 5 in proof above; assume A is ABSOLUTELY symmetric until you see at least one pair A_ij != A_ji
parity_flag = True # see 3 in proof above; assume A has all its pairs A_ij, A_ji of same parity until see otherwise

X1 = [[0] * n for _ in range(n)] # will store our "average/baseline" values, see 4 in proof above
X2 = [[0] * n for _ in range(n)] # will store our "delta" values, see 4 in proof above

for i in range(n):
    for j in range(i, n):
        if A[i][j] != A[j][i] and A[i][j] != -A[j][i]:
            A_itself_is_absolutely_symmetric = False
        tmp = A[i][j] + A[j][i]
        if tmp % 2 != 0:
            parity_flag = False
            break
        average = tmp // 2
        delta1, delta2 = A[i][j] - average, A[j][i] - average
        X1[i][j], X1[j][i] = average, average
        X2[i][j], X2[j][i] = delta1, delta2

if not parity_flag:
    print(-1)
elif A_itself_is_absolutely_symmetric:
    print(1)
    for row in A:
        print(*row)
else:
    print(2)
    for row in X1:
        print(*row)
    for row in X2:
        print(*row)