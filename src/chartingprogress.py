# Charting Progress
# https://open.kattis.com/problems/chartingprogress
# TAGS: string
# CP4: 2.2f, Sorting, Harder
# NOTES:
import sys

offset = 0
for line in sys.stdin:
    line = line.strip() # added strip() but not sure if needed actually O_o
    if line == '':
        offset = 0 # this is due to resetting between testcases
    L = len(line)
    c = line.count('*')
    print((L - c - offset) * '.' + c * '*' + offset * '.')
    offset += c