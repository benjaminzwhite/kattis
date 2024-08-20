# Toilet Seat
# https://open.kattis.com/problems/toilet
# TAGS: interpreter
# CP4: 1.6f, Real Life, Medium
# NOTES:
s = input()

prev1, prev2, prev3 = s[0], s[0], s[0]
commands = s[1:]

w1, w2, w3 = 0, 0, 0

for c in commands:
    # way 1 - When you leave, always leave the seat up
    if prev1 != c:
        w1 += 1
    if c != 'U':
        w1 += 1
    prev1 = 'U'

    # way 2 - When you leave, always leave the seat down
    if prev2 != c:
        w2 += 1
    if c != 'D':
        w2 += 1
    prev2 = 'D'

    # way 3 - When you leave, always leave the seat as you would like to find it
    if prev3 != c:
        w3 += 1
    prev3 = c

print(w1)
print(w2)
print(w3)