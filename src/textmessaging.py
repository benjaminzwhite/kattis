# Text Messaging Outrage
# https://open.kattis.com/problems/textmessaging
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
Greedy sorting - assign 1 key press to the num_keys_available largest frequencies, then repeat with 2 key presses then 3 etc.
"""
T = int(input())

for case_number in range(1, T + 1):
    num_letters_per_key, num_keys_avail, alph_size = map(int, input().split())

    xs = map(int, input().split())
    xs = sorted(xs, reverse=True)

    i = 0
    res = 0
    curr_key_presses = 1
    while i < len(xs):
        for _ in range(num_keys_avail):
            if i >= len(xs):
                break
            res += xs[i] * curr_key_presses
            i += 1
        curr_key_presses += 1

    print(f"Case #{case_number}: {res}")