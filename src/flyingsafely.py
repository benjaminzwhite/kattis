# Flying Safely
# https://open.kattis.com/problems/flyingsafely
# TAGS: basic, graph
# CP4: 2.4a, Graph Data Structures
# NOTES:
"""
Troll question - it's a connected graph so any tree will have n-1 edges mimimum to connect all vertices.

All the input data apart from n (number of cities to connect) is not needed.
"""
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    for _ in range(m):
        input()
    
    print(n - 1)