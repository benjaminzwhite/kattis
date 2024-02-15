# Count Doubles
# https://open.kattis.com/problems/countdoubles
# TAGS: array, range sum
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
You can brute force since n = 1000, even in Python; but below is a range sum approach that works for large n and m.

---

Implementation note:

There is potential for off-by-1 errors, as always with range sum type exercises, so I left print debug statements.

I initialize the evens_count to [0], so that I can refer to the previous value in the evens_count list.

Also this handles the "left side" of the window when sliding across the range sums.
"""
n, window_size = map(int, input().split())
xs = map(int, input().split())

evens_count = [0] # CARE! Initialize to [0] see Notes
for x in xs:
    if x % 2 == 0:
        evens_count.append(evens_count[-1] + 1)
    else:
        evens_count.append(evens_count[-1])

res = 0
for i in range(len(evens_count) - window_size): # NOTE THE UPPER RANGE AND ALSO LOWER RANGE - evens_count has 1 more element than xs, since first is [0] dummy to get the above loop started with evens_count[-1] operation
    #print(xs[i:i+window_size], evens_count[i:i+1+window_size])
    evens = evens_count[i + window_size] - evens_count[i]
    if evens >= 2:
        #print("THERE ARE AT LEAST 2 EVEN NUMBERS IN: ", xs[i:i+window_size]) <--- helps you see that you are indeed on the correct underlying xs interval for this given evens_count window
        res += 1

print(res)