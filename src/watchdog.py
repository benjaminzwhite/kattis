# Watchdog
# https://open.kattis.com/problems/watchdog
# TAGS: brute force, mathematics, geometry
# CP4: 7.2c, Circles
# NOTES:
T = int(input())

for _ in range(T):
    S, H = map(int,input().split())
    
    HATCHES = set()
    for _ in range(H):
        x, y = map(int, input().split())
        HATCHES.add((x, y))

    res = next(((X, Y) for X in range(S) for Y in range(S) for leash_size in range(S) if (X - leash_size) >= 0 and (X + leash_size) <= S and (Y - leash_size) >= 0 and (Y + leash_size) <= S and all(abs(X - x + (Y - y)*1j) <= leash_size for x, y in HATCHES) and (X, Y) not in HATCHES), ["poodle"])
    
    print(*res)