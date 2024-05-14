# Card Divisibility
# https://open.kattis.com/problems/carddivisibility
# TAGS: mathematics
# CP4: 0, Not In List Yet
# NOTES:
"""
Given L and R you have something like:

L=3, R=10:

345678910

This is just in general a sum of the form:

  sigma_i { d_i * 10**i
= sigma_i { d_i * (10**i - 1 + 1)
= sigma_i { d_i * (10**i - 1) + sigma_i { d_i *  1
  ^------------------------^   ^-----------------^
      this is 0 mod 9             this is the sum of the digits

In turn, the sum of the digits in 345678910 MOD 9 will be the same as the sum of the numbers themselves 3,4,5...9,10 MOD 9 
(look up "Digital Root" exercises done previously on Kattis or other OJs)

test_n = 14710
print(test_n, test_n%9) # 14710 4
print(S:=sum(int(d) for d in str(test_n)),S%9) # 13 4

So you can get the answer by taking the sum of all the INTS THEMSELVES from L to R inclusive: 3+4+5..+9+10, then taking this sum mod 9

Finally since L,R = 10**12 max, can't just do brute force sum(range(L,R+1)) so use the Gauss sum of range approach:

res = ( (L+R) * (R-L+1) // 2 ) % 9
"""
L, R = map(int, input().split())

res = (L + R) * (R - L + 1) // 2

print(res % 9)