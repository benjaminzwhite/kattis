# Cocoa Coalition
# https://open.kattis.com/problems/cocoacoalition
# TAGS: mathematics, number theory, logic, proof, nice
# CP4: 5.3k, Divisibility Test
# NOTES:
"""
Nice exercise:

Initial rect is n*m, target is = a

-with 1 cut you can form any rect 1..n*m or n*1..m so if target=a is divisible by m or n you can use this option
 xxxoo
 xxxoo
 xxxoo  here n=5,m=3, a=6 so you can "use the m=3 side" 

-with 2cuts: (A) you either cut 2 parallel lengthways or vertically, but this doesn't create any new possibilities compared to ^^^ step
 e.g. xxxx  here 2 horizontal cuts; you could obtain any of the resultant rectangles using a single cut as in step 1)
      xxxx
      oooo
      oooo
      yyyy

-with 2cuts: (B) OR you can cut 1 vertical 1 horizontal -> this creates 3 rectangles 
 [NB!!! YOU ONLY PERFORM THE CUT ON ONE OF THE RESULTANT NEW RECTANGLES SO YOU DO *NOT* FORM *4* RECTANGLES - ANSWER IS DIFFERENT IF YOU ARE ALLOWED TO "CUT THROUGH" LIKE IN USUAL PAPER CUTTING EXERCISES]
 so e.g.  xxxxx
          xxxxx
          ooyyy  <--- note how you only form *3* rectangles; here cut "vertically" ONE of the rectangles obtained from first cut step
          ooyyy
          ooyyy
    --> So here, again, if you can express target=a as  n' * m' where 0 < n' < n and 0 < m' < m, then you can do this in 2 cuts
    !!! also need to check this condition for n*m - a since it's the COMPLEMENT that might be expressible in this form also

-with 3 cuts: always possible: take a as k*n + remainder (use n here WLOG, same same with m):
     xxxx____
     xxxx____
     xxxx____
     xxxxx___
     xxxxx___

          ^---- make one cut here to get the "big _____ rectangle away"
         ^----- make one cut here to get the "remainder __xx column away"
                                                          ^------------------make one cut here to get the "xx" and "___" separated: now have one rectangle of size k*n and one of size 1*r so can form k*n + 1*r as required

"""
n, m, a = map(int, input().split())

if a % m == 0 or a % n == 0:
    print(1)
else:
    flg = False
    if n < m:
        n, m = m, n
    for d in range(1, n):
        if a % d == 0 and a // d < m or (compl := n * m - a) % d == 0 and compl // d < m:
            flg = True
            break
    if flg:
        print(2)
    else:
        print(3)