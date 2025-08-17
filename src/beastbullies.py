# Beast Bullies
# https://open.kattis.com/problems/beastbullies
# TAGS: logic, greedy
# CP4: 0, Not In List Yet
# NOTES:
"""
Nice little exercise/greedy reasoning practice. 

I found that considering, for example, the testcase:

10 4 3 2 1

helpful, as it's an "obvious one" where ALL the small animals need to stick together.
So you should be able to describe clearly "why" and translate that to algorithm.
(note the inequality is >= i.e. 1+2+3+4 == 10 so they DO survive the fight vs 10, whereas they would lose vs 11 since 11>10)

Formalizing this notion of stick together is how I got a solution approach - I wrote the comments below.
"""
n = int(input())

xs = []
for _ in range(n):
    xs.append(int(input()))

xs = sorted(xs, reverse=True)

res = 0
curr_group_strength = 0
curr_group_size = 0
all_prev_group_strengths = 0

for x in xs:
    curr_group_strength += x
    curr_group_size += 1
    
    # if curr_group_strength >= all_prev_group_strengths, then by being grouped they can survive against all attack patterns from bigger animals
    # so it makes sense for them to protect eachother -> the entire group is safe and will stick together
    if curr_group_strength >= all_prev_group_strengths:
        res += curr_group_size
        
        # curr group are predators for smaller ones
        all_prev_group_strengths += curr_group_strength

        # reset current group; we try with next animal who will start his own "self defense" grouping O_o
        curr_group_strength = 0
        curr_group_size = 0

print(res)