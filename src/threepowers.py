# Three Powers
# https://open.kattis.com/problems/threepowers
# TAGS: binary
# CP4: 2.2i, Big Integer
# NOTES:
"""
- CARE! formatting of result and escaping { and } chars in Python also
"""
while True:
    n = int(input())
    if n == 0:
        break
    
    if n == 1:
        print("{ }") # handle edge case n = 1 manually just to be safe (otherwise will have a double-emtpy-space in the f-string below)
        continue
    
    b = bin(n-1)[2:] # need to take n-1 due to how they count the "nth largest subset" because there is no empty subset allowed in the sequence
    res = (str(bd * 3**exp) for bd, exp in zip(map(int, b[::-1]), range(len(b))) if bd == 1)
    print(f"{{ {', '.join(res)} }}") # <--- NB: {{ is how you escape { in an f-string, same for }} for } escape.