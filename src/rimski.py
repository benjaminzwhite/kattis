# Rimski
# https://open.kattis.com/problems/rimski
# TAGS: array, greedy, improve
# CP4: 1.6j, Roman Numerals
# NOTES:
"""
TODO: IMPROVE

I find that LXXI is the only case where my logic doesnt work, I wonder if there is a fully general approach
(that does not require hardcoding this specific case)
"""
s = input()

if s == "LXXI": # only value that doesnt work with below logic: since you get prefix LXX with suffix I -> LXIX, when in fact prefix LX suffix XI leads to better result: XL+IX result
    print("XLIX")

else:   
    for i, c in enumerate(s):
        if c in {'I', 'V'}:
            # first occurence of non XLC char:
            prefix = s[:i]
            suffix = s[i:]
            
            # always makes sense to flip 60 to 40 first if possible
            if (prefix == "LX"):
                prefix = "XL"
            
            # XXXI -> XXIX if suffix == I
            if (suffix == 'I') and (prefix[-1] == 'X'):
                res = prefix[:-1] + 'IX'
                print(res)
                break
            elif (suffix == 'VI'):
                res = prefix + 'IV'
                print(res)
                break
            else:
                print(prefix + suffix)
                break

        if (i == len(s) - 1):
            if s == "LX":
                print("XL")
            else:
                print(s)