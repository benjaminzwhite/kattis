# Average Speed
# https://open.kattis.com/problems/averagespeed
# TAGS: datetime
# CP4: 1.6o, Time Waster, Easier
# NOTES:
def time_to_seconds(s):
    hh, mm, ss = map(int, s.split(':'))
    return ss + 60 * mm + 60 * 60 * hh

curr_time = 0
curr_speed = 0
total_distance = 0

while True:
    try:
        hhmmss, *new_speed = input().split()
        time = time_to_seconds(hhmmss)
        total_distance += (time - curr_time) * curr_speed / 3600
        curr_time = time
        if new_speed:
            curr_speed = int(new_speed[0])
        else:
            print(hhmmss, f"{total_distance:.2f} km")
    except EOFError:
        break