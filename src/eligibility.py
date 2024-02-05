# Eligibility
# https://open.kattis.com/problems/eligibility
# TAGS: datetime
# CP4: 1.4d, Multiple TC + Selection
# NOTES:
"""
Practice using datetime O_o

CARE! studies and born are the REFERENCE dates to compare to (earliest allowed start dates for elegible etc)
"""
import datetime

studies = datetime.datetime(2010, 1, 1)
born = datetime.datetime(1991, 1, 1)

n = int(input())

for _ in range(n):
    name, study, dob, courses = input().split()

    sy, sm, sd = map(int, study.split('/'))
    study = datetime.datetime(sy, sm, sd)

    by, bm, bd = map(int, dob.split('/'))
    dob = datetime.datetime(by, bm, bd)

    courses = int(courses)

    if study >= studies:
        print(name, "eligible")
        continue
    if dob >= born:
        print(name, "eligible")
        continue
    if courses > 40:
        print(name, "ineligible")
        continue
    print(name, "coach petitions")