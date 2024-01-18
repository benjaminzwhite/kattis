# Blueberry Waffle
# https://open.kattis.com/problems/blueberrywaffle
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
r, f = map(int, input().split())

if round(f/r) % 2 == 1:
	print("down")
else:
	print("up")