# A Furious Cocktail
# https://open.kattis.com/problems/cocktail
# TAGS: greedy, sorting
# CP4: 3.4b, Involving Sorting, E
# NOTES:
N, T = map(int, input().split())

xs = []
for _ in range(N):
    xs.append(int(input()))
    
xs = sorted(xs, reverse=True)

min_close = float('inf')
flg = True
for i, x in enumerate(xs):
    curr_open = i * T
    if min_close <= curr_open:
        flg = False
    min_close = min(min_close, curr_open + x)

if flg:
    print("YES")
else:
    print("NO")