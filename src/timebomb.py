# Timebomb
# https://open.kattis.com/problems/timebomb
# TAGS: array, string
# CP4: 1.6m, Input Parsing (Iter)
# NOTES:
"""
I took the 0123456789 reference string and zipped each one individually into a ''.join of its 3 columns

I use this 3-column join string as the key in the dict, d, to which I associate the value corresponding to the ASCII number.
"""
d = {'******   ******': '0', '          *****': '1', '* **** * **** *': '2', '* * ** * ******': '3', '***    *  *****': '4', '*** ** * ** ***': '5', '****** * ** ***': '6', '*    *    *****': '7', '****** * ******': '8', '*** ** * ******': '9'}

inps = []
for _ in range(5):
    inps.append(input())

res = []
tmp = []
for i, c in enumerate(zip(*inps), 1):
    if i % 4 == 0: # enumerate starting at 1, every 4th column is blank and separates 2 ascii numbers
        continue
    tmp.extend(''.join(c)) # extend the current ASCII char by this column (could be first, 2nd or 3rd column of the ASCII char)
    if i % 4 == 3: # every "3rd" column of block of 4 is the final column of an ASCII number in the input, so append it now to res [] as a distinct number
        res.append(''.join(tmp))
        tmp = []

number = []
flg = True
for x in res:
    if x in d:
        number.append(d[x])
    else:
        flg = False
        break
if flg:
    n = int(''.join(number))
    if n % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!") # can merge this else into one below, but left for clarity
else:
    print("BOOM!!")