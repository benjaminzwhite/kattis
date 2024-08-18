# Word Cloud
# https://open.kattis.com/problems/wordcloud
# TAGS: array
# CP4: 1.6f, Real Life, Medium
# NOTES:
from math import ceil

test_case = 1 # this is for tracking output string format
while test_case < 20:
    W, N = map(int, input().split())
    if (W == 0 and N == 0):
        break
    
    c_max = 0
    to_process = []
    
    for _ in range(N):
        word, cnt = input().split()
        c = int(cnt)
        if c >= 5:
            c_max = max(c_max, c)
            to_process.append((word, c))
            
    to_process = sorted(to_process, key = lambda t: t[0])
    to_process.append(("DUMMY_WORD_TO_TRIGGER_END_OF_ALGO", 10**6)) # use dummy word with huge count which will cause last real word to be processed and added to total_heights
    
    total_heights = 0
    curr_row_height = 0
    curr_row_width = W
    
    for tpl in to_process:
        word, c = tpl
        P = 8 + ceil((40 * (c - 4)) / (c_max - 4))
        t = len(word)
        word_width = ceil((9 * t * P) / 16)
        if word_width <= curr_row_width: # see above re: dummy word, the last word in to_process is dummy word with c = 10**6 so ensures this step will fail, triggering processing of total heights with last real element
            curr_row_width -= word_width
            curr_row_width -= 10 # remember to add horiz space once you know that current word itself fits into this row
            curr_row_height = max(curr_row_height, P)
        else:
            total_heights += curr_row_height
            curr_row_width = W - word_width - 10 # start new row with W minus the space of the current word, minus the 10 horiz space padding
            curr_row_height = P # current word is the current highest in new row
    
    print(f"CLOUD {test_case}: {total_heights}")
    test_case += 1 # this is just for tracking the output format