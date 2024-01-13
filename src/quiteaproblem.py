# Quite a Problem
# https://open.kattis.com/problems/quiteaproblem
# TAGS: basic
# CP4: 6.4a, String Matching
# NOTES:
import sys

for line in sys.stdin:
    if "problem" in line.lower():
        print("yes")
    else:
        print("no")