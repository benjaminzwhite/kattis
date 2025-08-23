# Avoidland
# https://open.kattis.com/problems/avoidland
# TAGS: greedy
# CP4: 3.4a, Greedy (Classical)
# NOTES:
n = int(input())

rs = []
cs = []
for _ in range(n):
    r, c = map(int, input().split())
    rs.append(r)
    cs.append(c)

# In the final state, the row values should be {1,2,3,4}
# If they are currently {1,1,4,4} for ex then need {0,+1,-1,0} changes i.e. 2 moves
# Same for cols (moves are independent in r- and c-axis)
# -> minimal number of moves is when rows/cols are "as close as possible" to 1,2,3,4 already i.e. process them in ascending order
rs.sort()
cs.sort()

res = sum(abs(r - i) + abs(c - i) for i, (r, c) in enumerate(zip(rs, cs), 1)) # CARE! 1-based indexing

print(res)