# Permutation Code
# https://open.kattis.com/problems/permcode
# TAGS: cipher
# CP4: 1.6l, Cipher, Medium
# NOTES:
"""
- Just lots of reading and do-as-they-say.
- Left comments in code itself, since easier to follow in-place.
"""
while True:
    x = int(input())
    if x == 0:
        break

    S = input()
    P = input()
    C = input()

    indices_S = {x:i for i,x in enumerate(S)} # performance: to avoid repeated lookups for S.index(something) (but don't really need to, since input S is len < 32)

    # Step 1:
    n = len(C)
    d = int(n**1.5 + x) % n

    # Step 2:
    # "Set C[d] to be the symbol in S whose position is the same as the position of M[d] in P."
    # -> C[d] = S[X] where X = P.index(M[d])
    # -> So for given example:
    #    C = ETAEAA, d=2
    #    we must have that C[d=2] = 'A' will be equal to S[P.index[M[2]]]
    # 
    # -> Now, since 'A' appears only once in S, the corresponding ^^^ index will be uniquely defined so we find that:
    # S[1] => 'A' therefore 'A' <= S[P.index[M[2]]]
    #                              S[      1      ]
    # i.e. 1 = P.index[M[2]]
    # 
    # So now going to P:
    # P[1] = 'E'
    # So that if 1 = P.index(something) then something = 'E'
    # so here, M[2] = 'E'
    M = [P[indices_S[C[d]]]] * n # initialize array with the value for d e.g. for example we have now set all of M to = M[2] = 'E'

    # Step 3:
    # For each j!=d in 0->n-1 set C[j] to be the symbol in S whose position is the value 
    # obtained by xor-ing the position of M[j] in P with the position of M[(j+1) % n] in S.
    # -> Since we only know M[d], this must be the start point for decrypt so M[d] is our "M[(j+1)%n]"
    # -> Since we can calculate M[j] from M[j+1], iterate DOWNWARDS from d:
    for j in range(d-1, -1, -1):
        # 1: S.index( C[j] ) =  LEFT xor RIGHT where:
        # 2: LEFT = P.index( M[j] )
        # 3: RIGHT = S.index( M[(j+1) % n])
        step_one = indices_S[C[j]]
        step_three = indices_S[M[(j+1) % n ]]
        step_two = step_one ^ step_three
        # step_two = P.index( M[j] )
        M[j] = P[step_two]

    for j in range(n-1, d, -1):
        step_one = indices_S[C[j]]
        step_three = indices_S[ M[(j+1) % n]]
        step_two = step_one ^ step_three
        M[j] = P[step_two]

    print(''.join(M))