# Halting After All
# https://open.kattis.com/problems/haltingafterall
# TAGS: brute force, binary
# CP4: 0, Not In List Yet
# NOTES:
"""
Quite frustrating exercise:

1/ it seems to be a golden rule of all interpreter/state machine type problems/exercises that they cannot make a clear explanation with
all the stuff in the right place. Here for example it talks about what the machine does IF it encounters a particular <s,i,t,o,d> tuple
but NOT what happens if it doesnt happen - it seems that *all possible s,i pairs are always present* but this is basically impossible to debug
2/ you have to read all over the place to understand what the head pointer is doing
3/ due to reading comprehension, in my first submission I was looking at:

STATES[(state, head_idx)]

when in fact you are supposed to be looking at the "MEMORY_TAPE AT INDEX: head_idx"

i.e. STATES[(state, memory_tape[head_idx])]

but amazingly the first 4-5 testcases pass with this *wrong* interpretation, so it is even more confusing to debug

---

After the comments above, in the end it's just a brute force:

I tried implementing first with itertools product([0,1], repeat=L) but this doesn't work: WHY is quite interesting actually;
the reason it fails is because the dynamics of the states can involved SETTING memory_tape INDICES THAT ARE > L.

-> so if you model the memory tape as a list of size L, you get run time error whenever it tries "writing to tape" at indices > L
-> so one workaround was to create, for each itertools.product, a huge list like [memory_input] + [0]*100_000 to model infinite tape
but this gets TLE of course lol

So I redesigned using bitwise so that you can access arbitrarily large "indices" i.e. bit positions in the bitwise implementation
"""
L = int(input())
S = int(input())

STATES = {}
for _ in range(2 * S):
    s, i, t, o, d = map(int, input().split())
    STATES[(s, i)] = (t, o, d)

ok = True
# TLE using product (0,1) so I use a bitwise approach instead
# NOTES: below on the correspondence between old solution: memory_tape[head_idx] and same with bitwise
for memory_tape in range(2 ** L):
    halts = False
    
    state = 0
    head_idx = 0 # "The head starts at index 0"

    for _ in range(L):
        # memory_tape[head_idx]  ---> get the head_idx'th bith of memory_tape
        # -> right shift memory_tape head_idx times, then bitwise AND
        # ( memory_tape >> head_idx ) & 1

        if (state, ( memory_tape >> head_idx ) & 1 ) in STATES:
            t, o, d = STATES[(state, ( memory_tape >> head_idx ) & 1 )]
            state = t

            # memory_tape[head_idx] = o  # <--- REIMPLEMENT THIS LOGIC WITH BITWISE STUFF:
            if o == 1:
                # want to set a bit: use bitwise OR operator
                memory_tape |= 1 << head_idx
            else:
            	# want to clear a bit: use bitwise AND operator
                memory_tape &= ~( 1 << head_idx)
            
            if d == 0:
            	# if d==0 you are supposed to shift head_idx -1,
            	head_idx -= 1
            elif d == 1:
            	# if d==1 you are supposed to shift head_idx +1,
            	head_idx += 1
            # "The head starts at index 0 and can never move left of 0"
            # so also cannot go below 0 hence the max() here
            head_idx = max(0, head_idx)

        if state == -1:
            halts = True
            break
    if not halts:
        ok = False
        break

if ok:
    print(1)
else:
    print(0)