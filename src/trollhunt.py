# Troll Hunt
# https://open.kattis.com/problems/trollhunt
# TAGS: mathematics
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
Reading comprehension: It's a "gotcha" question based on reading the story

Basically the "catch" is that the number of bridges from the input is the total number of all bridges in the world
and the troll HAS MOVED FROM ONE OF THEM to one of the b-1 others, SO THE "NUMBER OF b TO SEARCH" is input_b - 1 not input_b

IMHO the description is unclear and allows for a different interpretation of test case THAT IS MORE INTERESTING:
Based on first test case and taking b to == "b" input, you can explain the test case as follows:

There are b=5 possible bridges, so with 2 briges per day you eliminate 2, then 4, BUT ON DAY 2 YOU ONLY HAVE 1 brige leftover so TROLL MUST BE THERE
-> THIS IS *NOT* THE INTERPRETATION THEY WANT
"""
b, k, g = map(int, input().split())

b -= 1 # you include the bridge he is originally under -.-
num_groups = k // g

q, r = divmod(b, num_groups)

# my original approach had q + (r > 1) with b=b instead of b = b-1; this interpretation is that as long as leftover number
# of briges is 0 or 1, you know where the troll is on that day, otherwise you need another day to eliminate possibilities
print(q + (r > 0))