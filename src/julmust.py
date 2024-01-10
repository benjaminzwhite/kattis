# Julmust
# https://open.kattis.com/problems/julmust
# TAGS: binary search
# CP4: 9.inte, Interactive Problem
# NOTES:
"""
- It's an interactive program - you are trying to guess total number of drinks drunk up to current day, 
  where you DON'T KNOW how many are drunk (constant) per day.

- So each guess you linearly increase days by += 1
  and then perform binary search to find the constant: drinks_per_day

- And your guess then is : days_so_far * guessed_constant_drinks_per_day

- PROGRAM ACCEPTED WHEN YOU RECEIVE AN "EXACT" RESPONSE, DON'T NEED TO PRINT ANYTHING TO CONSOLE
"""
R = int(input())

l,r = 1,R
day = 0

# R_max is given as 1_000_000 and max num of days is 85 or so, but log2(1_000_000) is 20 so only
# need ~20 days max to find result, hence can use while True without worrying
while True:
    day += 1
    mid = (l + r) // 2
    
    print(day * mid, flush=True) # Kattis says to flush for this exercise explicitly in the problem statement
    
    response = input()
    if response == "exact":
        break
    elif response == "less":
        r = mid - 1
    else:
        l = mid + 1