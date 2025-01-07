# Tired Terry
# https://open.kattis.com/problems/tiredterry
# TAGS: array
# CP4: 8.7j, Other+DP 1D RSQ/RMQ
# NOTES:
"""
The only tricky thing is understanding inclusive i range, see below for how to initialize curr sleep count:

In my implementation, curr is init with the length_p_string BEFORE i=n (since we double ss=s+s, it's the period p BEFORE first "real" i)

Then when you enter while loop, you DECREMENT by the first item of the lookbehind, i.e. ss[i-p], and immediately incrememnt curr
by the current item ss[i] --> this means that curr is set to the CURRENT WINDOW for the i=n case, then you perform the check:
is curr < d or not, and all is OK
"""
n, p, d = map(int, input().split())
s = input()

ss = s + s # handles lookbehind/wraparound behaviour

i = n # start at end+1 of "prefix fake string", which is at index n-1 + 1 = n

# lookbehind for curr amount of sleep:
curr = sum(ss[j] == 'Z' for j in range(i - p, i)) # NOTE THIS IS *NOT* INCLUSIVE OF CURRENT i SO THAT YOU CAN ITERATE FROM i *INCLUSIVE* IN WHILE LOOP BELOW
res = 0
while i < len(ss):
    if ss[i - p] == 'Z':
        curr -= 1
    if ss[i] == 'Z':
        curr += 1
    if curr < d:
        res += 1
    i += 1

print(res)