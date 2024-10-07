# Shiritori
# https://open.kattis.com/problems/shiritori
# TAGS: set
# CP4: 2.3d, Hash Table (set)
# NOTES:
N = int(input())

seen = set()
player = 1
last_letter = ''

for turn in range(1, N + 1):
    word = input()
    if word in seen or (word[0] != last_letter and turn > 1):
        print(f"Player {player} lost")
        break
    else:
        seen.add(word)
        last_letter = word[-1]
        if player == 1:
            player = 2
        else:
            player = 1
    if turn == N:
        print("Fair Game")