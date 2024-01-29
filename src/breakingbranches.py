# Breaking Branches
# https://open.kattis.com/problems/breakingbranches
# TAGS: game, logic, proof
# CP4: 5.7a, Game Theory (Basic)
# NOTES:
"""
If the length of the stick is n=6 then there are n-1 = 5 breakable locations
-|-|-|-|-|-

The game ends when there are 0 breakable locations available (this total is
split across all smaller sticks, it's a global count when you think about it)

Each turn reduces the number of breakable locations by 1

So if a player has 1/3/5/... breakable location on their turn, they will win

So the condition is (n - 1) being ODD, or just n being EVEN, for Alice to win.

The specific move she chooses is IRRELEVANT (just output "1" for simplicity)
there is no "strategy" that makes a difference.
"""
n = int(input())

if n % 2 == 0:
    print("Alice")
    print("1")
else:
    print("Bob")