# Matrix Inverse
# https://open.kattis.com/problems/matrix
# TAGS: basic, mathematics
# CP4: 5.2j, Really Ad Hoc
# NOTES:
case_number = 0

while True:
    try:
        case_number += 1
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        input() # blank line O_o
        
        det = a * d - b * c
        A, B, C, D = d // det, -b // det, -c // det, a // det
        print(f"Case {case_number}:")
        print(A, B)
        print(C, D)
    except EOFError:
        break