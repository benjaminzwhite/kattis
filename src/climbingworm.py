# Climbing Worm
# https://open.kattis.com/problems/climbingworm
# TAGS: logic, proof
# CP4: 1.4j, Medium
# NOTES:
"""
Don't need to simulate, can solve analytically (see code below for proof).

CARE! With my approach below, need to handle the special case where climb >= target i.e. when can reach in 1 move.

My approach for e.g. inputs c, s, t = 13, 12, 5 will produce -7 instead of correct answer = 1
(only 1 climb step is needed to go reach target of 5)
"""
from math import ceil

climb, slip, target = map(int, input().split())

# Say worm first reaches top of pole on kth step. 
# Then he has made k-1 slips, so we have:
# k*c - (k-1)*s >= t  [goal condition, which we can simplify:]
# k*(c-s) >= (t-s)
# k >= (t-s)/(c-s)
res = ceil((target - slip) / (climb - slip))

if climb >= target:
    res = 1

print(res)