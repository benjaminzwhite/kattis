# Potion Commotion
# https://open.kattis.com/problems/potioncommotion
# TAGS: logic
# CP4: 0, Not In List Yet
# NOTES:
from math import ceil

n, m, p = map(int, input().split())
attacks = map(int, input().split())

curr_hp = n
flg = True
for attack in attacks:
    if attack < curr_hp:
        curr_hp -= attack
    else:
        # can you heal up for this attack
        potions_needed = max(1, ceil( (attack - curr_hp) / 20 ) )
        if potions_needed > p:
            flg = False
            break
        else:
            curr_hp = min(n, curr_hp + potions_needed * 20)
            curr_hp -= attack
            if curr_hp <= 0:
                flg = False
                break
            p -= potions_needed

if flg:
    print("champion")
else:
    print("next time")