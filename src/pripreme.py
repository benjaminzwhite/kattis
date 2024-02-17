# Pripreme
# https://open.kattis.com/problems/pripreme
# TAGS: logic, nice
# CP4: 3.4e, Non Classical, Easier
# NOTES:
"""
Nice exercise. Visualization of the logic:

Case 1: largest (____) is > sum of all others (----) :
 
|____________------      |  <- have to wait for the largest to finish in order to swap teachers
|------      ____________|  <- best total time is constrained by largest, for total time = largest+largest

Case 2: largest is <= sum of all others:

|____--------| <- one largest is finished, can start teaching the start of the ----- that has already been taught, with no waiting
|--------____| <- best total time is simply the sum of all the times
"""
N = int(input())

xs = list(map(int, input().split()))

largest = max(xs)
S = sum(xs)

# Case 1: largest is > sum of all others
if largest > S - largest:
    print(2 * largest)
# Case 2: largest is <= sum of all others
else:
    print(S)