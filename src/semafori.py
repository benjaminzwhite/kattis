# Semafori
# https://open.kattis.com/problems/semafori
# TAGS: logic
# CP4: 1.6i, Time, Harder
# NOTES:
N, L = map(int, input().split())

T = 0
prev_distance = 0
for _ in range(N):
    d, red, green = map(int, input().split())
    T += (d - prev_distance) # it took us this many seconds to get here from last traffic light
    # now check do we need to wait for next green light or not:
    part_of_cycle = T % (red + green)
    if part_of_cycle >= red:
        # we are in green so ok
        wait_time = 0
    else:
        wait_time = red - part_of_cycle
        T += wait_time
    prev_distance = d

# AT THIS POINT T MEASURES THE TIME TO CLEAR THE FINAL RED LIGHT - STILL HAVE TRAVEL TIME TO END OF THE ROAD, AT L:
# since last traffic light is at prev_distance, then leftover is L - prev_distance
res = T + (L - prev_distance)

print(res)