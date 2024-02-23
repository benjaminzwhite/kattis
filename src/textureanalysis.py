# Texture Analysis
# https://open.kattis.com/problems/textureanalysis
# TAGS: set
# CP4: 6.2f, Really Ad Hoc
# NOTES:
"""
Input string always starts and ends with *, so you split on * and you will always get ['', important stuff, ''] as your split list
So then consider xs[1:-1] to ignore those 2 empty split locations at start and end.
"""
i = 0
while True:
    i += 1
    line = input()
    if line == "END":
        break
    
    xs = line.split('*')
    res = set(map(len, xs[1:-1]))
    
    if len(res) > 1:
        print(i, "NOT EVEN")
    else:
        print(i, "EVEN")