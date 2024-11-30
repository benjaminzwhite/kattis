# Boiling Vegetables
# https://open.kattis.com/problems/vegetables
# TAGS: logic, priority queue
# CP4: 3.4d, Involving PQ
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/vegetables.md

(See also second solution approach involving priority queue)
"""
T, N = input().split()
T = float(T)
N = int(N)

weights = list(map(int, input().split()))

num_pieces = [1] * N

min_weight_piece = 0
max_weight_piece = 1e9

cnt = 0 # remember to take -1 for result since will always cnt+1 with above initial conditions

# should avoid division here and compare ming_weight_piece < ( max_weight_piece * T ) instead 
while (min_weight_piece / max_weight_piece) < T:
    cnt += 1
    min_weight_piece = 1e9
    max_weight_piece = 0
    i_to_update = -1

    # find the vegetable whose current pieces are the heaviest, and add +1 cut to it
    # e.g if a veg is 9kg and is currently being cut into 3 pieces, while another is 5kg and cut into 1 piece
    # then IT IS THE LATTER THAT HAS current pieces = 5/1 = 5kg that contributes the MAX WEIGHT PIECE
    # while the former is contributing pieces of weight 9/3 = 3kg
    # So the algorithm will take 2nd vegetable and instead of cutting into 1 piece, will cut it into 1+1 = 2pieces.
    for i, (veg_weight, veg_pieces) in enumerate(zip(weights, num_pieces)):
        min_weight_piece = min(min_weight_piece, veg_weight / veg_pieces)
        if (veg_weight / veg_pieces) > max_weight_piece:
            i_to_update = i
            max_weight_piece = (veg_weight / veg_pieces)
    
    num_pieces[i_to_update] += 1