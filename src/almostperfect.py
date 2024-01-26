# Almost Perfect
# https://open.kattis.com/problems/almostperfect
# TAGS: mathematics, number theory
# CP4: 5.3d, Prime Factors Functions
# NOTES:
while True:
    try:
        n = int(input())
        divisors = set()
        
        for d in range(1, int(n**0.5) + 1):
            if n % d == 0:
                divisors.add(d)
                divisors.add(n // d)

        if sum(divisors) == 2 * n:
            print(n, "perfect")
        elif abs(2 * n - sum(divisors)) <= 2:
            print(n, "almost perfect")
        else:
            print(n, "not perfect")
    
    except EOFError:
        break