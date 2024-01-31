# Östgötska - Ostgotska
# https://open.kattis.com/problems/ostgotska
# TAGS: string
# CP4: 6.4a, String Matching
# NOTES:
s = input()

xs = s.split()

cnt = sum('ae' in x for x in xs)

# should do cnt >= 0.40 * len(xs) but below is for clarity
if cnt / len(xs) >= 0.40:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")