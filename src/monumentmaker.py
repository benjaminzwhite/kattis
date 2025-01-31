# Monument Maker
# https://open.kattis.com/problems/monumentmaker
# TAGS: cipher, array
# CP4: 6.2a, Cipher, Harder
# NOTES:
"""
A bit of reading comprehension/trial and error trying to understand the rules (whether . separates words at end of line ? etc.)

Also have to be careful as last line is EVEN i.e. right to left it has spaces hence the code "if c not in '. '" below
(it's just performing an empty space character check, you could do isalpha() instead also.)

---

Implementation notes: use 1/0 -> 0/1 by ^ operation to toggle a binary state
"""
num_lines, _, w_max = map(int, input().split())

direction = 0 # lines alternate left to right then right to left, encode 0 as direction == left-to-right
words = []
for _ in range(num_lines):
    l = input()
    words.extend(l if direction == 0 else l[::-1])
    direction ^= 1

# CARE! Got a WA because word doesn't get processed with my approach below unless it is "followed by a ." so append a last . as dummy to do this
words.append('.') # trigger processing of last element

curr_line_width = 0
curr_word_len = 0
lines_cnt = 1
for c in words:
    if c not in '. ': # CARE! Got WA until added ' ' here also: you do not add the space chars! (they occur on last line if last line is even since will be right to left and padded with ' ')
        curr_word_len += 1
    elif c == '.':
        if (new_w := curr_line_width + curr_word_len) <= w_max:
            curr_line_width = new_w + 1
            curr_word_len = 0
        else:
            lines_cnt += 1
            curr_line_width = curr_word_len + 1
            curr_word_len = 0

print(lines_cnt)