# Interpreter
# https://open.kattis.com/problems/interpreter
# TAGS: interpreter
# CP4: 1.6p, Time Waster, Harder
# NOTES:
"""
It seems on all programming OJ sites that interpreter/esolang exercises never clearly explain what the ops are supposed to do

- Here the expected meaning of:

"0 b c -> means goto the location in register b unless register c contains 0"

actually means:

if int(registers[c]) != 0, i = int(registers[b]), OTHERWISE YOU ALWAYS i += 1 STARTING FROM i = 0 WHERE i IS RAM POINTER

- Also the "register and RAM locations hold a 3 digit integer between 0 and 999" but it should clearly say 000 since you need to access a,b,c = 0,0,0

- Also the test case doesn't contain all the ops at least once, no 8s or 9s which are the confusing ones, so you can't even debug locally properly

So my solution isn't very DRY as I just kept adjusting until I understood the meaning of the exercise statement O_o
"""
import sys

registers = ["000"] * 10
ram = ["000"] * 1000

for j, x in enumerate(sys.stdin):
	ram[j] = x

i = 0
cnt = 0
while True:
    F = 0 # flag for whether we will jump i+1 or to a register address (due to a=='0' see below)
    cnt += 1
    a, b, c = ram[i]
    b = int(b)
    c = int(c)
    
    if a == '1':
        break
    elif a == '2':
        registers[b] = str(c).zfill(3)
    elif a == '3':
        tmp = (int(registers[b]) + c) % 1000
        registers[b] = str(tmp).zfill(3)
    elif a =='4':
        tmp = (int(registers[b]) * c) % 1000
        registers[b] = str(tmp).zfill(3)
    elif a == '5':
        registers[b] = registers[c]
    elif a == '6':
        tmp = (int(registers[b]) + int(registers[c])) % 1000
        registers[b] = str(tmp).zfill(3)
    elif a == '7':
        tmp = (int(registers[b]) * int(registers[c])) % 1000
        registers[b] = str(tmp).zfill(3)
    elif a == '8':
        registers[b] = ram[int(registers[c])]
    elif a == '9':
        ram[int(registers[c])] = str(registers[b]).zfill(3)
    elif a == '0':
        if int(registers[c]) != 0:
            i = int(registers[b])
            F = 1
    if F == 0:
        i += 1

print(cnt)