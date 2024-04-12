# Purple Rain
# https://open.kattis.com/problems/purplerain
# TAGS: array, range sum
# CP4: 3.5a, Max 1D/2D Range Sum
# NOTES:
"""
It's a variant on Kadane's algorithm max 1d range sum

I maintain the currently largest NEGATIVE and POSITIVE sums (ie min negative and max positive)
I also maintain the INDICES OF the current ranges also (left, right)

- each time you reach a smaller negative, check if its absolute value is > best -> if so updated
- each time you reach a larger positive, check if its absolute value is > best -> if so updated

CARE! wants 1-based indexing for the result so add +1; because I forgot to add+1 to enumerate instead
"""
def kadane_var(xs):
    #bestn = float('inf') # leftover from implementation early attempt: dont need them with the current implementation O_o just compare both n and p to best overall
    currn = 0
    nl, nr = (0, 0)

    #bestp = -float('inf') # leftover from implementation early attempt: dont need them with the current implementation O_o just compare both n and p to best overall
    currp = 0
    pl, pr = (0, 0)

    best = 0
    res = (0, 0)

    for i, c in enumerate(xs):
        if c == 'B':
            x = 1
        else:
            x = -1

        if currn + x <= x:
            nr = i
            currn += x
        else:
            (nl, nr) = (i, i)
            currn = x

        if abs(currn) > best:
            res = (nl + 1, nr + 1)
            best = abs(currn)

        if currp + x >= x:
            pr = i
            currp += x
        else:
            currp = x
            (pl, pr) = (i, i)
            currp = x

        if currp > best:
            res = (pl + 1, pr + 1)
            best = currp

    return res

print(*kadane_var(input()))