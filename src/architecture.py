# Architecture
# https://open.kattis.com/problems/architecture
# TAGS: logic, proof, nice
# CP4: 1.4i, Still Easy
# NOTES:
"""
Nice exercise. A bit of reading comprehension to understand statement:

Reformulation:
"Is there any arrangement of buildings in an RxC grid that can result in the given North and East visible skyline ?"

Proof steps:

Necessary condition/observation:
The maximum building height, max_height, for the entire board must therefore be the max of East, and max of North,
and therefore max_East == max_North is necessary/always true.
(Proof by contradiction/logic - the highest building is visible from both East and North skyline, so its height value
must also be the highest value in each of those 2 rows/columns)

This condition is also SUFFICIENT since you can always do the following construction:

Let max_height = 7 for example appear in 2nd row and 3rd col. Then place the values as follows:

       0 0 a 0
       p q 7 r
       0 0 b 0
       0 0 c 0

where p,q,r are the 3 other values (<= max_height = 7) that you want to appear in the Northern skyline
and a,b,c (<= max_height = 7) are the 3 other values you want in Eastern skyline
and 0 elsewhere
"""
R, C = map(int, input().split())

eastern = map(int, input().split())
northern = map(int, input().split())

if max(eastern) == max(northern):
    print("possible")
else:
    print("impossible")