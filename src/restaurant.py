# Working at the Restaurant
# https://open.kattis.com/problems/restaurant
# TAGS: array, stack, interpreter
# CP4: 2.2j, Stack
# NOTES:
"""
Lots of reading comprehension: makes you think it's something sophisticated but just do exactly what the testcase does O_o 
i.e. drop all on pile2, move all from pile2 to pile1 when "need some" : you need some when the number of plates on pile1 is < number requested
(only move from pile2 to pile1 when empty otherwise will not preserve order of arrival)
"""
while (N := int(input())):
    pile1, pile2 = 0, 0
    for _ in range(N):
        op, x = input().split()
        x = int(x)
        if op == "DROP":
            pile2 += x
            print(f"DROP 2 {x}")
        elif op == "TAKE":
            if x <= pile1:
                pile1 -= x
                print(f"TAKE 1 {x}")
            else:
                leftover = x - pile1
                if pile1 > 0:
                    print(f"TAKE 1 {pile1}")
                    pile1 = 0
                print(f"MOVE 2->1 {pile2}")
                pile1 = pile2
                pile2 = 0
                print(f"TAKE 1 {leftover}")
                pile1 -= leftover
    print()