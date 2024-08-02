# Delicious Bubble Tea
# https://open.kattis.com/problems/bubbletea
# TAGS: basic, array
# CP4: 1.4i, Still Easy
# NOTES:
N = int(input())

prices = map(int, input().split())

M = int(input())

toppings = list(map(int, input().split()))

can_mix = []

for i in range(N):
    K, *vals = map(int, input().split())
    can_mix.append(list(vals))

X = int(input())

min_price = float('inf')

for i, price in enumerate(prices):
    for cm in can_mix[i]:
        total = price + toppings[cm - 1]
        min_price = min(min_price, total)
        
print(max((X // min_price) - 1, 0))