# FizzBuzz
# https://open.kattis.com/problems/fizzbuzz2
# TAGS: array
# CP4: 1.4j, Medium
# NOTES:
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)

N,M = map(int, input().split())
best_score = -1
best_candidate = -1
REF = [fizzbuzz(m) for m in range(1, M + 1)]

for candidate in range(1, N + 1):
    score = sum(ref == x for ref, x in zip(REF, input().split()))
    if score > best_score:
        best_score = score
        best_candidate = candidate

print(best_candidate)