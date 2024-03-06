# Genetic Search
# https://open.kattis.com/problems/geneticsearch
# TAGS: string, improve
# CP4: 6.4a, String Matching
# NOTES:
"""
TODO: IMPROVE - current approach is brute force, solve with better string matching approach

There are 3 types of sets to generate from a reference S, and then count how many times the members occur in a given string L.
"""
def count_substrings(substrings, size, s):
    res = sum(s[i : i + size] in substrings for i in range(len(s) - size + 1))
    return res

while True:
    x = input()
    if x == '0':
        break
    S, L = x.split()
    SIZE = len(S)

    # type 1 - just the string S itself
    res1 = count_substrings({S}, SIZE, L)

    # type 2 - generate all strings that you can obtain by 1 deletion from S
    type2set = set([S[:i] + S[i + 1 :] for i in range(len(S))])
    res2 = count_substrings(type2set, SIZE - 1, L)

    # type 3 - insert all chars ACGT into all positions of S
    type3set = set([S[:i] + c + S[i:] for c in 'ATCG' for i in range(len(S) + 1)])
    res3 = count_substrings(type3set, SIZE+1, L)

    print(res1, res2, res3)