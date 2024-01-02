# Count The Vowels
# https://open.kattis.com/problems/countthevowels
# TAGS: basic
# CP4: 6.2c, Regular Expression
# NOTES:
"""
- tagged as regex in CP4 but not needed of course
"""
s = input()

print(sum(1 for c in s.lower() if c in {'a','e','i','o','u'}))

# alternative comprehension:
# print(sum(c in {'a','e','i','o','u'} for c in s.lower()))