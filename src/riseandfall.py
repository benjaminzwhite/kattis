# Rise and Fall
# https://open.kattis.com/problems/riseandfall
# TAGS: greedy
# CP4: 0, Not In List Yet
# NOTES:
T = int(input())
for _ in range(T):
    s = input()
    peak_passed = False # 123356778|543... <-- | is the peak up to which the prefix is non-decreasing 12335...
    res = [s[0]]
    L = len(s)
    for i in range(1, L):
        res.append(s[i])
        if not peak_passed and s[i - 1] > s[i]:
            peak_passed = True
        elif peak_passed and s[i - 1] < s[i]:
            res.pop()
            break

    res.append((L - len(res)) * res[-1])
    print(''.join(res))