# Support Vector Machine
# https://open.kattis.com/problems/svm
# TAGS: mathematics, geometry
# CP4: 7.2b, Lines
# NOTES:
"""
A bit overranked, it's just do what you are told.

I got error on first submit (I'm guessing lots of people do also hence the big difficulty rating) because after
all the reading, it uses n as input testcase and THE GIVEN TESTCASE HAS n QUERIES so I thought you are supposed to do:

for _ in range(n) -> input testcase

when in fact n is the size of the vectors xs and ws, and THE NUMBER OF TESTCASES IS ACTUALLY UNSPECIFIED

Instead of n testcases, you just keep inputting until end of file -.-
"""
def inner_product(v1, v2):
    return sum(x1 * x2 for x1, x2 in zip(v1, v2))

n = int(input())
*ws, b = map(float, input().split())

while True:
    try:
        xs = list(map(float, input().split()))

        d = (inner_product(ws, xs) + b) / inner_product(ws, ws) ** 0.5

        print(d)
    except EOFError:
        break