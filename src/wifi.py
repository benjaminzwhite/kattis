# Wi-Fi
# https://open.kattis.com/problems/wifi
# TAGS: binary search, greedy
# CP4: 8.7b, BSTA+Other, Harder
# NOTES:
"""
Personal annoyance: all the testcases and examples are shown with the inputs ALREADY SORTED but when you submit you
actually need to sort the inputs yourself - so some tests must have unsorted inputs. I don't understand why people do this
as a kind of "gotcha" moment in problem statements - it's just misleading, because anyone who can solve this exercise
obviously knows that you need to sort the inputs to solve so why create an "artificial difficulty" ??

---

Binary search on the max_dist from any house to the nearest OPTIMALLY PLACED wifi emitter:

For each house, check if you are within range (-d,+d) of a currently placed wifi emitter, if not you need +1 wifi emitter.
Where should you place this emittier? The answer is: greedy place it as far away as possible from current house, so that you
just cover the current house: this ensures you avoid any "dead space" where there are no houses and therefore get optimal coverage.

After a given iteration of the binary search with the current mid guess for max_dist: count how many wifi emitters were used.
If the total is <= wifi available, then the check() for this binary search mid is OK so adjust max_dist down.
If you needed more emitters > wifi available, then you will need to adjust max_dist up.
"""
T = int(input())
for _ in range(T):
    wifis, num_houses = map(int, input().split())
    houses = []
    for _ in range(num_houses):
        houses.append(int(input()))

    houses.sort() # have to sort input yourself -.- why do people do this with misleading testcases it's so stupid

    lo = 0
    hi = 1e9 # can probably reduce this a lot as max house distance is 100_000 or something O_o
    EPS = 1e-6
    while hi - lo > EPS:
        mid = (hi + lo) / 2

        wifi_points_needed = 0
        curr_wifi_location = -1e9

        for house in houses:
            if abs(house - curr_wifi_location) <= mid:
                continue
            else:
                wifi_points_needed += 1
                curr_wifi_location = house + mid

        if wifi_points_needed <= wifis:
            hi = mid
        else:
            lo = mid

    print(f"{lo:.1f}")