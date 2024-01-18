# Simon Says
# https://open.kattis.com/problems/simonsays
# TAGS: basic, string
# CP4: 6.4a, String Matching
# NOTES:
N = int(input())

for _ in range(N):
    s = input()
    if s.startswith("Simon says"):
        print(s[11:])