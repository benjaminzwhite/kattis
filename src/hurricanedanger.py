# Hurricane Danger!
# https://open.kattis.com/problems/hurricanedanger
# TAGS: mathematics, geometry
# CP4: 7.2b, Lines
# NOTES:
"""
The main focus of the exercise is good numerical practice/implementation.
You can avoid using floats/sqrts etc. by staying in integers:

See comment below; dont need actual distance, just take numerator of the distance calculation
and ignore "normalisation" denominator which involves sqrts and converting to floats etc.
"""
T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    m = int(input())

    res = []
    best = float('inf')
    for _ in range(m):
        name, x, y = input().split()
        x = int(x)
        y = int(y)
        # https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
        # val is the numerator in the actual distance calculation - since don't need the actual value, just keep the numerator
        # since denominator is some sqrt() of a scaling factor that is the same for all points i.e. independent of current x,y
        val = abs((x2 - x1) * (y1 - y) - (x1 - x) * (y2 - y1)) # val: an integer since all xs and ys are ints
        if val < best:
            res = [name]
            best = val
        elif val == best:
            res.append(name)

    print(*res)