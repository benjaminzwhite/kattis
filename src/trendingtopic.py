# Trending Topic
# https://open.kattis.com/problems/trendingtopic
# TAGS: queue, interpreter
# CP4: 2.2l, List/Queue/Deque
# NOTES:
"""
IMHO really hard to understand/reading comprehension. I was getting WA for ages, didn't understand why:

"The list of N most frequent words during the last 7 days must be shown given a query."
"There must be shown all words whose counter of appearances is equal to the word at position N."
"Even if the amount of words to be shown exceeds N"

--> THE (ONLY) SAMPLE TEST CASE GIVEN MAKES IT LOOK LIKE YOU ARE SUPPOSED TO
    TAKE THE N HIGHEST *VALUES* OF FREQUENCY, THEN OUTPUT ALL THE WORDS WHICH HAVE THIS FREQUENCY e.g.
    top 3:
    text 4
    corresponding 3
    file 2
    provide 2
    test 2
    words 2

--> The above testcase [and the entire sample testcase for that matter] is consistent with this interpretation, 
i.e. the 3 highest frequency VALUES are 4,3,2 so output ALL WORDS WITH THOSE FREQUENCIES

HOWEVER IT SEEMS THAT WHAT ACTUALLY IS BEING ASKED IS:
"while you have not printed >= N words on screen, print all words with next highest frequency"

So basically for each n:
you print all the words with 1st highest frequency, decrement "n_available" by how many words you just printed; if n_available <= 0 then STOP PRINTING

---

Implementation notes:

Solution probably isn't optimal, I kept adding stuff because I didn't understand why I was getting WA (see comment above)
"""
from collections import deque

days = deque([])
cnt = {}

while True:
    try:
        l = input()
        
        if l == "<text>":
            curr_day = []
            while (l_ := input()) != "</text>":
                for word in l_.split():
                    if len(word) > 3:
                        cnt[word] = 1 + cnt.get(word, 0)
                        curr_day.append(word)
            days.append(curr_day)

        elif l.startswith("<top"):
            # update curr 7 day window
            while len(days) > 7:
                old = days.popleft()
                for w in old:
                    cnt[w] -= 1
                    if cnt[w] == 0:
                        del cnt[w]

            _, n, _ = l.split()
            n_remaining = int(n)

            print(f"<top {n}>")

            freqs = sorted(set(cnt.values()), reverse=True)
            for f in freqs:
                if n_remaining <= 0: # READING COMPREHENSION/ question is unclear
                    break
                tmp = []
                for k, v in cnt.items():
                    if v == f:
                        tmp.append(k)
                for x in sorted(tmp):
                    print(x, f)

                n_remaining -= len(tmp)

            print("</top>")

    except:
        break