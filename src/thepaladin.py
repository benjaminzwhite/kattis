# The Paladin
# https://open.kattis.com/problems/thepaladin
# TAGS: dynamic programming, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/thepaladin.md
"""
n, k = map(int, input().split())

# lookup array for the rune pair costs
fst_x_snd = [[float('inf')] * 26 for _ in range(26)]
for _ in range(n):
    fst_snd, cost = input().split()
    fst = ord(fst_snd[0]) - 97 # a = 0
    snd = ord(fst_snd[1]) - 97
    fst_x_snd[fst][snd] = int(cost)

dp = [[float('inf')] * 26 for _ in range(k+5)] # k+5 is sentinel value

# See notes: LAST_INDEX and potential for off-by-one errors:
# This is the LAST_INDEX (*INCLUSIVE*) UP TO WHICH WE TRY TO PLACE THE snd_char
# e.g. in abc|dd|cba <- EVEN k=8, LAST_INDEX = 4 - 1 + (0) = 3, and indeed we will try to place snd_char in idx 1,2,3 but not 4.
# e.g. in xyz|m|zyx  <- ODD k=7, LAST_INDEX = 3 - 1 + (1) = 3, and indeed we try to place snd_char in idx 1,2,3 but not 4.
LAST_INDEX = k // 2 - 1 + (k % 2 == 1) 

for snd_position_in_palindrome in range(1, LAST_INDEX + 1):
    for fst_char_option in range(26):
        for snd_char_option in range(26):
            # try insert all pairs  (fst_char, snd_char) so that snd_char is in snd_position_in_palindrome
            extend_prev_palindrome = fst_x_snd[fst_char_option][snd_char_option] + fst_x_snd[snd_char_option][fst_char_option]
            
            # if this snd_position is ANYTHING OTHER THAN THE FIRST PAIR WE ARE PLACING e.g. if position > 1
            # then we need to add the dp cost of the growing palindrome to this position also, that ENDS WITH the fst_char
            if snd_position_in_palindrome > 1:
                extend_prev_palindrome += dp[snd_position_in_palindrome-1][fst_char_option]
            
            dp[snd_position_in_palindrome][snd_char_option] = min(dp[snd_position_in_palindrome][snd_char_option], extend_prev_palindrome)

# See notes: FOR EVEN STRINGS, YOU MUST MODIFY DP OPTIONS SO THAT THEY MUST HAVE A CENTRAL DOUBLE PAIR
# I do this by adding, to each dp cost ending with snd_char, the cost of the double pair (snd_char, snd_char)
# This cost will be INF (in the fst_x_snd array) if the pair doesn't exist, so this step will assign dp = INF to any results which
# cannot be made to "end-in-the-middle" with any double char pair
# e.g. if best result up to this step is abc|d but (d, d) does not exist, then abc|dd|cba is NOT in fact a valid option, so goes back up to INF
if k % 2 == 0:
    for snd_char_option in range(26):
        dp[LAST_INDEX][snd_char_option] += fst_x_snd[snd_char_option][snd_char_option]

# The result is the min total cost having reached the LAST_INDEX
res = min(dp[LAST_INDEX])

# UPDATE: noticed while testing my solution before submitting:
# My approach doesn't handle the case where k=2
# --> Just need to look for min cost of all (char, char) pairs in this case
if k == 2:
    for snd_char_option in range(26):
        res = min(res, fst_x_snd[snd_char_option][snd_char_option]) # i.e. check min cost among: ('a','a'), ('b','b'), ...., ('z','z')

# CARE! make sure to print -1 if res is INF, corresponds to no valid solution after the dp calculation
print(res if res < float('inf') else -1)