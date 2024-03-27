# Not Amused
# https://open.kattis.com/problems/notamused
# TAGS: interpreter
# CP4: 2.3h, Balanced BST (map)
# NOTES:
curr_day = 0

while True:
    try:
        l = input()
        if l == "CLOSE":
            print(f"Day {curr_day}")
            for k, v in sorted(d.items()):
                print(f"{k} ${v * 0.1:.2f}")
            print()
        elif l == "OPEN":
            curr_day += 1
            d = {}
        else:
            op, name, val = l.split()
            if name not in d:
                d[name] = 0
            if op == "ENTER":
                d[name] -= int(val)
            else:
                d[name] += int(val)
    except EOFError:
        break