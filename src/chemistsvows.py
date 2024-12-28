# Chemist's Vows
# https://open.kattis.com/problems/chemistsvows
# TAGS: dynamic programming
# CP4: 6.3b, DP String, Non Classic
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/chemistsvows.md
"""
REF = {'cr', 'xe', 'c', 'br', 'h', 'ta', 'lr', 'at', 'o', 'sc', 'si', 'li', 'ds', 'la', 'zr', 'se', 'rg', 'po', 's', 'mo', 're', 'lu', 'es', 'os', 'cn', 'np', 'nb', 'am', 'tm', 'w', 'pb', 'cm', 'rf', 'no', 'mt', 'na', 'pr', 'n', 'rh', 'ba', 'pt', 'au', 'sg', 'p', 'ac', 'cd', 'f', 'sm', 'k', 'cu', 'cf', 'ga', 'ra', 'ge', 'ir', 'yb', 'co', 'v', 'kr', 'ce', 'ne', 'te', 'ag', 'mg', 'pd', 'db', 'zn', 'md', 'u', 'in', 'th', 'ar', 'cs', 'fm', 'tb', 'tl', 'pa', 'ti', 'er', 'mn', 'cl', 'bh', 'be', 'rn', 'hs', 'sn', 'nd', 'bk', 'b', 'fr', 'gd', 'hf', 'bi', 'ru', 'fe', 'i', 'fl', 'ni', 'pu', 'rb', 'he', 'al', 'lv', 'dy', 'hg', 'sr', 'as', 'y', 'ho', 'sb', 'eu', 'tc', 'pm', 'ca'}

T = int(input())
for _ in range(T):
    s = input()
    
    dp = [False] * (len(s) + 10) # sentinel value
    dp[0] = s[0] in REF
    
    if len(s)>1:
        dp[1] = dp[0] and s[1] in REF or s[:2] in REF

    for i in range(2, len(s)):
        if dp[i - 1] and s[i] in REF:
            dp[i] = True
        if dp[i - 2] and s[i - 1:i + 1] in REF: # CARE! make sure you are looking BEHIND AT PREVIOUSLY COMPUTED dp VALUES FOR i' < i
            dp[i] = True

    if dp[len(s) - 1]: # can you make it to the last char in the string
        print("YES")
    else:
        print("NO")