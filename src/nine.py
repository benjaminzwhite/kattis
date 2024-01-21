# I Hate The Number Nine
# https://open.kattis.com/problems/nine
# TAGS: mathematics, combinatorics
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
This is a relatively simple version of such questions, because we are asked for ALL d-digit numbers
(More complex versions ask something like "How many numbers less than 4829336 do not contain a 5" and you
now have to consider ranges a bit).

The answer is combinatorial: for each digit position, you can choose any digit EXCEPT the number 9.

So there are 10 - 1 = 9 choices per digit position.

However, for the first position, you cannot choose the digit 0 either (else it would not be a d-digit number anymore), so
for the first position there are only 8, rather than 9, possible choices of digit.

Note that the rest of the exercise is very simple in Python since you can do powers of large numbers with a BIGMOD = 10**9 + 7
using the inbuilt pow() optional 3rd argument.
"""
BIGMOD = 10**9 + 7

T = int(input())

for _ in range(T):
	d = int(input())

	res = 8 * pow(9, d - 1, BIGMOD)

	print(res % BIGMOD)