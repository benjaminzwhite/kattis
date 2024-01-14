# Railroad
# https://open.kattis.com/problems/railroad2
# TAGS: basic, graph
# CP4: 4.6f, Eulerian Graph
# NOTES:
"""
- basic Eulerian graph question
"""
X, Y = map(int, input().split())

if Y % 2 == 1:
    print("impossible")
else:
    print("possible")