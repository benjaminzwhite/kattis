# A New Alphabet
# https://open.kattis.com/problems/anewalphabet
# TAGS: cipher, dict
# CP4: 1.6k, Cipher, Easier
# NOTES:
"""
Careful, need to escape a few characters like ' and \
"""
d = {'a':'@', 'b':'8', 'c':'(', 'd':'|)', 'e':'3', 'f':'#', 'g':'6', 'h':'[-]', 'i':'|', 'j':'_|', 'k':'|<', 'l':'1', 'm':'[]\\/[]','n':'[]\\[]','o':'0','p':'|D','q':'(,)','r':'|Z','s':'$','t':'\'][\'','u':'|_|','v':'\\/','w':'\\/\\/','x':'}{','y':'`/','z':'2'}

s = input()

res = ''.join(d.get(c, c) for c in s.lower())

print(res)