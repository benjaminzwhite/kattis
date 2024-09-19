# Sort of sorting
# https://open.kattis.com/problems/sortofsorting
# TAGS: array, sorting
# CP4: 2.2f, Sorting, Harder
# NOTES:
first = True

while True:
    if not first:
        print()
    first = False
    
    n = int(input())
    if n == 0:
        break
    
    xs = []
    for _ in range(n):
        xs.append(input())
        
    xs = sorted(xs, key=lambda x: x[:2])
    for x in xs:
        print(x)