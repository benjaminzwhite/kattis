# Problem Classification
# https://open.kattis.com/problems/problemclassification
# TAGS: dict
# CP4: 2.3h, Balanced BST (map)
# NOTES:
"""
NOTES: code below isn't very optimized because I couldn't work out the output wanted for the case where there are NO matches, and didn't simplify after getting AC.

So I just submitted different versions until i got right answer: it turns out that if no category has any matches, you output all the categories in alphabetical order.

Implementation note:

NOTE THAT THIS WAS CAUSING MY PYTHON IMPLEMENTATION TO "FAIL" BECAUSE WITH DEFAULTDICT IF YOU DON'T SET CATEGORY_COUNT[categ] = 0 AS YOU ENCOUNTER
EACH CATEGORY IN THE INPUT YOU WILL NEVER POPULATE THE CATEGORY_COUNT DICT DURING ITERATING THROUGH THE MAIN TEXT, SO NO RECORD OF THE CATEGORIES THEMSELVES

-> So basically the "fix" is to initialize category_count[categ] = 0 while inputting, so you can output all of them in this testcase
"""
from collections import defaultdict

word_to_category = defaultdict(list)
category_count = defaultdict(int)

N = int(input())

for _ in range(N):
    categ, _, *words = input().split()
    category_count[categ] = 0 # see comment above why you have to initialize category_count to 0; you need to handle the case of 0 matches
    for word in words:
        word_to_category[word].append(categ)

while True:
    try:
        l = input()
        ws = l.split()
        for w in ws:
            if w in word_to_category:
                for c in word_to_category[w]:
                    category_count[c] += 1
    except:
        break

most_common = 0
for k, v in category_count.items():
    if v > most_common:
        most_common = v

if most_common == 0:
    for k in sorted(category_count.keys()):
        print(k)
else:
    for k in sorted(category_count.keys()):
        if category_count[k] == most_common:
            print(k)