# Avion
# https://open.kattis.com/problems/avion
# TAGS: basic
# CP4: 6.4a, String Matching
# NOTES:
cnt = 0
res = []
for i in range(1, 6):
    s = input()
    if "FBI" in s:
        cnt += 1
        res.append(i)
        
if cnt == 0:
    print("HE GOT AWAY!")
else:
    print(*res)