# Umm Code
# https://open.kattis.com/problems/ummcode
# TAGS: cipher, improve
# CP4: 6.2a, Cipher, Harder
# NOTES:
"""
TODO: IMPROVE - solved quickly, there might be better way to solve
"""
s = input()

xs = s.split()
goods = []
for x in xs:
    tmp = []
    flg = True
    for c in x:
        if c.isalnum():
            if c in 'um':
                tmp.append(c)
            else:
                flg = False
                break
    if flg:
        goods.extend(tmp)

res = []
for i in range(0, len(goods), 7):
    chunk = goods[i : i + 7]
    b = ''.join('1' if c == 'u' else '0' for c in chunk)
    n = int(b, 2)
    res.append(chr(n))

print(''.join(res))