# Fibonacci Cycles
# https://open.kattis.com/problems/fibonaccicycles
# TAGS: mathematics, set
# CP4: 5.6a, Cycle Finding
# NOTES:
"""
Reading comprehension - I think the question is formulated weirdly/confusingly:

As is written, with my understanding, the answer is trivially n=2 for all inputs since F2 (you aren't allowed to say F0 and F1) 
will *always* be "the first number in the sequence of Fibonacci numbers modulo k that has a repeat at some point in the sequence"
since:

- F2 must have a repeat at some point in the sequence and 
- F2 is of course "earlier than" all other Fn = F3,F4,F5...

For example with the k=4 example, when you reach the value for n=8 it will generate F8 % k == 2 which is therefore a repeat of F2 == 2.
So with that formulation of the question, the answer is always F2.

---

Clearer reformulation - What the question actually wants is:

- Generate all Fibonacci numbers modulo k until you first obtain a remainder value that has already been seen. 
- Print the n for which that remainder PREVIOUSLY occured.
"""
Q = int(input())

for _ in range(Q):
    k = int(input())
    seen = {}
    a, b = 1, 1
    for n in range(2, 1000 + 1): # k_max is 1000
        a, b = b, a + b
        if b % k in seen:
            print(seen[b % k])
            break
        seen[b % k] = n