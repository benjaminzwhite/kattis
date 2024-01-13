# Pizza Hawaii
# https://open.kattis.com/problems/pizzahawaii
# TAGS: set
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
- really weird output requirement: you need TO OUTPUT A STRING WITH THE ( and ) AS CHARS

---

Variables explanation:

- foreign, english = foreign, english ingredient names SETS
- d_foreign, d_english = dictionaries of Foreign and English ingredients, with the values being the pizza names, pizza_name, that these ingredients appear in
- then the logic at the end if that:
if d_foreign[f] == d_english[e] (i.e. the set of pizza names are the same for a foreign and an english ingredient name,
then that foreign <-> english ingredient name pairing is possible
-> so can append the tuple (f,e) to results)
- finally, sort results alphabetically and print with the weird ( and ) char formatting O_o
"""
from collections import defaultdict

T = int(input())

for t in range(1, T+1):
    n_pizzas = int(input())
    
    foreign, english = set(), set()
    d_foreign, d_english = defaultdict(set), defaultdict(set)
    
    for _ in range(n_pizzas):
        pizza_name = input()
        _, *foreign_ingredients = input().split()
        for fi in foreign_ingredients:
            foreign.add(fi)
            d_foreign[fi].add(pizza_name)
        _, *english_ingredients = input().split()
        for ei in english_ingredients:
            english.add(ei)
            d_english[ei].add(pizza_name)
            
    res = []
    for f in foreign:
        for e in english:
            if d_foreign[f] == d_english[e]:
                res.append((f, e))
    
    res = sorted(res, key = lambda x: (x[0], x[1])) # Update after submit: think this is default Python sort behaviour so can remove sort key
    for f, e in res:
        print(f"({f}, {e})") # formatting output O_o
    
    if t != T:
        print()