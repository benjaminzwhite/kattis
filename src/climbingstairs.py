# Climbing Stairs
# https://open.kattis.com/problems/climbingstairs
# TAGS: logic
# CP4: 1.4j, Medium
# NOTES:
"""
You need to go to the office and back home during the day; and you need to go to the register HAVING COMPLETED THE need NUMBER OF STEPS

So basically "greedy":
- go to the office anyway, do your work day O_o
- then, as you head home, go to register floor: this adds + abs(register - office) more steps
- now check if you have reached the needed total:
Case 1 -> if office + abs(register-office) >= need, then you're OK: so you walk downstairs from register office (adds + register more steps)
Case 2-> else: just do up/down 1 floor around the register office until >= need reached. This takes either exactly need or need+1 (if need is odd) floors
               then, again, go home from register floor
"""
from math import ceil

need, register, office = map(int, input().split())

res = office + abs(register - office)

if res >= need:
	# Case 1 explained above
	res += register
else:
	# Case 2 explained above
	res += 2 * ceil((need - res) / 2)
	res += register

print(res)