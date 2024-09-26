# Game of Throwns
# https://open.kattis.com/problems/throwns
# TAGS: stack, interpreter
# CP4: 2.2j, Stack
# NOTES:
n, k = map(int, input().split())

commands = input().split()

stk = [0] # student 0 starts with egg
i = 0 # command pointer

while i < len(commands):
    command = commands[i]
    if command == "undo":
        for _ in range(int(commands[i + 1])):
            stk.pop()
        i += 2
    else:
        curr = (stk[-1] + int(command) + n) % n # wraparound trick for idx < 0 or idx >= n
        stk.append(curr)
        i += 1

print(stk[-1]) # last item in stack represents the student currently holding egg