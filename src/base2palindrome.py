# Base-2 Palindromes
# https://open.kattis.com/problems/base2palindrome
# TAGS: logic, string, improve
# CP4: 9.cons, Construction
# NOTES:
"""
TODO: IMPROVE: try to get a shorter way of doing it

---

Pattern is:

1xxxxx|0/1|xxxxx1 for odd number of digits
1xxxxx|xxxxx1 for even number of digits

-> need leading 1 (hence last digit 1 by palindrome property) to avoid leading 0s (not allowed)
-> then the xxxx should be all binary strings in ascending order:
-> if e.g. there are d=9 digits in the target string you have 1xxx|0/1|xxx1 a total of 3 x's to fix in the prefix part
   >>> SO YOU GENERATE ALL BINARY STRINGS b OF LENGTH UP TO 3 i.e. 000,001,010,011,100,101,110,111
   -> Then the tail is the [::-1] of the prefix
-> If d is ODD the centre |0/1| is also to be fixed but is independent of the xxxx part:
   DO THE 0 VALUE FIRST since will lead to numerically smaller terms being created first
"""
RES = [0, 1, 3, 5, 7, 9, 15] # initialize all the values up to d=4 digits; it says the 1st base2 palindrome is 1 so use 1-based indexing.

d = 5
while len(RES) < 50_010:
    for b in range(2**(d // 2 - 1)): # generate all the binary strings to fit into the xxxxx part
        prefix = '1' + str(bin(b)[2:].zfill(d // 2 - 1)) # zfill so that you have the correct padding i.e. number of places to make up a total of d digits
        if d % 2 == 1: # handle the case when d is odd: have a centre value that can be 0 or 1
            # 1xxxxx|0/1|xxxxx1
            res1 = prefix + '0' + prefix[::-1]
            RES.append(int(res1, 2))
            res2 = prefix + '1' + prefix[::-1]
            RES.append(int(res2, 2))
        else:
            # 1xxxxx|xxxxx1
            res = prefix + prefix[::-1]
            RES.append(int(res, 2))
    d += 1
    
M = int(input())

print(RES[M])