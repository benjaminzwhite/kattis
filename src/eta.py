# ETA
# https://open.kattis.com/problems/eta
# TAGS: mathematics, graph, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/eta.md
"""
flg = True
a, b = map(int, input().split('/'))
if a < b - 1:
    flg = False

a_prime, b_prime = a, b

# you can solve this analytically if you want, I'm just keeping the logic from the notes above for clarity
while a_prime - b_prime + 1 > (b_prime - 2) * (b_prime - 1) // 2:
    a_prime += a
    b_prime += b

num_shifts_needed = a_prime - b_prime + 1

distances = [0] * (b_prime + 10) # +10 is just a sentinel value
distances[0] = 1
distances[1] = b_prime - 1 # originally all in d=1 

curr_d = 1
while num_shifts_needed > 0:
    max_can_shift = distances[curr_d] - 1 # must leave 1 behind
    if max_can_shift >= num_shifts_needed:
        distances[curr_d] -= num_shifts_needed
        distances[curr_d + 1] += num_shifts_needed
        num_shifts_needed = 0
    else:
        distances[curr_d] = 1
        distances[curr_d + 1] = max_can_shift
        num_shifts_needed -= max_can_shift
    curr_d += 1

# printing, see implementation notes
if not flg:
    print("impossible")
else:
    # Always produces a tree on b_prime vertices and b_prime-1 edges therefore:
    print(b_prime, b_prime - 1)
    curr_vertex_label = 2
    for d, cnt in enumerate(distances[1:curr_d + 5], 1): # +5 is sentinel
        for v in range(curr_vertex_label, curr_vertex_label + cnt):
            print(curr_vertex_label - 1, v)
        curr_vertex_label += cnt