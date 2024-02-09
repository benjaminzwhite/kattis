# Image Processing
# https://open.kattis.com/problems/imageprocessing
# TAGS: array, nice
# CP4: 2.2c, 2D Array, Easier
# NOTES:
"""
Nice exercise, interesting - good practice for convolution and 2d array/matrix/submatrix access - also good for flatten / chain itertools.
Seems a bit underranked at 1.8 compared to other green exercises though (a few tricky things to get correct)

Below code should be self explanatory:
The row, col stuff is tricky to get the right indexes: basically here row, col is accessing all TOP_LEFT [row][col] within 
the image, so that you can then, from that TOP_LEFT, move M cells to the right and N cells down which represents the kernel area

---

Implementation notes:

HERE THE KERNEL AS GIVEN IS SUPPOSED TO BE FLIPPED ON ROWS AND COLUMNS, so what I do is: 
Instead of store Kernel as a N*M matrix, I just keep extending it so that it is already flattened
e.g. [[1,2],[3,4]] would be stored as [1,2,3,4] directly

Then, during the convolution step, you iterate through the submatrix row by row,
BUT ZIP IT WITH ^^^ THIS KERNEL[::-1] <-- BACKWARDS!!! which represents "flipping columns".
"""
from itertools import chain

H, W, N, M = map(int, input().split())

image = []
for _ in range(H):
    image.append(list(map(int, input().split())))

kernel = []
for _ in range(N):
    kernel.extend(list(map(int, input().split()))) # NEED TO LOOP THROUGH THIS BACKWARDS since rows and cols are flipped in problem statement

res = []
for row in range(H - N + 1):
    temp = []
    for col in range(W - M + 1):
        flatten = chain.from_iterable([[image[row + y][col + x] for x in range(M)] for y in range(N)]) # flatten the current N*M submatrix of image, so can zip with the (already flattened) N*M kernel (which we store as a single flattened list see above)
        convolution = sum(k * x for k, x in zip(kernel[::-1], flatten)) # CARE! Loop through kernel backwards due to flipped rows and cols
        temp.append(convolution)
    res.append(temp) # update after submitting: can just print(*temp) directly instead of storing all of them in a res list

for x in res:
    print(*x)