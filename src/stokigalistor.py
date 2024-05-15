# Messy lists aka stokigalistor
# https://open.kattis.com/problems/stokigalistor
# TAGS: basic, sorting
# CP4: 2.2e, Sorting, Easier
# NOTES:
N = int(input())

xs = list(map(int, input().split()))

cnt = 0
for x, sor_x in zip(xs, sorted(xs)):
    if x != sor_x:
        cnt += 1
        
print(cnt)