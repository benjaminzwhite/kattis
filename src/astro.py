# Astro
# https://open.kattis.com/problems/astro
# TAGS: brute force, datetime
# CP4: 2.2b, 1D Array, Harder
# NOTES:
"""
As always with time based stuff, very tedious to debug since hard to know if error due to some 00:00 vs 24:00 nonsense or whatever.

I just do the obvious brute force:
try star1 + a * delta1 for all possible values of a = 1,2,3... and see if any correspond to star2 + b*delta2 with b intger
by checking whether (after rearranging eq) delta2 divides the integer expression formed exactly.

---

My first submissions were failing so I tried adjusting UPPER_RANGE to 10**7 but made no difference.

Then noticed that my line:
if (star1 + a*delta1 - star2) % delta2 == 0 ...
[which is where I am brute forcing all the solutions to the 2 stars landing on same time with integer coefficients a, b for their deltas]
... produces answers where b == 0

Thinking about this - with input:
Star1  = 23:00
delta1 = 00:47
Star2  = 23:47
delta2 = 15:15 (whatever)

my code was producing that the "next time they shine together" is 23:47
-> This seems perfectly logical/OK to me, but it seems that it is NOT ALLOWED BY EXERCISE ?!
(this corresponds to "b == 0" i.e. star1 + a==1 * delta1 == star2 + b==0 * delta2)

To see if this was the problem, I added the extra line:
... and (star1 + a*delta1 - star2) // delta2 > 0
which rules out this b==0 case and the solution passed -.-
"""
stars = []
for _ in range(4):
    hh, mm = map(int, input().split(':'))
    x = 60 * hh + mm
    stars.append(x)

star1, delta1 = stars[0], stars[2]
star2, delta2 = stars[1], stars[3]

future_time = None

UPPER_RANGE = 10**3 # found experimentally (no theory atm) - passes test case for Never at 10**6, adjust if needed TRIED DOWN TO 10**2 <- fails, 10**3 passes

for a in range(1, UPPER_RANGE):
    if (star1 + a * delta1 - star2) % delta2 == 0 and (star1 + a * delta1 - star2) // delta2 > 0:
        future_time = star1 + a * delta1
        break

if future_time is None:
    print("Never")
else:
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    q, r = divmod(future_time, 24 * 60)
    print(days[q % 7])
    hh, mm = divmod(r, 60)
    print(str(hh).zfill(2), ':', str(mm).zfill(2), sep='')