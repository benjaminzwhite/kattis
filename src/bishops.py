# Bishops
# https://open.kattis.com/problems/bishops
# TAGS: greedy, logic, chess
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
Basically a greedy approach: draw n x n board on paper, fill top row with n bishops

You will find then that you are left with a triangle that is not covered, and the
bottom row now has n-2 spots (all except leftmost and righmost) where you can place 
another n-2 bishops. So answer is n + (n - 2) = 2 * n - 2

Implementation notes:

CARE! Special case n=1 is tested, which is = 1 while formula gives 2*n-2 = 0

(After submitting: seems that n=0 is not tested because my code below is AC O_o)
"""
import sys

for n in sys.stdin:
    print(max(2 * int(n) - 2, 1))