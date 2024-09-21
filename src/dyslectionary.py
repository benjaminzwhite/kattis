# Dyslectionary
# https://open.kattis.com/problems/dyslectionary
# TAGS: array, sorting
# CP4: 2.2f, Sorting, Harder
# NOTES:
"""
Weird input logic as I was getting used to Kattis formatting and IO commands,
probably can simplify it a lot.
"""
INPUTS = [ [] ]

while True:
    try:
        line = input()
        if line == "": # start a new list of lines
            INPUTS.append([])
        else: # append to existing list of lines
            INPUTS[-1].append(line)
    except EOFError:
        break
        
for i, xs in enumerate(INPUTS):
    words = sorted(xs, key=lambda x: (x[::-1], len(x)))
    WIDTH = max(len(x) for x in words)
    for word in words:
        print(f"{word:>{WIDTH}}") # they want you to right justify for some reason O_o
    
    if i != len(INPUTS) - 1:
        print()