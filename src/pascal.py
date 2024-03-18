# Pascal
# https://open.kattis.com/problems/pascal
# TAGS: mathematics, number theory
# CP4: 5.3c, Finding Prime Factors
# NOTES:
n = int(input())

prime = True # <-- note that this handles the n=1 case (which wants you to print 0) even though 1 is not prime ;)
for d in range(2, int(n**0.5) + 1):
    if n % d == 0:
        print(n - n // d)
        prime = False
        break

if prime:
    print(n - 1)