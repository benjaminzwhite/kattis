# Busy Schedule
# https://open.kattis.com/problems/busyschedule
# TAGS: datetime, sorting
# CP4: 1.6i, Time, Harder
# NOTES:
"""
Datetime stuff + sort with a custom key
"""
def h(t):
    t_, ampm = t.split()
    hh, mm = map(int, t_.split(':'))
    tmp = hh * 60 + mm
    tmp %= 720
    if ampm == 'p.m.':
        tmp += 720
    return tmp

first_testcase = True

while True:
    n = int(input())
    if n == 0:
        break
        
    xs = []
    for _ in range(n):
        xs.append(input())

    res = sorted(xs, key=lambda x: h(x))

    if first_testcase:
    	first_testcase = False
    else:
    	print()

    for x in res:
    	print(x)