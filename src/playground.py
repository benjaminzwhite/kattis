# Playground
# https://open.kattis.com/problems/playground
# TAGS: mathematics, geometry, logic
# CP4: 3.4f, Non Classical, Harder
# NOTES:
"""
If the accumlated length of all prev smaller segments >= current segment, you can satisfy the requirement since:

          .
       .     ,             
    .             ,        <=== here have freedom to arrange the pieces (think of it physically); it's a generalization of making a triangle if sum 2 small sides > large side
   /                   ,   
  /                     |  
  _______________________  <--- current segment (longest)
"""
while int(input()):
    xs = sorted(map(float, input().split()))

    flg = False
    acc = 0
    for x in xs:
        if acc >= x: # NOTE: unlike with triangle which needs 2 small sides > big (to avoid degenerate triangle) - here the "soldering semicircles" means we are allowed the == case (indeed this works for the testcase xs=[1.00, 1.00] <-- solder the 2 semicircles and it's OK)
            flg = True
            break
        acc += x

    if flg:
        print("YES")
    else:
        print("NO")