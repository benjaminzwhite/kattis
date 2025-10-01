# Interval Cover
# https://open.kattis.com/problems/intervalcover
# TAGS: greedy
# CP4: 3.4a, Greedy (Classical)
# NOTES:
"""
It's just standard Interval Cover with weird input choices, use of floats, and you have to output WHICH intervals
are used in optimal solution BY USING THEIR INDEX *AS THEY APPEARED IN THE ORIGINAL INPUT ORDER* which is **NOT SORTED**

So you need to track in the xs[] the (left, right, original_idx_of_tuple)
"""
while True:
    try:
        A, B = map(float, input().split())
        n = int(input())
        xs = []
        for idx in range(n):
            a, b = map(float, input().split())
            xs.append((a, b, idx)) # need to track ORIGINAL indices i.e. before sorting

        xs = sorted(xs, key=lambda x:(x[0], -x[1]))
        #print(xs)
        i = 0
        curr_left = A
        rightmost = -float('inf')
        possible = True
        res = []
        while rightmost < B:
            possible = False
            curr_best_idx = None
            while i < n and xs[i][0] <= curr_left:
                #print(xs[i])
                if xs[i][1] >= rightmost:
                    curr_best_idx = xs[i][2]
                    rightmost = xs[i][1]
                    possible = True
                    
                i += 1
            if not possible:
                break
            else:
                res.append(curr_best_idx)
                curr_left = rightmost

        if not possible:
            print("impossible")
        else:
            print(len(res))
            print(*res)
    except:
        break