# Zipf's Song
# https://open.kattis.com/problems/zipfsong
# TAGS: sorting
# CP4: 2.2f, Sorting, Harder
# NOTES:
"""
Reading comprehension to understand description - description overloads the word "i'th song" and i index 
especially if you're thinking in terms of 0 indexing so it's hard to see clearly what is in what order

Basically:
You get a list labelled L=1,2,3....n
The Zipf score says its frequency should be proportional to z=1/L
If the quality metric is then q=actual_freq/zipf_freq then q is proportional to actual_freq/ (1/L) -> proportional to actual_freq * L

IN THE BELOW I'M USING i FOR L SINCE I WAS TRYING TO MATCH THE DESCRIPTION, just think of it as LABEL rather than 0 based index
"""
n, m = map(int, input().split())

xs = []
for i in range(1, n + 1): # nb, confusing after all the reading - z_i is proportional to 1/i so q = f/z is proportional to f/ (1/i) -> f*i
    f, s = input().split()
    f = int(f)
    xs.append((f * i, i, s)) # tiebreak is order of appearance i.e. increasing i

xs = sorted(xs, key=lambda x:(-x[0], x[1]))  # tiebreak is order of appearance i.e. increasing i which is stored in x[1]

for m_ in range(m):
    print(xs[m_][2])