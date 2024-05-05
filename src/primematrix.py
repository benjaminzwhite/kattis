# Prime Matrix
# https://open.kattis.com/problems/primematrix
# TAGS: logic, nice
# CP4: 3.2a, Pre-calculate-able
# NOTES:
"""
Nice exercise:

Possibility criterion: need n distinct numbers, all less than b. So need n <= b in any case.

Observation: if you do 1 + 2 +... + n-1 + X where X is leftover to reach closest prime, there is risk that X needs to be very large > b
-> so can assign the excess to each other value by apportioning +1 to the values
-> SO START FROM 1,2,3...n  then you +1 the n VALUE (since you can't increment +1 any other without creating duplicates)
   then +1 the n-1 value, then n-2, etc in DESCENDING ORDER and repeat until get to smallest next prime
-> check that your largest value, at the end of this process, is <= b:

Walkthrough example:

b = 20, n = 5:
step1: [1,2,3,4,5] <- this currently sums to n*(n+1)//2 = 15 which is NOT PRIME
                ^___ += 1
       [1,2,3,4,6] <- this sums to 15 + 1 which is not prime
       [1,2,3,5,6] <- this sums to 16 + 1 which IS PRIME: OK, now just check that we didn't end up with any number > b: NO, max is 6 OK

So the formula is: "generate range from 1 to n", find the delta from n*(n+1)//2 to next smallest prime, then divide delta evenly among the 
n elements STARTING FROM THE LARGEST ("right to left") THEN FINALLY CHECK DID NOT PRODUCE A NUMBER > b

So using above example the short way; n*(n+1)//2 = 15; smallest next prime is 17, delta is 2, so divide 2 evenly among the 2 largest elements
"""
n, b = map(int, input().split())

range_sum = n * (n + 1) // 2

p = range_sum
while True:
    if all(p % d != 0 for d in range(2, int(p**0.5) + 1)):
        next_prime = p
        break
    p += 1

delta = next_prime - range_sum
res = list(range(1, n + 1))
q, r = divmod(delta, n)
for i in range(n - r):
    res[i] += q
for i in range(n - r, n):
    res[i] += (q + 1) # apportion the excess equally to the r largest/rightmost elements in the range

if res[-1] > b: # with the above way of apportioning +1 from largest to smallest elements in range(1,n+1) then rightmost element will always be largest in res list
    print("impossible")
else:
    for shift in range(n):
        print(*(res[shift:] + res[:shift]))