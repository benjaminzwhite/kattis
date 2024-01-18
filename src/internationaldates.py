# International Dates
# https://open.kattis.com/problems/internationaldates
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
a, b, c = map(int, input().split('/'))

if a > 12:
    print("EU")
elif b > 12:
    print("US")
else:
    print("either")