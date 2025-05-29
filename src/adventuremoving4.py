# Adventures in Moving -- Part IV
# https://open.kattis.com/problems/adventuremoving4
# TAGS: dynamic programming
# CP4: 4.6c, Conversion to DAG
# NOTES:
"""
Dynamic programming:

The dp state is dp[i=0, 1, ..., 200] "minimum cost to leave each station with tank capacity = i"

Initial condition/state: you are in station "-1" i.e. not in a real station - your tank is half_full so 200//2 = 100
and the cost to "leave this station" i.e. start rental place, is therefore 0

Now process each "real" (see below for "dummy" station I used for implementation purposes) station in order:

- station is at a distance "dist_travelled" = station_x - previous_x_location (i.e. prev station or rental place)
- to leave each real station, with tank capacity j you can:

1. Arrive at the station, having travelled D km from a place where you had j+D fuel - i.e. DONT BUY ANY FUEL HERE.
This "option1" is possible IF j + D >= D i.e. if you left previous station with 87 fuel and need to travel 123 to reach this
one, then your tank went < 0 on the road

2. Try to buy 1,2,3... units of fuel at this station on top of the various possible amounts you arrived with:
- you can arrive with any amount <= j+D - D i.e. determined by prev_travel distance
- for all the possible valid amounts to arrive with, try adding 1,2,3... up until your tank is now 200
(you can do this by starting with +1 fuel unit, for +1 COST, then for +2 fuel unit just look behind at curr_row and add +1 COST etc.)

See my implementation below - this is "option2" using "if curr row...".

I append a "dummy" station at distance = dist, where the fuel costs +Infinite amount.
This models arriving at your destination, where you can't buy fuel/have to deliver truck with 100 units in tank
So after this last "station", the result is in dp[-1][100]

---

Implementation notes:

You can make the dynamic programming more efficient by just storing the previous row (save memory) but I left my first solution
because it is clearer, also in how you build the dp array via the input step.
"""
dist = int(input())

stations = []
while True:
    try:
        km , cost = map(int, input().split())
        stations.append((km, cost))
    except:
        break

# CARE! this is my "dummy" last station - our arrival location, where cost = INF so can't refuel there if there is no "real" station
stations.append((dist, float('inf')))

# minimum cost to leave each station with tank capacity = i
dp = [[float('inf')] * (200 + 5)] # tank capacity is 200, 0 is valid so should be 201. I put values up to 205 as sentinel

dp[0][100] = 0 # initial state is "station 0" i.e. start position, and we have 100 litres at a total cost of 0 currently

prev_loc = 0
for km, cost in stations:
    dist_travelled = km - prev_loc
    prev_loc = km # don't forget to update O_o

    curr_row = []
    for i in range(205):
        if i + dist_travelled <= 200:
            option1 = dp[-1][i + dist_travelled]
        else:
            option1 = float('inf')

        if curr_row:
            option2 = curr_row[-1] + cost
        else:
            option2 = float('inf')

        res = min(option1, option2)

        curr_row.append(res)
    
    dp.append(curr_row) # you can optimize the memory use here instead of appending everything O_o

print(dp[-1][100] if dp[-1][100] < float('inf') else "Impossible")