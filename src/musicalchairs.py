# Musical Chairs
# https://open.kattis.com/problems/musicalchairs
# TAGS: simulation, mathematics, nice
# CP4: 3.2j, Josephus Problem
# NOTES:
"""
CARE! with the indexing here - it's 1 based indexing and starts counting itself, so you get +/- 1 or 2 offby errors if you aren't careful

Failed first attempt due to TLE - didn't understand why; the reason after re-reading is that the k value (i.e. the number of shifts to perform)
can be huge like 10**6. So if you keep looping for each element you TLE, in Python at least.

The key to solving is that the "effective number of jumps to perform" is obtaininable by thinking modulo the number of remaining elements.
So initially if there are 5 elements and you are told to do e.g. 13 jumps, you only "really" need to do 13 % 5 = 3

Then after you remove whichever element you landed on, remember to update "remaining_n". This is the 'n' you use for the modulo calculations.

Meanwhile, the "original_n" is the one you use to look up the *actual* elements in the input list.
"""
original_n = int(input()) # this is HOW MANY ELEMENTS WERE ORIGINALLY IN THE LIST ks
ks = [(i + 1, k) for i, k in enumerate(map(int, input().split()))] # CARE! 1 based numbering of the professors

remaining_n = original_n # this will be the "size" of the people after each removal step, i.e. decremement by 1 each time you remove someone
i = 0 # we start on the INDEX 0 (note this is "Professor #1" due to 1 based numbering)
seen = set()

for _ in range(original_n):
    while i in seen: # keep moving ahead until we find the next remaining professor (mimics effect of deleting elements from actual list)
        i = (i + 1) % original_n
    jumps_to_perform = (ks[i][1] - 1) % remaining_n # -1 because WE COUNT THE INITIAL PROFESSOR HIMSELF (see description -.-) ! use REMAINING_N for modulo since here we mimic the eeny-meeny-minie-moe on the "remaining" people
    while jumps_to_perform:
        i = (i + 1) % original_n
        if i not in seen:
            jumps_to_perform -= 1
    seen.add(i)
    remaining_n -= 1

print(ks[i][0]) # i is the index which corresponds to index in ORIGINAL ks; so lookup which element is at index i in ks. [0] is because this is the (proffessor_number, k-value_of_that_professor) <-- we want [0] in this tuple