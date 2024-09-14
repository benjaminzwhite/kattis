# Mjehuric
# https://open.kattis.com/problems/mjehuric
# TAGS: array, sorting
# CP4: 2.2e, Sorting, Easier
# NOTES:
"""
Original submission had break after print statement (I thought it wants to return to head of list after finding first swap,
but in fact you don't break - you do all swaps in a given initial input sequence, then repeat with updated sequence etc)

The 2 given test cases both pass the first interpretation, but fail on submit.

To see the difference between the two different interpretations of what they want, you should use test case e.g. 4 3 2 5 1
which produces 2 different outputs depending on if you break on each swap or perform all swaps on each pass.
"""
xs = list(map(int, input().split()))

go = True

while go:
    go = False
    for i in range(4):
        if xs[i] > xs[i + 1]:
            go = True
            xs[i], xs[i + 1] = xs[i + 1], xs[i]
            print(' '.join(map(str, xs)))