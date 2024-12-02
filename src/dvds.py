# DVDs
# https://open.kattis.com/problems/dvds
# TAGS: logic, greedy
# CP4: 3.4f, Non Classical, Harder
# NOTES:
"""
Basically start looking for element 1, then element 2... each time you see an element that is NOT current "target", then it must be moved at least once.
Since you can always find a way to move the out of place elements exactly once, then the result is just +=1 for each such mismatched element

Example: (above what I mean is that e.g. 15324 -> 1 is ok [curr target goes from 1 to 2 now], then 5,3 NOT OK,
then 2 is ok [curr target goes from 2 to 3 now], then 4 is not)

-> The out of place elements 5,3,4 can be removed in the order 3,4,5 so that you know the final order will be 1,2,3,4,5
"""
k = int(input())

for _ in range(k):
    n = int(input())
    xs = map(int, input().split())
    curr = 1
    res = 0
    for x in xs:
        if x != curr:
            res += 1
        else:
            curr += 1
    print(res)