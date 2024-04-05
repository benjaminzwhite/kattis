# Growing Rectangular Spiral
# https://open.kattis.com/problems/rectangularspiral
# TAGS: mathematics, logic, proof
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
CARE! Extra output requirements:
You have to print the dataset number for each line AND THE NUMBER OF STEPS (even though it's always either 2 or 6 O_o)

---

Case 1: if y > x, can go there directly in 2 moves: x, then y.

Case 2: geometry:
                          (x,y)
                            ^  
                            ^
  (-2,2)   |  (1,2)         ^ 
     v     |                ^
_____v_____|__(1,0)_________^________
     v                      ^
     v                      ^
     v                      ^
 (-2,-n)----------------->(x,-n)   

So for the 3 extra steps of the journey need:
1) dy = n+2 on the v part
2) dx = x+2 on the - part
3) dy = n+y on the ^ part
and since these need to be strictly increasing:
n+y > x+2 > n+2

Also since the move from (1,2) to (-2,2) has length 3, we need the first of the new steps to be length > 3 also.
For the minimum total length we want:
  n_best + y > x + 2
  n_best + y == x + 3
  n_best = x + 3 - y

(In the optimal case, n_best + y > x + 2 is always true since x+3-y+y = x+3 > x+2
 so don't need to check that condition on x,y below:)
"""
P = int(input())

for _ in range(P):
    dataset, x, y = map(int, input().split())
    # case 1
    if y > x:
        print(dataset, 2, x, y)
    # case 2
    else:
        n_best = x + 3 - y
        if x + 2 > n_best + 2 > 3:
            print(dataset, 6, 1, 2, 3, n_best + 2, x + 2, y + n_best)
        else:
            print(dataset,"NO PATH")