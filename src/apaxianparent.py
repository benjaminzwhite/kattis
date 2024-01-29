# Honour Thy (Apaxian) Parent
# https://open.kattis.com/problems/apaxianparent
# TAGS: basic, string
# CP4: 6.2f, Really Ad Hoc
# NOTES:
y, p = input().split()

if y.endswith("ex"):
    print(y + p)
elif any(y.endswith(v) for v in "aeiou"):
    print(y[:-1] + "ex" + p)
else:
    print(y + "ex" + p)