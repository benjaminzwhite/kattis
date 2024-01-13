# Eye of Sauron
# https://open.kattis.com/problems/eyeofsauron
# TAGS: basic, string
# CP4: 1.4i, Still Easy
# NOTES:
s = input()

l = len(s)

if l % 2 == 0 and s.index('(') == l // 2 - 1:
	print("correct")
else:
	print("fix")