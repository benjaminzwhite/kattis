# Mixtape Management
# https://open.kattis.com/problems/mixtapemanagement
# TAGS: string, logic
# CP4: 0, Not In List Yet
# NOTES:
"""
Very difficult to understand the question, lots of unneeded details / reading comprehension:

How I would simply state exercise:

Generate any list of n distinct numbers such that the n elements are:
1) in sorted lexicographic order when viewed as strings, str()
2) and such that these numbers' values, i.e. when viewed as int(), match a given "rank list"

---

Many possible approaches, here is one that works with explainable logic:

First you create a dummy prefix of fixed length - here I take 9 followed by 100 zeroes (I pick '9' for easy debugging to make it clear what is being added/modified)
then right-insert values from an increasing series of numbers - you could pick from 13,17,1231,14141241 whatever you want - I just use 1,2,3,4 to keep it simple

So to be clear, we currently have elements of the form : '9' + 100 copies of '0' + ['1', '2', '3', ....]

If you stop here, you have a lexicographically sorted list since it's going to be:
90000[...]00001, 90000[...]00002, 90000[...]00003, etc. so we satisfy requirement (1) from exercise statement

Then for the requirement (2) "size-when-viewed-as-integer":
You append a NUMBER of 9's (again, dummy value - you can pick whatever you want) proportional to the RANK that this new string should appear in.

e.g. if you want 90000[...]000013 (which is 13th in LEXICOGRAPHIC ORDER) to appear in 47th NUMERICAL ORDER then:

-> append 47 copies of 9's at the end of the string, which ensures it will be the 47th smallest of all the values
since e.g. the 46th smallest will only have 46 9's etc.
(if you find it easier : think about using '0' as this suffix instead of '9' to see why each subsequent number is bigger and bigger)
"""
_ = input()

xs = input().split()

res = []
for i, x in enumerate(xs, 1):
    prefix = '9' + str(i).zfill(100) # the i in the prefix will handle the LEXICOGRAPHIC order property
    size = '9' * int(x) # the number of 9's after the fixed length prefix above will handle the NUMERIC order property
    res.append(prefix + size)

print(' '.join(res))