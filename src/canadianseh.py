# Canadians, eh?
# https://open.kattis.com/problems/canadianseh
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
s = input()

if s[-3:] == "eh?":
	print("Canadian!")
else:
	print("Imposter!")