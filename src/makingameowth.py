# Making A Meowth
# https://open.kattis.com/problems/makingameowth
# TAGS: basic
# CP4: 1.4j, Medium
# NOTES:
"""
I found the description very hard to understand/reading comprehension:

The P is NOT ACTUALLY the fixed pages of some book or whatever; here's the actual explanation:

If you must read a total of P pages, with someone else interfering every N'th page you read:

1) How many pages in total, T, will you physically/actually have to "turn over"? This is MORE THAN P
2) How many of those T total turned over pages are read by the intruder ? It's T - P of course, this how many Meowth reads

e.g. for first test case, 4 10 2 3, the situation is actually: N=4, P=10:
1,2,3 /4/ 5,6,7 /8/ 9,10,11 /12/ 13 
Note that you TURN OVER 13 pages, that you READ 10 pages: 1,2,3 | 5,6,7 | 9,10,11 | 13, and Meowth reads 3 pages: 4,8,12

So the solution is that you always read P pages.
and Meowth reads P//(N-1) since he reads every Nth page
(think geometrically of N-1 as the size of your intervals in the diagram above)
"""
n, p, x, y = map(int, input().split())

you = p * x
meowth = (p // (n - 1)) * y
res = you + meowth

print(res)