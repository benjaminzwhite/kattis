# Lucky Numbers
# https://open.kattis.com/problems/luckynumber
# TAGS: brute force, mathematics, recurrence
# CP4: 3.2a, Pre-calculate-able
# NOTES:
"""
Just build them all incrementally - note that after k = 8 -> len = 2227, then k=9,10 -> 2492,
and then from k=11 -> 2225 the len(lucky) starts falling to 0 (n=23,24,25,26: 6,3,1,0... then 0 onward)

The reason why they fall/become rarer after k=9/10 is as follows:

Building step:
Imagine you have k=3 list done, then to get 4 digit lucky number:
-Take each l from the k=3 list, and multiply l by 10 to get l_. 
-Find nearest multiple of k=4 that is >= l_ (since it has to have the same first 3 digits) and then add all multiples of
 of k = 4 WHILE STILL KEEPING THE SAME FIRST 3 DIGITS (since you know that they satisfy the lucky property for k=3)
 e.g. for k=3 and you have 105
 then moving it to k=4 you have 1050 which %4 is 2
 So multiples of 4 starting with 105 are (1050+2) + 0,4,8,.... <-- but STOP when tickover into 106 as first digits
 this occurs when your value is >= (l_ + 1) * 10 i.e. next multiple of 10 compared to startvalue of l_
 ^^^ this is why they become rarer after k=9,10; because you aren't guaranteed to have ANY multiple of k within these 2 constraining start/end conditions
"""
n = int(input())

if n > 25:
    print(0)
else:
    lucky = list(range(1, 9 + 1))

    for k in range(2, n + 1):
        lucky_ = []
        for l in lucky:
            l_ = l * 10
            offset = l_ % k
            if offset == 0:
                offset = k
            start_at = l_ + k - offset # see NOTES above
            end_at = (l + 1) * 10
            lucky_.extend(range(start_at, end_at, k))
        lucky = lucky_

    print(len(lucky))