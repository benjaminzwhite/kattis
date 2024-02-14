# Curve Speed
# https://open.kattis.com/problems/curvespeed
# TAGS: basic
# CP4: 1.4b, Repetition Only
# NOTES:
"""
A bit overranked O_o ?
"""
import sys

for line in sys.stdin:
    R, S = map(float, line.split())
    V = ((R * (S + 0.16)) / (0.067))**0.5
    print(round(V))