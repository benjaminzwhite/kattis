# Daylight Saving Time
# https://open.kattis.com/problems/dst
# TAGS: datetime
# CP4: 1.6i, Time, Harder
# NOTES:
N = int(input())

for _ in range(N):
    sign, D, H, M = input().split() 
    D, H, M = map(int, (D, H, M))

    if sign == 'F':
        t = H * 60 + M
        new_t = t + D
        new_h, new_m = divmod(new_t, 60)
        new_h %= 24
        print(new_h, new_m)
    else:
        t = H * 60 + M
        new_t = t - D
        new_h, new_m = divmod(new_t, 60)
        new_h %= 24
        print(new_h, new_m)