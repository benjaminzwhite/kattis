# Sum of the Others
# https://open.kattis.com/problems/sumoftheothers
# TAGS: basic, logic
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
You don't need to "try all answers":
- If all the other numbers sum to S, and if the sum itself is also in the input line, then the line of inputs will sum to S+S = 2*S
- So the answer we want, S, is just the sum of the line of inputs divided by 2 (i.e. 2*S // 2 = S)
"""
while True:
    try:
        print(sum(map(int, input().split())) // 2)
    except EOFError:
        break