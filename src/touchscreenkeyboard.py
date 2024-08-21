# Touchscreen Keyboard
# https://open.kattis.com/problems/touchscreenkeyboard
# TAGS: array
# CP4: 1.6g, Real Life, Harder
# NOTES:
keyboard = """qwertyuiop
asdfghjkl
zxcvbnm"""

REF = {}

for r, row in enumerate(keyboard.splitlines()):
    for c, cell in enumerate(row):
        REF[cell] = (r, c)

def dist(char1, char2):
    r1, c1 = REF[char1]
    r2, c2 = REF[char2]
    return abs(r1 - r2) + abs(c1 - c2)

def total_dist(word1, word2):
    return sum(dist(char1, char2) for char1, char2 in zip(word1, word2))

t = int(input())

for _ in range(t):
    ref_word, l = input().split()
    l = int(l)
    
    res = []
    
    for _ in range(l):
        curr_word = input()
        curr_d = total_dist(curr_word, ref_word)
        res.append((curr_word, curr_d))
        
    res = sorted(res, key = lambda x: (x[1], x[0]))
    
    for tpl in res:
        print(*tpl)