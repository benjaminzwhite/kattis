# Alphabet Animals
# https://open.kattis.com/problems/alphabetanimals
# TAGS: graph, dict
# CP4: 2.4a, Graph Data Structures
# NOTES:
"""
In this current implementation, as you add each input animal to the dict with keys = first_letter_of_animal, there is the possibility
that the input WILL GO TO ITSELF e.g. EAGLE

-> The "win condition" is if you can name an animal which ends with a letter such that NO OTHER ANIMAL *STARTS WITH THAT LETTER*
-> This involves checking that "first_letter_d == []"
-> BUT, as seen in EAGLE example, you need to handle the case where eagle itself was added to 'e':['eagle']
-> since the next player can't reuse "eagle" as a guess, then you can enlarge the win condition implementation slightly:
   if first_letter_d == [] OR first_letter_d == [your_winning_guess] i.e. length 1 list 
   In the 2nd case what is happening is that the "only word with first letter = last letter of winnign guess" is the winning guess itself
   WHICH IS UNAVAILABLE TO NEXT PLAYER
-> so this mimics the win condition of next player not having ANY valid animal names.

(Note that this implementation avoids logic along the lines of "if all animals do not start with START_LETTER and guess != animal" etc)
"""
last_animal = input()

candidates = []
first_letter_d = {k:[] for k in "abcdefghijklmnopqrstuvwxyz"}

n = int(input())
for _ in range(n):
    s = input()
    if s[0] == last_animal[-1]:
        candidates.append(s)
    first_letter_d[s[0]].append(s)

if not candidates:
    print('?')
else:
    tmp = next((candidate for candidate in candidates if (first_letter_d[candidate[-1]] == [] or first_letter_d[candidate[-1]] == [candidate])), None)
    if tmp is None:
        print(candidates[0])
    else:
        print(tmp + '!')