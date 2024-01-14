# Speed Limit
# https://open.kattis.com/problems/speedlimit
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
while True:
	n = int(input())
	if n == -1:
		break

	prev_time = 0
	res = 0
	for _ in range(n):
		s, t = map(int, input().split())
		res += s * (t - prev_time)
		prev_time = t

	print(res, "miles")