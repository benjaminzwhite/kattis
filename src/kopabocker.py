# Buying Books
# https://open.kattis.com/problems/kopabocker
# TAGS: mathematics, combinatorics, brute force
# CP4: 0, Not In List Yet
# NOTES:
"""
It's brute force - I used meaningful variable names during the input to explain what is being recorded.

You have, for each shop, a fixed postage cost for any "BOOK ORDER" from that shop.
Then each shop has some subset of all books available to buy.

So encode this in a "shops_x_books" table: you know the max number of books so you can just access with indices
that shop[r][c] means shop r does or does not have book c available and, if so, what its cost is.

Implementation detail: if you initialize this table with float('inf'), it easily handles case where book is not available
because taking min() will give float('inf') on any book that is not avail, so it will never be taken as a real option.

Then the main logic is simple: instead of trying to be clever and choose a subset, then within subset choose whether or not
you pick at least 1 book from any given bookstore etc., instead I just TAKE ALL COMBINATIONS OF ALL SIZES OF BOOKSHOPS, and for a given
combination interpret this as being an order where AT LEAST ONE BOOK IS BOUGHT FROM ALL OF THE indices in the curr combination of shops: 

e.g. (0,2,3,7) means shop[0], [2], [3], [7] has AT LEAST ONE ORDER

this means that for each combo, the curr_order_cost is:
a) Firstly the sum of all the i shops' POSTAGE cost: postage[0], postage[2], postage[3], postage[7] then...
b) You iterate "COLUMN WISE" over these "four" (0,2,3,7 in this curr example) shops inventory:
   at each column j, i.e. for each BOOK, you take the min of all possible sales costs across these selected shops

Due to my init with float('inf'), if any column is entirely float('inf') <=> i.e. if some combination of shops leads to
you NOT HAVING A PARTICULAR BOOK j AVAILABLE ANYWHERE, then the total cost for that combination will be float('inf') so will be not taken.

---

Implementation notes:

I set everything to 1 based indexing hence in input() I take book_1_index which is 1,2,3... and convert it to 1-1,2-1,3-1 etc so book indices are j=0,1,2,3...

Also, CARE!: make sure you take all combinations but with AT LEAST 1 ELEMENT/BOOKSHOP !
"""
from itertools import combinations

num_books, num_shops = map(int, input().split())

shops_x_books = [[float('inf')] * num_books for _ in range(num_shops)]
postage = [0] * num_shops

for i in range(num_shops):
    shop_data, shop_postage = map(int, input().split())
    postage[i] = shop_postage

    for _ in range(shop_data):
        book_1_index, cost = map(int, input().split())
        # CARE: I will use 0 based indexing in the shops_x_books arr
        shops_x_books[i][book_1_index - 1] = cost

min_cost = float('inf')

for shops_used in range(1, num_shops + 1):
    for comb in combinations(range(num_shops), shops_used):
        curr_cost = 0
        for i in comb:
            curr_cost += postage[i]
        for j in range(num_books):
            tmp = float('inf')
            for i in comb:
                tmp = min(tmp, shops_x_books[i][j])
            curr_cost += tmp
        min_cost = min(min_cost, curr_cost)

print(min_cost)