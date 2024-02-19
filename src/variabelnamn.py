# Variable Names
# https://open.kattis.com/problems/variabelnamn
# TAGS: logic, nice
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
Very nice little exercise.

If you naively do the obvious approach - i.e. for each x in the input, keep looking in seen() and check if x, or 2x or 3x... has already
been used -> this times out due to large inputs.

So instead, need to maintain a more complex dictionary and updating rules: seen[x] stores the most recent multiple of x used.

Then for each x in the inputs, if it is in seen then lookup the most recent multiple that was used, then continue trying from there.
e.g. if seen[5] = 35, then start looking at 35+5 = 40 etc.

NOTE: need to store ORIGINAL VALUE OF x => x_ so that can increment with x_ rather than x (which may have been set to e.g. 35 rather than 5 now)

After this loop, update dict USING THE KEY x_ NOT x (remember x_ is the original input value and x is now the most recent mulitple of x_ that we have used)

Finally, IF THIS VALUE OF X THAT WE REACHED ITSELF IS NOT IN SEEN, then create an entry for it:
e.g. if from original x=5 we got to 35+5 = 40 , you must update seen[40] = 40 also!
"""
n = int(input())

seen = {}
# seen[3] = 12 means most recent multiple of 3 used was 12

for _ in range(n):
    x = int(input())
    x_ = x
    if x in seen:
        x = seen[x] + x_
        while x in seen:
            x += x_
    seen[x_] = x
    
    seen[x] = x # Important! Update with the value of x that you reached also!
    print(x)