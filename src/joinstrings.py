# Join Strings
# https://open.kattis.com/problems/joinstrings
# TAGS: DFS
# CP4: 2.2l, List/Queue/Deque
# NOTES:
"""
I got WA/RTE on first submits, until I handled the case N=1 which I guess means there are testcases with N-1=0 queries!?!

---

CARE! with my implementation with a stack, make sure you extend the stack with the d[k] in REVERSE order since they
will then be popped in the CORRECT, FORWARD ORDER
"""
N = int(input())

LOOKUP = [None] # initialize with dummy value so that we can use 1 based indexing
for _ in range(N):
    LOOKUP.append(input())

d = [[] for _ in range(N + 10)] # +10 is sentinel

HEAD = 1 # WA/RTE - I needed to initialize this for cases where N=1 so there are N-1 = 0 -> NO QUERIES O_o
for query in range(N - 1):
    head, tail = map(int, input().split())
    d[head].append(tail)
    if query == N - 2:
        HEAD = head # THE LAST head,tail PAIR will mean that head is the overall HEAD of the string (since it's the item to which the last tail is concatenated to)

res = []
stk = [HEAD]
while stk:
    curr = stk.pop()
    res.append(LOOKUP[curr])
    stk.extend(d[curr][::-1])

print(''.join(res))