# Undead or Alive
# https://open.kattis.com/problems/undeadoralive
# TAGS: string, regex
# CP4: 1.4c, Selection Only
# NOTES:
"""
- Probably cleaner/better to use regex than with indices and string slices
"""
s = input()

happy, sad = 0, 0

for i, c in enumerate(s):
    if c == ':':
        if s[i:i+2] == ':)':
            happy += 1
        elif s[i:i+2] == ':(':
            sad += 1
            
if happy and sad:
    print("double agent")
elif happy:
    print("alive")
elif sad:
    print("undead")
else:
    print("machine")