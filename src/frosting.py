# Frosting on the Cake
# https://open.kattis.com/problems/frosting
# TAGS: logic, geometry, nice
# CP4: 7.2f, Quadrilaterals
# NOTES:
"""
You can permute rows and columns such that you form 3x3 "mega" regions

If you don't see it, do with a black and white chessboard -> can form 2x2=4 large squares black white grouping 
"""
n = int(input())

widths = list(map(int, input().split()))
heights = list(map(int, input().split()))

topl = sum(widths[::3]) * sum(heights[::3])
topm = sum(widths[1::3]) * sum(heights[::3])
topr = sum(widths[2::3]) * sum(heights[::3])

midl = sum(widths[::3]) * sum(heights[1::3])
midm = sum(widths[1::3]) * sum(heights[1::3])
midr = sum(widths[2::3]) * sum(heights[1::3])

botl = sum(widths[::3]) * sum(heights[2::3])
botm = sum(widths[1::3]) * sum(heights[2::3])
botr = sum(widths[2::3]) * sum(heights[2::3])

white = topl + midr + botm
brown = topm + midl + botr
pink = topr + midm + botl

print(brown, pink, white) # CARE! for the output order, I thought logical would be white brown pink given the l->r of the pattern