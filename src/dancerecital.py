# Dance Recital
# https://open.kattis.com/problems/dancerecital
# TAGS: DFS, precompute
# CP4: 3.2e, Iterative (Permutation)	
# NOTES:
"""
My bad variable names: can't remember why I used the variable name "MISMATCH" below - basically it's the INTERSECTION
i.e. how many members in common: between ABCXY and DXEFBZ we have X,B in both so "MISMATCH" is 2
Not a very good choice of variable names by me when I re-read submission.

---

Nice - I noticed that it's classified as 3.2e, Iterative (Permutation) in CP4 book, but in Python my first naive approach
(with brute force permutations) didn't work; maybe in faster language it's OK (or there is an optimization to implement)

So I tried to solve with DFS : DFS better than BFS, I presume, because since you get to "full sized" permutations earlier, you generate min_mismatch
values earlier, which then allows you to break earlier from subsequent attempts (i.e if you know that min_mismatch <= 5, then while DFS'ing if you
find any intermediate states with > 5 you can abandon and break early reducing unnecessary computation)
However, basic DFS still times out/TLE on tests 6/7

Better idea: PRECOMPUTE once the "mismatches" between all possible pairs of words in the input:
Since there are at most R=10 words, you create a 10x10 matrix so at most 100 calculations (that do not need to be repeated from now on)

(whereas, in the original approach, I was re-calculating mismatch(word1,word2) multiple times for every 10! permutation -> time out comes from here I guess)

Probably can return to permutations approach if you use the above precalculation step also

UPDATE: tried permutations approach, with precalculated MISMATCHES array, doesn't work: still times out -> you need the pruning from DFS it seems

---

Notes on DFS implementation - the stack is made up of tuples: ( last appended word index / total mismatch / set(indices used) )
you only need to track the last word's index (to compare with current one) if you also track ALL the indices used separately
then at each DFS step, you try adding all words that have NOT been used; you LOOKUP (see above, rather than compute each time) their mismatch
with the last appended word, then add this new word's index to the used() set.
"""
R = int(input())
xs = []
for _ in range(R):
    xs.append(input())
    
num_indices = len(xs) # realised that this is just R above, actually don't need it

stk = [] # last appended word_index / total mismatch / indices used
for i in range(num_indices): # INITIALIZE WITH ALL THE SINGLE WORDS
    stk.append((i, 0, set([i])))

min_mismatch = float('inf') # see above, mismatch is bad choice of words - we are counting something like "min total sum of pairwise overlaps"

# Precompute once the mismatch between all pairs of words using set intersection
# See note above this is MY BAD CHOICE OF VARIABLE NAMES
# e.g. between ABCXY and DXEFBZ we have X,B in both so "MISMATCH" is 2
MISMATCHES = [[len(set(xs[i]).intersection(set(xs[j]))) for i in range(num_indices)] for j in range(num_indices)]

while stk:
    curr_last_idx, curr_mismatch, curr_indices_used = stk.pop()
    if curr_mismatch >= min_mismatch:
        continue
    if len(curr_indices_used) == num_indices:
        min_mismatch = min(min_mismatch, curr_mismatch)
        continue

    for i in range(num_indices):
        if i not in curr_indices_used:
            mismatch_increase = MISMATCHES[curr_last_idx][i]
            new_indices_used = curr_indices_used | {i}
            stk.append((i, curr_mismatch + mismatch_increase, new_indices_used))

print(min_mismatch)