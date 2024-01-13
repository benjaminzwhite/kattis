# Saving Princess Peach
# https://open.kattis.com/problems/princesspeach
# TAGS: basic, array
# CP4: 2.3c, DAT, Others
# NOTES:
N, Y = map(int, input().split())

seen = set()

for _ in range(Y):
    seen.add(int(input()))
    
for x in range(N):
    if x not in seen:
        print(x)

print(f"Mario got {len(seen)} of the dangerous obstacles.")