# Illuminati Spotti
# https://open.kattis.com/problems/illuminatispotti
# TAGS: brute force
# CP4: 2.4a, Graph Data Structures
# NOTES:
N = int(input())

adj = []
for _ in range(N):
    adj.append(list(map(int, input().split())))

triangles = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if all((adj[i][j], adj[j][k], adj[k][i])):
                triangles += 1

print(triangles)