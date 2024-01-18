# Modulo
# https://open.kattis.com/problems/modulo
# TAGS: basic
# CP4: 5.3i, Modular Arithmetic
# NOTES:
seen = set()

for _ in range(10):
	n = int(input())
	seen.add(n % 42)

print(len(seen))