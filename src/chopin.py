# Preludes - alt kattis name: Chopin
# https://open.kattis.com/problems/chopin
# TAGS: basic
# CP4: 1.6e, Real Life, Easier
# NOTES:
import sys

PAIRS = [("A# Bb"), ("C# Db"), ("D# Eb"), ("F# Gb"), ("G# Ab")]

d = {}
for p in PAIRS:
    k, v = p.split()
    d[k] = v
    d[v] = k

c = 1
for line in sys.stdin:
    note, tonality = line.split()
    if note in d:
        print(f"Case {c}: {d[note]} {tonality}")
    else:
        print(f"Case {c}: UNIQUE")
    c += 1