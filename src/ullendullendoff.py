# Úllen dúllen doff
# https://open.kattis.com/problems/ullendullendoff
# TAGS: basic
# CP4: 1.5a, 1D Character Array
# NOTES:
n = int(input())

names = input().split()

# The counting song has 13 words.
# The -1 is due to indexing/start counting 1st word but at index 0 in names
res = names[13 % n - 1]

print(res)