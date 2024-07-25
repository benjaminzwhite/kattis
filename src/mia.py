# Mia
# https://open.kattis.com/problems/mia
# TAGS: basic
# CP4: 1.4f, Function
# NOTES:
"""
No idea what I was doing with this complex implementation - late night solving I guess O_o
"""
while True:
    s0, s1, r0, r1 = map(int, input().split())
    
    if (s0, s1, r0, r1) == (0, 0, 0, 0):
        #print("Tie.") <- got WA for printing tie for the 0,0,0,0 input, should NOT print just end program instead
        break
    
    def score(x1, x2):
        if (x1, x2) in {(1, 2), (2, 1)}:
            return 100_000 # arbitrary big numbers to impose scoring order (instead of creating a lookup table or max/sort-with-key)
        elif x1 == x2:
            return x1 * 10_000 # see above comment; here best pair is 6,6 so returns score of 66_000 which is < 100_000; worst is 1,1 * 10_000
        else:
            return (10 * max(x1, x2)) + min(x1, x2) # see above comment; here best non pair is 6,5 so returns 65 which is < 1,1 * 10_000 above
            
    score1 = score(s0, s1)
    score2 = score(r0, r1)
    
    if score1 > score2:
        print("Player 1 wins.")
    elif score1 == score2:
        print("Tie.")
    else:
        print("Player 2 wins.")