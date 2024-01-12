# Thanos
# https://open.kattis.com/problems/thanos
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
"""
RANT:

I've solved a few similar exercises with a population growth, and where the problem asks to round down the resulting (non-integer)
number of people to an integer number.

THIS MAKES NO SENSE BECAUSE THEN THE R (annual growth factor) IS MEANINGLESS/SELF-INCONSISTENT/ILL-DEFINED:
(I know it's just an exercise, but people seem to think it's "clever" to "only have integer number of people" as a gotcha to
make people get WA submissions, but in fact it is the problem authors who don't understand their own mistake)

Illustration:

If a testcase has population = 100 and growth factor = 2.5%, then according to these kind of problems' logic, the answer should be:

Year 1 end population is 102.5 --> "hahaha you must round down here to 102 !!! No such thing as 0.5 people at the end of the year :^)"

WITHOUT REALISING THAT THIS THEREFORE INVALIDATES THE "CONSTANT" GROWTH FACTOR RETROACTIVELY

i.e. Here the resultant actual population change from 100 to 102 ACTUALLY CORRESPONDS TO A R = 2% GROWTH FACTOR NOT R = 2.5% ANYMORE, SO
THE RESULT IS SELF-INCONSISTENT WITH ITS OWN INPUT PARAMETERS.

This is because they are "putting the cart before the horse":

THE GROWTH FACTOR IS **ALWAYS DERIVED FROM A PHYSICALLY-MEANINGFUL, UNDERLYING DISCRETE INTEGER CHANGE IN POPULATION NUMBERS**, IT IS NOT
MEANINGFUL TO FIRST START WITH AN ARBITRARY GROWTH FACTOR AND TRY TO DERIVE AN INTEGER POPULATION FROM IT (because as illustrated above 
in many cases this will lead to self-inconsistent result).

(If you find it easier to think about, it's IMPOSSIBLE for a population of e.g. 7 people to grow 10% in a year, so these 2 variables
should never appear in a meaningful testcase, and therefore the "rounding" behavior should never be needed).

Note that this also applies to e.g. an average yearly growth rate of X% after 5 years for example, and then trying to derive the actual
population at the end of year 1, year 2, etc. using this X% average growth rate.

END RANT O_o
"""
T = int(input())

for _ in range(T):
    P, R, F = map(int, input().split())
    years = 0
    while F >= P:
        years += 1
        P = int(R * P) # see RANT above O_o
    print(years)