# Znanstvenik
# https://open.kattis.com/problems/znanstvenik
# TAGS: string, sorting
# CP4: 8.7c, Fast DS+Other, Easier
# NOTES:
"""
Quite unclear/hard to understand testcases due to reading comprehension:

You are supposed to move "downwards" row by row and see when the situation first occurs, but aren't allowed to go any further.
This is why the test cases have "-1" to their "obvious" answers, it's basically "what is the last row at which the condition does NOT hold"

Also, rotating inputs doesn't add anything to the exercise - would be easier to just iterate left->right rather than in columns.
---

Naive implementation is therefore to, for each column to check if all the partial columns cols[:endpoint] are distinct - e.g. by using a set:
But taking set each iteration times out.

Cleverer approach : check whenever the first "full set" occurs
-> sort the words and compare pairwise
-> any duplicate letters , if they exist, can only occur in adjacent pair words once the list is sorted
-> i.e. find the MAX COMMON PREFIX
"""
r, c = map(int, input().split())

inps = [input() for _ in range(r)]

board = []
for col in zip(*inps):
    board.append(col[::-1]) # CARE! I ADD THE COLUMNS REVERSED HERE

board.sort()

similarity = 0 # <-- basically this is the longest common prefix when you think about it
for fst, snd in zip(board, board[1:]):
    i = 0
    while i < r and fst[i] == snd[i]:
        i += 1
    similarity = max(similarity, i)

if similarity > r:
    similarity = r

print(r - similarity - 1) # CARE! -1 because of counter-intuitive exercise statement, see Notes above