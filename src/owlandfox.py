# The Owl and the Fox
# https://open.kattis.com/problems/owlandfox
# TAGS: basic
# CP4: 3.2g, Try All Answers
# NOTES:
T = int(input())

for _ in range(T):
    s = input()
    for i, c in enumerate(s[::-1]):
        if c != '0':
            # i!=0 condition is to avoid cases where rightmost char is nonzero e.g. for input s=199 gives 198199 since s[-0:] = 199
            res = s[:-i-1] + str(int(c)-1) + s[-i:] * (i != 0)
            print(int(res))
            break