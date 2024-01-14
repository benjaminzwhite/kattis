# SMIL
# https://open.kattis.com/problems/smil
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
"""
- probably better to do with a regex
"""
s = input()

for i,x in enumerate(s):
    if x in {':',';'}:
        if s[i+1:i+2] == ')' or s[i+1:i+3] == '-)':
            print(i)