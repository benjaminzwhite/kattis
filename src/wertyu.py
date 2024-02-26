# WERTYU
# https://open.kattis.com/problems/wertyu
# TAGS: string, cipher
# CP4: 1.6e, Real Life, Easier
# NOTES:
"""
Got a WA on first submit, not sure why: not sure if I was failing due to \ escape char or maybe something else input related.

I added .strip() to the input() step and also handled the escaped \ char (\\ in Python) separately, then got AC.
"""
row1 = "`1234567890-="
row2 = "QWERTYUIOP[]\\" # <--- escape the \ ??? I tried r"QWE...." but doesnt seem to work as raw string O_o
row3 = "ASDFGHJKL;'"
row4 = "ZXCVBNM,./"

board = row1 + row2 + row3 + row4

while True:
    try:
        s = input().strip() # ???

        res = []
        for c in s:
            if c == ' ':
                res.append(' ')
            elif c == '\\': # ???
                res.append(']')
            else:
                i = board.find(c)
                res.append(board[i - 1])

        print(''.join(res))
    except EOFError:
        break