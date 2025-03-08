# Ozljeda
# https://open.kattis.com/problems/ozljeda
# TAGS: mathematics, improve
# CP4: 8.7j, Other+DP 1D RSQ/RMQ
# NOTES:
"""
TODO: IMPROVE:

Code is a bit messy; also don't clearly understand WHY the pattern occurs how it does.

---

I just reduced the sequence by adding more and more terms and find that it becomes immediately periodic after the first new term O_o

So for example with the k=4 term starting values 1,3,5,7, reduce(xor, [1,3,5,7]) = 0, then reduce(xor, [3,5,7,0]) = 1, then:...
you get: intial_term=0, then 1, 3, 5, 7, 0, 1, 3, 5 ....

Same for the other -> you get a pattern of period k+1

So then, to handle the queries, instead of computing the above pattern for some huge value, just compute 1 fundamental "period"
-> here it would be [1,3,5,7,0]

Then compute the range_XOR of this:

[1, 1 ^ 3, 1^3^5, 1^3^5^7, 1^3^5^7^0] = [1, 2, 7, 0, 0] in this example <== CALL THIS period_range_q IN CODE BELOW.

NOW FINALLY, for a given l,r query you can lookup the corresponding range in the (small) period_range_q[]

---

Implementation notes:

CARE! THE GIVEN l,r ARE THE SUBSCRIPTS OF THE SEQUENCE, so to get the correct result from the period_range_q[]
you need to: -=1 l and r, to get the index within the (hypothetical huge array which you didnt compute)
and then %= (k+1) (because that is the size of the period, always) so that, instead of looking up in the "hypothetical huge array"
you can lookup the equivalent position in the periodic pattern, found in period_range_q[]

---

Brute force code used to study pattern (use the same input() code and variables as in solution below):

from functools import reduce
from operator import xor

for _ in range(200):
    curr_x = reduce(xor, A[-k:])
    A.append(curr_x)

for l, r in queries:
    res = reduce(xor, A[l - 1:r])
"""
from functools import reduce

k = int(input())
A = list(map(int, input().split()))
Q = int(input())

queries = []
for _ in range(Q):
    l, r = map(int, input().split())
    queries.append((l, r))

# See notes: you only ever end up needing 1 more value to create the fundamental period[] -> this value is the reduce(XOR, initial_terms)
last_value_to_add_to_A = reduce(lambda acc, x: acc ^ x, A)
 
period = A + [last_value_to_add_to_A] # add this value to A to get the fundamental repeating pattern

period_range_q = [period[0]]
for x in period[1:]:
    period_range_q.append(x ^ period_range_q[-1])

for l, r in queries:
    l -= 1 # CARE! the queries l, r are 1 INDEXED "SUBSCRIPTS" OF THE given x_l XOR x_l-1 XOR ....
    r -= 1 # CARE! the queries l, r are 1 INDEXED "SUBSCRIPTS" OF THE given x_l XOR x_l-1 XOR ....
    
    # the pattern is of period k+1 (k from the recurrence +1 from the single value to add, before the entire pattern repeats)
    l %= (k + 1)
    r %= (k + 1)

    # CARE! we are taking a range xor query so [r] is INCLUSIVE and [l-1] is EXCLUSIVE so that we get the sequence from x_l to x_r 
    print(period_range_q[l - 1] ^ period_range_q[r])