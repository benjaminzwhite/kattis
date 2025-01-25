# Highway to Mount Fansipan
# https://open.kattis.com/problems/highwaytomountfansipan
# TAGS: mathematics, combinatorics, improve
# CP4: 8.7h, Mathematics+Other	
# NOTES:
"""
TODO: IMPROVE: I think my implementation can be improved - here I started working with dicts but I have to copy them around and modify,
probably easier to have some kind of table to store things

---

It's basically combinatorics, but there are some implementation details and logic behavior to check (I got a RTE on first submit):
I left comments locally in code below.
"""
from copy import deepcopy

BIGMOD = 10**9 + 7

T = int(input())
for _ in range(T):
    num_horiz_words = int(input())
    lengths_of_horiz_words_required = list(map(int, input().split()))
    d_how_many_candidate_words = int(input())

    POSSIBLE_VERTICAL_WORDS = [] # don't know why I'm UPPERCASING this O_o
    initial_letters_and_their_lengths = {}

    for _ in range(d_how_many_candidate_words):
        curr_word = input()
        curr_word_len = len(curr_word)
        if curr_word_len == num_horiz_words:
            # this could potentially be a VERTICAL word since it has right number of chars
            POSSIBLE_VERTICAL_WORDS.append(curr_word)

        fst = curr_word[0]
        if fst not in initial_letters_and_their_lengths:
            initial_letters_and_their_lengths[fst] = {}

        if curr_word_len not in initial_letters_and_their_lengths[fst]:
            initial_letters_and_their_lengths[fst][curr_word_len] = 0
        initial_letters_and_their_lengths[fst][curr_word_len] += 1

    # try all POSSIBLE_VERTICAL_WORDS
    res = 0
    for poss_vertical in POSSIBLE_VERTICAL_WORDS:
        # can no longer use this word, so decrement dict info -> copy the dict so modify locally
        d = deepcopy(initial_letters_and_their_lengths)
        # CARE! above, make sure you deepcopy and not just copy else will get WA (silly mistake)

        d[poss_vertical[0]][num_horiz_words] -= 1 # the length of this word is always num_horiz_words since we are trying all possible vertical words
        # CARE! I got a run time error RTE : I think it's because I forgot to del the key if the above -=1 step sets the value to 0
        if d[poss_vertical[0]][num_horiz_words] == 0:
            del d[poss_vertical[0]][num_horiz_words]

        cnt = 1 # multiplicative accumulator, will become 0 if no words are possible at any step
        for horiz_first_char, target_len in zip(poss_vertical, lengths_of_horiz_words_required):
            # e.g. here if poss_vertical is "icpc", what the zip() is doing is:
            # i ----> target_len is 6 in this row, and horiz_first_char is i
            # c ----> target_len is 3 in this row, and horiz_first_char is c etc.etc.
            # p
            # c
            
            curr_char_cnt = 0
            if horiz_first_char in d and target_len in d[horiz_first_char]:
                curr_char_cnt = d[horiz_first_char][target_len]

            if curr_char_cnt > 0:
                # if curr_char_cnt then there was a valid word that fits here horizontally so need to update d to 
                # account for the fact that we are using "it" --> NOTE THAT IT DOESNT MATTER SPECIFICALLY WHICH WORD,
                # just that you have used A WORD that begins with first_char and has length = target_len
                # e.g. cow and cat -> instead of having 2 words beginning with c and of len 3, you now only have 1 WHETHER YOU "ACTUALLY" 
                # put cow OR cat here -> it doest matter combinatorially ofc, just that you have 1 fewer option without repetition
                # if you need, in future steps, another word starting with c and of len 3.
                # --------------
                # remove 1 word that has that horiz first char and that target len, since it cant be used anymore
                d[horiz_first_char][target_len] -= 1
                if d[horiz_first_char][target_len] == 0:
                    del d[horiz_first_char][target_len]
            cnt *= curr_char_cnt
        res = (res + cnt) % BIGMOD

    print(res % BIGMOD)