# Soft Passwords
# https://open.kattis.com/problems/softpasswords
# TAGS: basic, string
# CP4: 6.2e, String Comparison
# NOTES:
S = input()
P = input()

digits = '0123456789'

if S == P or any(S == d + P for d in digits) or any(S == P + d for d in digits) or S == P.swapcase():
    print("Yes")
else:
    print("No")