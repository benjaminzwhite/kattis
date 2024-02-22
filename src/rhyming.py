# Rhyming Slang
# https://open.kattis.com/problems/rhyming
# TAGS: string
# CP4: 6.2e, String Comparison
# NOTES:
common_word = input()

E = int(input())
groups = []
for _ in range(E):
    groups.append(input().split())

P = int(input())
for _ in range(P):
    word = input().split()[-1]
    flg = False
    for g in groups:
        if any(common_word.endswith(w) for w in g) and any(word.endswith(w_) for w_ in g):
            flg = True
            break
    if flg:
        print("YES")
    else:
        print("NO")