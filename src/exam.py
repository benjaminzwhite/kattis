# Exam
# https://open.kattis.com/problems/exam
# TAGS: logic, nice
# CP4: 6.3b, DP String, Non Classic
# NOTES:
"""
Nice little logic/reasoning exercise.

The max number you can get correct is determined by how many times you
agree and disagree with your friend's results:

Start with clearest example situation - the absolute best outcome would be that:
- all the places where you AGREE were answers your friend got correct
- all the places where you DISAGREE were answers your friend got wrong (so you got right)
This would give you 100% of correct answers overall.

All other cases are "intermediate" situations of the above - CARE! though, you need to
account for the fact that the number of correct might be < number of agrees etc (see the
min() logic in the result below - think about it with some examples if unclear).

(L - agree is number of disagree, L - correct is number of incorrect)
"""
correct = int(input())

s1 = input()
s2 = input()

L = len(s1)
agree = 0

for c1, c2 in zip(s1, s2):
    if c1 == c2:
        agree += 1
        
res = min(agree, correct) + min(L - agree, L - correct)

print(res)