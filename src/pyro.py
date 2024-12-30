# Pyro Tubes
# https://open.kattis.com/problems/pyro
# TAGS: binary, brute force
# CP4: 8.7k, Three++ Components, E
# NOTES:
"""
Just brute force bitmasks.

Also, reading comprehension: for some reason I thought there were 16 but in fact there are 18 TUBES so you need MASKS up to 18 digits, not 16
"""
import sys

# Precompute - generate all 1 set bit and 2 set bit 18-digit binary numbers:
MASKS = []
for i in range(17, -1, -1): # 18 digits NOT 16 digits
    MASKS.append(2**i)
    for j in range(i - 1, -1, -1):
        MASKS.append(2**i + 2**j) # generates all 2 set bit binary numbers

d = set()
input_list = [] # CARE! need to maintain the order in which lines were added (need it for output result later -.-)
for line in sys.stdin:
    l = line.strip() # had a WA due to inputs initially, so stripping line just to be sure
    if l != '-1':
        k = int(l)
        d.add(k) # set for fast lookup
        input_list.append(k) # need to preserve order for the final result -.-

res = {}
for k in d:
    cnt = 0
    for m in MASKS:
        if (k_ := k ^ m) > k and k_ in d: # xor with the (m)ask to get whether the new number has 1,2 bitflips AND is > k, AND is in d
            cnt += 1
    res[k] = cnt

for x in input_list:
    print(f"{x}:{res[x]}")