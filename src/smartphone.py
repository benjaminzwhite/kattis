# Smart Phone
# https://open.kattis.com/problems/smartphone
# TAGS: array, logic, string, nice
# CP4: 6.2e, String Comparison
# NOTES:
"""
Nice little exercise; my implementation trick makes the solution quite clean:

You have 1 "current typing" and 3 "suggestions" but you can just treat them as 4 "suggestions" as long as you make sure
that the first one DOES NOT INCUR THE +1 unit cost which you must pay for the real suggestions
(i.e set its cost to 0 effectively). 

Then the rest of the logic applies identically to these 4 options, you don't have to consider 2 different cases.

---

Rest of code should be clear:

For each suggestion check the length of the common prefix, then you delete to reach that common prefix then
add the correct letters to reach the target (See the comments below also)
"""
T = int(input())

for _ in range(T):
    best = float("inf")
    target = input()
    suggestions = []
    for _ in range(4):
        suggestions.append(input())

    # NOTE: the FIRST suggestion, i.e. sug_num == 0 index, is the CURRENTLY TYPED WORD - if you treat it as a "suggestion" it is special
    # as it DOEST NOT COST the extra +1 to take (unlike the other 3 "real" suggestions)
    # thus the (sug_num != 0) in the best cost calculation on last line 
    for sug_num, s in enumerate(suggestions):
    	# IMPORTANT - need to handle min(s), min(target) as your next() failure condition
    	# since its the SHORTEST of the 2 strings which determines what the best prefix length is:
        j = next((i for i, x in enumerate(s) if i < len(target) and x != target[i]), min(len(s), len(target)))

        # 3 OPERATIONS COST/BREAKDOWN FOR EACH SUGGESTION:
        # need to delete len(s) - j chars from the suggestion to get the prefix
        # need to type len(target) - j chars from the common prefix to reach the target word
        # need to pay 1 for taking a suggestion (unless the "suggestion" was in fact the currently typed word in which case you "pay 0")
        best = min(best, (len(s) - j) + (len(target) - j) + (sug_num != 0))

    print(best)