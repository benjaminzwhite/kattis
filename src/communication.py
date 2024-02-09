# Jumbled Communication
# https://open.kattis.com/problems/communication
# TAGS: binary, bitmask, brute force
# CP4: 3.2g, Try All Answers
# NOTES:
def brute_force(target):
    for x in range(256):
        if (x ^ (x << 1)) % 256 == target:
            return x

n = int(input())

xs = map(int, input().split())

print(*(brute_force(x) for x in xs))