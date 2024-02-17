# Doubleplusgood
# https://open.kattis.com/problems/doubleplusgood
# TAGS: brute force, bitmask
# CP4: 3.2f, Iterative (Combination)
# NOTES:
"""
CARE! You have some potential for -1/+1 indexing errors due to the fact you are doing
bitmask on the + operations, of which there are K, while there are K+1 numbers.

Implementation:

I split into head, *tail. This way, when we process bitmask we are always:
1) Starting with the head token
2) Either +:string_extending or +:integer_adding the i'th token of TAIL where I will range(number_of_operations) == range(number_of_tokens_in_TAIL)
"""
s = input()

operations = s.count('+')

# Suppose s = "1+9+8+4", then:
# head: '1', tail = ['9','8','4']
# -> always build from head token and try insert {} operation before each of the tail tokens
head, *tail = s.split('+')

res = set()

for mask in range(1 << operations): 
    expression = []
    token = head
    
    for i in range(operations):
        if mask & (1 << i):
            token += tail[i] # we say this {+} symbol is "extend token" e.g. tail[i] = '8', token '19' -> '198' 
        else:
            expression.append(token) # we say this {+} symbol is "integer add" so current token is finished
            token = tail[i]
    
    expression.append(token) # !!! remember to add the current token at the end since it has not been handled yet
    
    evaluate_expression = sum(map(int, expression))
    
    res.add(evaluate_expression)

print(len(res))