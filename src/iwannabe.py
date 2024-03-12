# I Wanna Be The Very Best
# https://open.kattis.com/problems/iwannabe
# TAGS: sorting
# CP4: 2.3d, Hash Table (set)
# NOTES:
N, K = map(int, input().split())

xs = []
for i in range(N):
    a, d, h = map(int, input().split())
    xs.append((a, d, h, i)) # APPEND TUPLE (a,d,h,i) IN THIS ORDER SO THAT WHEN YOU RANGE OVER ATTRIBUTE 0,1,2 THE INDEX MATCHES THE TUPLE INDEX a,d,h 

seen = set()
for attribute in range(3):
    xs = sorted(xs, key = lambda x: -x[attribute]) # WANT HIGHEST VALUES FOR EACH ATTRIBUTE
    for a, d, h, i in xs[:K]:
        seen.add(i)

print(len(seen))