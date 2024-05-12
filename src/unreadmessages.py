# Unread Messages
# https://open.kattis.com/problems/unreadmessages
# TAGS: mathematics, logic, dict
# CP4: 0, Not In List Yet
# NOTES:
n, m = map(int, input().split())

d = {}
unreads = 0
curr_generation = 0
for _ in range(m):
    l = input()
    unreads += (n - 1) # we are sending a new message to all n-1 other people
    last_updated = d.get(l, 0) # we read our unread messages; these are the messages sent since we last checked our inbox
    unreads -= (curr_generation - last_updated)
    curr_generation += 1
    d[l] = curr_generation # record that this person most recently checked their inbox in this generation
    print(unreads)