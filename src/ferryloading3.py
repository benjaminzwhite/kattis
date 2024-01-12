# Ferry Loading III
# https://open.kattis.com/problems/ferryloading3
# TAGS: deque
# CP4: 2.2l, List/Queue/Deque
# NOTES:
"""
Tedious reading comprehension (I bet this is why the problem is rated difficult, people getting WA for same reason as me):

I was passing all given tests but fail on attempt. Re-reading description:

"For each test case, output one line per car, in the same order as the input, giving the time at which that car is unloaded at the opposite bank."

So: The problem wants you to PRINT THE OUTPUT IN THE ORDER IN WHICH THE CARS ARRIVE, RATHER THAN "AS THEY ARE UNLOADED IN REAL LIFE".

IMHO I think this is pretty un-intuitive, especially since they deliberately made the example testcase work with the more "logical" output order.
(and worst of all it doesn't really add anything interesting to the exercise, just more reading comprehension and artificial difficulty).

---

Actual solution notes:

- Due to the output requirement mentioned above, I maintain a RES[] list of the current car's ORIGINAL INDEX/ORDER
"""
from collections import deque

c = int(input())

for curr_test_case in range(1, c+1):
    n, t, m = map(int, input().split())
    
    leftbank, rightbank = deque([]), deque([])
    
    RES = [0] * m
    for j in range(m):
        car_time, car_side = input().split()
        car_time = int(car_time)
        if car_side == "left":
            leftbank.append(j)
        else:
            rightbank.append(j)
        RES[j] = car_time
            
    bank, time = 0, 0 # bank == 0 is left, 1 is right. Allows to swap bank with: bank ^= 1 
    
    while leftbank or rightbank:
        left_time, right_time = float('inf'), float('inf')
        if leftbank:
            left_time = RES[leftbank[0]]
        if rightbank:
            right_time = RES[rightbank[0]]
        
        next_time = min(left_time, right_time)
        time = max(time, next_time)
        
        loaded = 0
        if bank == 0:
            curr_bank = leftbank
        else:
            curr_bank = rightbank
        
        while curr_bank and RES[curr_bank[0]] <= time and loaded < n:
            loaded += 1
            RES[curr_bank[0]] = time + t
            curr_bank.popleft()
        
        time += t
        bank ^= 1 # swap bank from 0 to 1, or 1 to 0
    
    for car in RES:
        print(car)
    
    if curr_test_case != c:
        print()