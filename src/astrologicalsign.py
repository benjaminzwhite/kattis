# Astrological Sign
# https://open.kattis.com/problems/astrologicalsign
# TAGS: basic, logic
# CP4: 1.4d, Multiple TC + Selection
# NOTES:
"""
I convert input of the form "dd MONTH_FIRST_3_LETTERS" to the actual day of the year (365 days assumed)
Then for each star sign, find the first day of the year that "opens" that star sign's interval e.g. Aries starts on day 80, Taurus on 111
Then for each input, convert that day to number, lookup the LARGEST NUMBER IN d THAT IS <= THAT NUMBER
-> that is the opening day for the corresponding star sign

Implementation note:
Edge case for CAPRICORN due to wrap around (dec-jan)
-> Capricorn includes 1-20 jan. So if day of year < 21 i.e. is 1-20, then map it to "end of december" part of Capricorn i.e. number 356
"""
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

d = {21:"Aquarius", 51:"Pisces", 80:"Aries", 111:"Taurus", 141:"Gemini", 173:"Cancer", 204:"Leo", 235:"Virgo", 265:"Libra", 296:"Scorpio", 327:"Sagittarius", 356:"Capricorn"}

t = int(input())

for _ in range(t):
    s = input()

    x, m = s.split()
    x = int(x)

    day_of_year = x + sum(DAYS[:MONTHS.index(m)])
    if day_of_year < 21:
        day_of_year = 356

    res = max(k for k, v in d.items() if k <= day_of_year)

    print(d[res])