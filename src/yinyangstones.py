# Yin and Yang Stones
# https://open.kattis.com/problems/yinyangstones
# TAGS: logic, game, proof
# CP4: 1.4h, Easy
# NOTES:
"""
-The 2 operations involve taking a quantity Q+1 of one stone and Q of the other to produce 1 stone of the first type
-Therefore every operation removes Q of BOTH TYPES OF STONE
-Since we want to end with 1 of each type and can only remove the same amount, Q for some value of Q, of stones each step
 then the initial state must have same number of white and black stones
-So |W|==|B| is necessary.
-It is also sufficient:
 for any arrangement with |W|==|B|, put your finger on any W stone. There are |W-1|+|B| remaining stones i.e. excess of +1 B, so you can
 perform the reduction immediately on those, to leave 1 B stone.
"""
s = input()

if s.count('W') == s.count('B'):
    print(1)
else:
    print(0)