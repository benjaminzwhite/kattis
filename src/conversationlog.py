# Conversation Log
# https://open.kattis.com/problems/conversationlog
# TAGS: sorting, dict
# CP4: 2.3f, Hash Table (map), H
# NOTES:
"""
Sorting requirement for output is: ordered from ***most to least*** used and, in case of a tie, in alphabetical order

How to implement to avoid a 2nd counting object that counts occurences of all words:
-> add all occurences of words to a defaultdict[word] WHERE YOU APPEND TO A LIST not a set
-> therefore the length of the list (which contains the names of the users who said that word, MAY BE REPEATED NAMES) counts the OCCURENCES OF THE WORD
-> then when you take set() of the list, you get the unique users who said that word
-> you want this len to be == len(set(all_users))  (this is the 2nd condition "a word that is used by all users")
"""
from collections import defaultdict

all_words = defaultdict(list)
all_users = set()

M = int(input())

for _ in range(M):
    user, *words = input().split()
    all_users.add(user)
    for word in words:
        all_words[word].append(user)

F = 0
for k in sorted(all_words.keys(), key = lambda x: (-len(all_words[x]), x)):
    if len(set(all_words[k])) == len(all_users):
        F = 1
        print(k)
if F == 0:
    print("ALL CLEAR")