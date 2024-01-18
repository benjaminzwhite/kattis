# Missing Numbers
# https://open.kattis.com/problems/missingnumbers
# TAGS: basic
# CP4: 1.4i, Still Easy
# NOTES:
n = int(input())

xs = {int(input()) for _ in range(n)}

if (M := max(xs)) == n:
    print("good job")

else:
    for x in range(1, M + 1):
        if x not in xs:
            print(x)