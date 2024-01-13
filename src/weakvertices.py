# Weak Vertices
# https://open.kattis.com/problems/weakvertices
# TAGS: graph
# CP4: 2.4a, Graph Data Structures
# NOTES:
"""
Do 3 loops: for s in range(n): for e in range(n): for m in range(n): then check if there is any way of forming a triangle
with these 3 matrix coordinates e.g. M[s][m], M[m][e], M[e][s]
"""
while True:
    n = int(input())
    if n == -1:
        break

    adj_m = [list(map(int, input().split())) for _ in range(n)] # Adjaceny matrix converted to ints etc.

    # goods contains all the GOOD vertices, i.e. ones where you can form at least one triangle:
    goods = set(s for e in range(n) for m in range(n) for s in range(n) if (len(set([s, m, e])) == 3 and adj_m[s][m] == 1 and adj_m[m][e] == 1 and adj_m[e][s] == 1))

    # Result is all the numbers in range(n) that ARE NOT IN THE ABOVE "GOODS" LIST OF VERTICES WHICH DO BELONG TO TRIANGLES
    print(*filter(lambda x: x not in goods, range(n)))