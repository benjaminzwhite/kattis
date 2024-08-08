# Bela
# https://open.kattis.com/problems/bela
# TAGS: basic, interpreter, dict
# CP4: 1.6a, Game (Card)
# NOTES:
N, B = input().split()

N = int(N)

# dominant suit
D = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
# not dominant
ND = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}

res = 0

for _ in range(4 * N):
    x = input()
    
    if x[1] == B:
        res += D[x[0]]
    else:
        res += ND[x[0]]

print(res)