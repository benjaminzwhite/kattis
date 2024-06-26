# Ljutnja
# https://open.kattis.com/problems/ljutnja
# TAGS: mathematics, number theory, sorting
# CP4: 8.7k, Three++ Components, E
# NOTES:
"""
Don't need to binary search, can solve it analytically:

It's basically "fair division" - try to divide such that the delta between wanted and actual is as close as possible across all people
e.g. prefer remove 2,2,2,2,3 rather than 11,0,0,0,0 since sum of squares for former is < latter option

To do this, calculate the missing number of items that would be needed to reach everyones target goal; try divide this evenly by N

TRICKY PART IS THAT SOME PEOPLE MAY WANT FEWER THAN THIS INITIAL VALUE.
e.g. if one person wants 23 and you are supposed to fair divide by -57 everyone, you can't give that person "23 - 57" items since quantity would be negative

So try removing from people in increasing order, and if their wanted is < fair division amount, you remove
all their wanted THEN UDPATE THE FAIR DIVISION AMOUNT WITH "N-1" REMAINING PEOPLE

Once the person's x is >= fair division amount, then you have usual situation which can be found with q, r = divmod

=> "give amount q to (N' - r) people and q+1 to r people who get +1 extra leftovers"
   except here you are "removing/failing to give them" (bad wording lol)
"""
M, N = map(int, input().split())

xs = []
for _ in range(N):
    xs.append(int(input()))

xs = sorted(xs)

missing = sum(xs) - M
res = 0
q, r = divmod(missing, N)
for x in xs:
    if x < q:
        missing -= x
        res += x * x
        N -= 1
        q, r = divmod(missing, N)
    else:
        res += q**2 * (N - r) + (q + 1)**2 * r
        break

print(res)