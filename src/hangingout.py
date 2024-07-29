# Hanging Out on the Terrace
# https://open.kattis.com/problems/hangingout
# TAGS: basic, interpreter
# CP4: 1.4h, Easy
# NOTES:
L, num_events = map(int, input().split())

curr = 0
res = 0

for _ in range(num_events):
    s = input()
    op, val = s.split()
    val = int(val)
    if op == "enter":
        if (new := curr + val) <= L:
            curr = new
        else:
            res += 1
    else:
        curr -= val

print(res)