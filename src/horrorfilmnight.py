# Horror Film Night
# https://open.kattis.com/problems/horrorfilmnight
# TAGS: greedy
# CP4: 3.4e, Non Classical, Easier
# NOTES:
"""
A bit unclear description imho:

When you encouter a film which both people like, E[ie] == M[im], then that RESETS the can_pick status:
both people can pick the next film since it considers that previous was disliked by no-one.
(I thought you had to track the previous "single person dislike" rather)

Code below is messy as I was getting WA until I interpreted exercise with the above requirement O_o

---

Other than that - it's greedy solution:

You can always +1 res if both people like the movie, else it always makes sense to increase +1 by the earliest film then toggle.
(imagine there are no == films; then the data is EEEMMMEMEMEEMMME so you ignore length of groups and just count how many
toggles there are - again this illustration is when there are no E==M situations, for simplicity)
"""
ne, *E = map(int, input().split())
ie = 0
nm, *M = map(int, input().split())
im = 0

E = sorted(E)
M = sorted(M)

e_can_pick, m_can_pick = True, True
res = 0
while ie < len(E) and im < len(M):
    if E[ie] == M[im]:
        # free, can always do
        res += 1
        ie += 1
        im += 1
        # UPDATE - getting WA: try if he means that this configuration RESETS the can_pick status??? reading comprehension exercise -.-
        e_can_pick = True
        m_can_pick = True
    elif E[ie] < M[im]:
        if e_can_pick:
            res += 1
            ie += 1
            e_can_pick = False
            m_can_pick = True
        else:
            ie += 1
    else:
        if m_can_pick:
            res += 1
            im += 1
            e_can_pick = True
            m_can_pick = False
        else:
            im += 1

if (ie < len(E) and e_can_pick) or (im < len(M) and m_can_pick):
    res += 1

print(res)