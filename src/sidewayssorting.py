# Sideways Sorting
# https://open.kattis.com/problems/sidewayssorting
# TAGS: array, sorting
# CP4: 2.2e, Sorting, Easier
# NOTES:
first = True

while True:
    if not first:
        print()
    first = False
    
    r, c = map(int, input().split())
    if r == 0:
        break
    
    xs = []
    for _ in range(r):
        xs.append(input())
        
    res = sorted((col for col in zip(*xs)), key=lambda x: ''.join(x).lower())
    for row in zip(*res):
        print(''.join(row))