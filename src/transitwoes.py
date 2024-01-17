# Transit Woes
# https://open.kattis.com/problems/transitwoes
# TAGS: basic
# CP4: 1.6e, Real Life, Easier
# NOTES:
s, t, n = map(int, input().split())
ds = list(map(int, input().split()))
bs = list(map(int, input().split()))
cs = list(map(int, input().split()))

curr_time = s + ds[0] # we are now at first bus stop

for i in range(len(bs)):
    if curr_time % cs[i] == 0: # if we e.g. arrive at curr_time 15 to a bustop where busses arrive every 3 mins, then we dont have to wait
        wait_time = 0
    else:
        wait_time = cs[i] - (curr_time % cs[i]) # else if we arrive at curr_time 17 to busstop where every 3mins is bus, we have to WAIT: 17%3= 2 <- mins since last bus, so wait 3-2 = 1 min for NEXT one
    curr_time += wait_time + bs[i] + ds[i+1]

if curr_time <= t:
    print("yes")
else:
    print("no")