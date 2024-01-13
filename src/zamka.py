# Zamka
# https://open.kattis.com/problems/zamka
# TAGS: basic, brute force
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
L = int(input())
D = int(input())
X = int(input())

mn = float('inf')
mx = -float('inf')

for x in range(L, D+1):
	tmp = sum(map(int, str(x)))
	if tmp == X:
		mn = min(mn, x)
		mx = max(mx, x)

print(mn)
print(mx)