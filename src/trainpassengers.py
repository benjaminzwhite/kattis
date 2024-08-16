# Train Passengers
# https://open.kattis.com/problems/trainpassengers
# TAGS: interpreter, grid
# CP4: 1.6e, Real Life, Easier
# NOTES:
"""
I found the description unclear (about order of leaving/entering and also the requirement about staying vs capacity)
I tried a few different interpretations until I got correct answer
"""
C, n = map(int, input().split())

curr_passengers = 0

# only n stations but loop to n+1; if station reaches == n without breaking, then we have processed all stations OK
# so we can perform the last check for "possible" if curr_passengers == 0 at end of code outside loop
for station in range(n + 1):
    if station == n:
        continue
    
    left, entered, stayed = map(int, input().split())
    if station == n - 1:
        if (entered > 0) or (stayed > 0):
            print("impossible")
            break
    
    curr_passengers -= left
    if curr_passengers < 0:
        print("impossible")
        break
    
    curr_passengers += entered
    if (curr_passengers > C) or (stayed > 0 and C != curr_passengers):
        print("impossible")
        break

if station == n:
    print("possible" if curr_passengers == 0 else "impossible")