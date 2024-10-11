# Competitive Arcade Basketball
# https://open.kattis.com/problems/competitivearcadebasketball
# TAGS: dict
# CP4: 2.3e, Hash Table (map), E
# NOTES:
"""
Unclear description IMHO - I kept failing the last test, couldn't figure out why:

It seems it's because THERE IS A TEST CASE WHERE A PLAYER WHO HAS ALREADY WON THE REQUIRED NUMBER OF
POINTS *CONTINUES PLAYING* AND SO REPEATEDLY TRIGGERS THE "Player X wins!" BUT IT SEEMS (FROM TRYING
THE ALTERNATIVE) THAT YOU AREN'T EXPECTED TO KEEP REPRINTING THE WINNER MESSAGE FOR THAT PLAYER.

So all you have to do is create a winners set() and only print each winner once.

(there is no output explanation/sample test with this expected behavior being shown/illustrated)
"""
from collections import defaultdict

n, p, m = map(int, input().split())

for _ in range(n):
    tmp = input()

d = defaultdict(int)
winners = set()

for _ in range(m):
    player, score = input().split()
    d[player] += int(score)
    if d[player] >= p:
        if player not in winners:
            print(f"{player} wins!")
        winners.add(player)

if not winners:
    print("No winner!")