# WFF 'N PROOF
# https://open.kattis.com/problems/wffnproof
# TAGS: greedy, interpreter
# CP4: 3.4d, Involving Sorting, H
# NOTES:
"""
Still not sure I understand what the point of all the text is, it is not used O_o 

Reading comprehension:
it's just saying that you can form a WFF with 2 WFFs and 1 KACE op, and you can always preprend any number of N ops to a WFF.

A single lowercase pqrst is also a WFF.

So what's longest string you can make?

answer: greedy -> just "reduce" 2 lowercases + 1 KACE op to form a WFF, then keep reducing this with 1 new lowercase + 1 new KACE op
then can prepend ALL the N's that occur since NNNNNNNNNNNNNNNw is a WFF.
"""
while (s := input()) != '0':

    N = 0
    KACE = []
    pqrst = []
    for c in s:
        if c in "pqrst":
            pqrst.append(c)
        elif c in "KACE":
            KACE.append(c)
        else:
            N += 1

    if not pqrst:
        # need at least one pqrst to begin "reducing" with KACE ops, or to prepend any number of N's, or both
        print("no WFF possible")
    else:
        res = ["N"] * N
        tmp = [pqrst.pop()] # need first pqrst to begin "reducing" with KACE ops
        while KACE and pqrst:
            tmp.append(pqrst.pop())
            tmp.append(KACE.pop())
        print(''.join(res + tmp[::-1]))