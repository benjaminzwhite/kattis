# Cut the negativity
# https://open.kattis.com/problems/cutthenegativity
# TAGS: basic
# CP4: 2.4a, Graph Data Structures
# NOTES:
"""
- tagged as Graph related but basically just move through a 2nd array of rows/cols
- CARE! 1 based indexing throughout
"""
n = int(input())

m = 0 # don't need this, can just print len(res) at the end, but used for clarity
res = []

for r in range(1, n + 1): # 1 based indexing
    xs = map(int, input().split())
    for c, x in enumerate(xs, 1): # 1 based indexing
        if x == -1:
            continue
        m += 1
        res.append( (r, c, x) )
        
print(m) # requires you to print the total count/len of res
for line in res:
    print(*line)