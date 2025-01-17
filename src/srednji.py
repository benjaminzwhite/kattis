# Srednji
# https://open.kattis.com/problems/srednji
# TAGS: array, nice
# CP4: 2.3h, Balanced BST (map)
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/srednji.md
"""
N, B = map(int, input().split())
xs = list(map(int, input().split()))

res = 0

# Find where the value B occurs in the input
i = xs.index(B)

# Starting left_idx to consider in first part of algorithm:
# CARE! See implementation note:
# Start with l = i - 1, SINCE WILL INIT d = {0:1} so already treated xs[i] i.e. the element B itself
# The reason you do this is because all other elements are > or < so can do if/else rather than repeatedly handle the xs == B case
l = i - 1 

d = {0:1}

# Start by moving left from the location of B (it's arbitrary choice, left/right)
left_acc = 0
while l >= 0:
    if xs[l] < B:
        left_acc -= 1
    elif xs[l] > B:
        left_acc += 1
    d[left_acc] = 1 + d.get(left_acc, 0)
    l -= 1

# Now move right from the value B and count the "pairs" that define valid intervals
right_acc = 0
while i < N:
    # CARE! dont do IF/ELSE naively beacuse you need to NOT INCREASE right_acc for i=i, i.e. when you start out xs[i] == B, so DONT CHANGE right_acc here
    if xs[i] > B:
        right_acc -= 1 # I use the "reverse encoding" of right_acc
    elif xs[i] < B:
        right_acc += 1
    res += d.get(right_acc, 0)
    i += 1

print(res)