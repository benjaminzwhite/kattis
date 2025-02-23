# Battleship
# https://open.kattis.com/problems/battleship
# TAGS: grid, interpreter
# CP4: 1.6d, Game (Others), Harder
# NOTES:
"""
It's just implementation really, however it has a weird indexing decision: uses x,y where y is INCREASING FROM BOTTOM ROW OF THE INPUT BOARDS
e.g. if input board has 4 rows and 6 cols, my logic for rows would be 0,1,2,3 in order of input() lines; but here the exercise calls them 3,2,1,0.

You also have to implement some stuff about subsequent guesses being misses, see comments in code below.

The only other thing (reading comprehension) is "THE NUMBER OF TURNS MUST BE THE SAME FOR BOTH PLAYERS".

So specifically: if  Player0 destroys Player1's last ship on Player0 turn; then Player1 HAS THE RIGHT TO RESPOND i.e. play their "last_turn"

This may or may not lead to Player1 in turn destroying all of Player0's ships (in which case: draw), or not (in which case Player0 will win and Player1 will lose)

However, if Player1 destroys Player0's last ship, then this last_turn DOES NOT TRIGGER since at that point Player0 and Player1 have both played same number of turns.
"""
T = int(input())

for _ in range(T):
    W, H, N = map(int, input().split())
    
    ships0, ships1 = set(), set()
    for h in range(H):
        for w, cell in enumerate(input()):
            if cell == '#':
                ships0.add((w, H - h - 1)) # this is to match the weird indexing convention (i.e. instead of using standard row/col)
    for h in range(H):
        for w, cell in enumerate(input()):
            if cell == '#':
                ships1.add((w, H - h - 1))

    d = {0: ships0, 1: ships1}

    commands = []
    for _ in range(N):
        commands.append(tuple(map(int, input().split())))

    # player 0 and player 1
    # NOTE: player0 goes first
    curr_player = 0
    cmd_idx = 0
    game_over = False
    last_turn = False
    while cmd_idx < len(commands) and not game_over:
        x, y = commands[cmd_idx]
        if (x, y) in d[1 - curr_player]:
            d[1 - curr_player].discard((x, y)) # remove the ship - he says "subsequent guesses where you've already hit a ship count as FAILS" <- this set discard implements this behavior as 2nd,3rd...guess will mean that x,y is NOT IN THE SET OF SHIPS -> will count as miss
            if len(d[1 - curr_player]) == 0:
                if curr_player == 0: # SEE NOTES: you only are allowed to prolong the game for the last_turn if it's PLAYER0 who destroys Player1's last ship: then Player1 has one last (set of) move(s) to try to DRAW.
                    last_turn = True
                    curr_player ^= 1
                else:
                    game_over = True
        else:
            if last_turn:
                game_over = True
            else:
                curr_player ^= 1

        cmd_idx += 1
    
    if len(d[0]) > 0 and len(d[1]) == 0:
        print("player one wins")
    elif len(d[1]) > 0 and len(d[0]) == 0:
        print("player two wins")
    else:
        print("draw")