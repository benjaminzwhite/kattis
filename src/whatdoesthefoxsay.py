# What does the fox say?
# https://open.kattis.com/problems/whatdoesthefoxsay
# TAGS: basic
# CP4: 2.3d, Hash Table (set)
# NOTES:
T = int(input())

for _ in range(T):
    xs = input()
    seen = set()
    while True:
        s = input()
        if s == "what does the fox say?":
            break
        a, b, noise = s.split() #a, b, not used
        seen.add(noise)
    print(' '.join(w for w in xs.split() if w not in seen))