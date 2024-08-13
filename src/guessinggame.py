# Guessing Game
# https://open.kattis.com/problems/guessinggame
# TAGS: interpreter
# CP4: 1.6c, Game (Others), Easier
# NOTES:
l, r = 0, 11 
curr_value = -1

while True:
    s = input()
    
    if s == "right on":
        if l <= curr_value <= r:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        l, r = 0, 11
        curr_value = -1
    
    elif s == "0":
        break
    
    else:
        if s == "too high":
            r = min(r, curr_value - 1)
        elif s == "too low":
            l = max(l, curr_value + 1)
        else:
            curr_value = int(s)