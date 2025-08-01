# A Flea on a Chessboard
# https://open.kattis.com/problems/fleaonachessboard
# TAGS: logic, grid
# CP4: 5.2g, Grid
# NOTES:
import sys

for l in sys.stdin:
    S, x, y, dx, dy = map(int, l.split())
    if S == x == y == dx == dy == 0:
        break

    S2 = 2 * S

    def whitesquare(x, y):
        return (S < x < S2 and 0 < y < S) or (0 < x < S and S < y < S2) # has to be STRICTLY inside boundaries, reading comprehension

    moves = 0
    start_x, start_y = x % S2, y % S2
    x_, y_ = x % S2, y % S2
    while True:
        if whitesquare(x_, y_):
            print(f"After {moves} jumps the flea lands at ({x + moves * dx}, {y + moves * dy}).")
            break
        moves += 1
        x_ = (x_ + dx) % S2
        y_ = (y_ + dy) % S2
        if (x_, y_) == (start_x, start_y): # returned to an equivalent location modulo the grid pattern, so infinite cycle commences -> cannot escape
            print("The flea cannot escape from black squares.")
            break