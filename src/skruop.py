# Turn It Up!
# https://open.kattis.com/problems/skruop
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
n = int(input())
volume = 7

for _ in range(n):
    comm = input()
    if comm == "Skru op!":
        volume = min(10, volume+1)
    else:
        volume = max(0, volume-1)

print(volume)