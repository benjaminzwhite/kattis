# Battle Simulation
# https://open.kattis.com/problems/battlesimulation
# TAGS: basic, dict
# CP4: 1.4j, Medium
# NOTES:
s = input()

REF = {'R':'S', 'B':'K', 'L':'H'}

res = []
i = 0
while i < len(s):
    if len(set(s[i : i + 3])) == 3:
        res.append('C')
        i += 3
    else:
        res.append(REF[s[i]])
        i += 1
        
print(''.join(res))