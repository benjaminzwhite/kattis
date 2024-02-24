# Scrolling Sign
# https://open.kattis.com/problems/scrollingsign
# TAGS: string
# CP4: 6.4a, String Matching
# NOTES:
"""
I strongly disagree with the interpretation of this exercise statement:

I tried 3-4 different submissions (while getting WA) because of ambiguity on how to handle inputs of the form ["cat","cat","cat","cat"]

Do you need to "see" 12 letters here or 3? After submitting all interpretations the ACCEPTED ANSWER IS 3 NOT 12.

That doesn't make sense to me from either:
1) the information theory view point ("cat" and "cat" * 100000 are different as messages - you don't "know" the string repeats until you see all the chars)
2) from advertising point of view given the problem context of an advert sign (if you pay money for NIKE * 100 to appear on Times Square the message is not just NIKE * 1) 
"""
T = int(input())

for _ in range(T):
    k, w = map(int, input().split())
    xs = []
    for _ in range(w):
        xs.append(input())

    overlap_sum = 0

    for l, r in zip(xs, xs[1:]):
        curr_overlap = next((k - i for i in range(k) if l[i:] == r[:k - i]), 0)
        overlap_sum += curr_overlap
    res = k * w - overlap_sum

    print(res)