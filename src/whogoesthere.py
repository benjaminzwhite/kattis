# Who Goes There?
# https://open.kattis.com/problems/whogoesthere
# TAGS: array
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
CARE! there is the possibility, with my implementation, that there are MORE PLACES than teams that want to go
-> so if you just check "while n" you might get infinite loop if all the xs are == 0
-> so i check if any(x > 0 ...) each while loop

Implementation note:

Obviously this is not a very efficient/elegant way but I left it to show approach does not TLE because input size is small.
You can instead, for ex, count once how many distinct values of x have x>0, say cnt = 17.
Then your while loop is while n > 0 and cnt > 0.
Then each time you do xs[i] -= 1, you check if this xs[i] reached 0; if yes then you cnt -= 1 (while loop stops when cnt == 0)
"""
n, m = map(int, input().split())

xs = []
for _ in range(m):
    xs.append(int(input()))

res = [0] * m
i = 0
while n and any(x > 0 for x in xs):
	if xs[i] > 0:
		res[i] += 1
		xs[i] -= 1
		n -= 1
	i = (i + 1) % m

for x in res:
	print(x)