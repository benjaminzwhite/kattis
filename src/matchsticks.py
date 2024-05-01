# Matchsticks
# https://open.kattis.com/problems/matchsticks
# TAGS: greedy, nice
# CP4: 9.cons, Construction
# NOTES:
"""
Nice little ad hoc exercise:

For min possible, using bruteforce (I kept the brute force code below in comments) you see recurring pattern:
once you get past the triple digit cases basically you are trying to greedily pack as many 8's as possible
(since they use up most matchsticks) then fitting in the leftover matchsticks if you dont have enough to make
one more '8' (which requires 7 matchsticks) hence the mod 7 dependence once you get out of the small cases

Implementation notes:

I create a few small n cases as they are easier to handle specifically on a 1 by 1 basis.

Then I handle the mod 7 patterns for the larger cases with a LOOKUP of the various optimal combinations.

---

Brute force code for studying the patterns

d = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}

mapping = {}

for n in range(1, 10001):
    how_many_matchsticks = sum(d[c] for c in str(n))
    if how_many_matchsticks not in mapping:
        mapping[how_many_matchsticks] = []
    mapping[how_many_matchsticks].append(n)

for k, v in mapping.items():
    print(k, min(v))
"""
SMALL_CASES = {2:'1', 3:'7', 4:'4', 5:'2', 6:'6', 7:'8', 8:'10', 9:'18', 10:'22', 11:'20', 12:'28', 13:'68', 14:'88', 15:'108'}
LOOKUP = ['108', '188', '200', '208', '288', '688', '888'] # mod 7 behaviour due the the figure '8' requiring 7 matchsticks

def get_min(n):
    if n <= 15:
        return SMALL_CASES[n]
    q, r = divmod(n - 15, 7)
    how_many_eights = q
    res = LOOKUP[r] + how_many_eights * '8'
    return res

def get_max(n):
    # use as many decimal places as possible -> greedy with '1' symbol using up 2 matchsticks each
    if n % 2 == 1:
        how_many_ones = (n - 3) // 2
        res = '7' + how_many_ones * '1'
    else:
        how_many_ones = n // 2
        res = how_many_ones * '1'
    return res

T = int(input())

for _ in range(T):
    n = int(input())
    print(get_min(n), get_max(n))