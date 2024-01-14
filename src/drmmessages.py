# DRM Messages
# https://open.kattis.com/problems/drmmessages
# TAGS: basic, cipher
# CP4: 1.6k, Cipher, Easier
# NOTES:
"""
- simple do as you are told

- left full version for clarity; here in comment is a simplified version
without creating extra lists etc:

s = input()

l = len(s)

left, right = s[:l//2], s[l//2:]
rotate_val_l = sum(ord(x) - 65 for x in left)
rotate_val_r = sum(ord(x) - 65 for x in right)

res = []
for cl, cr in zip(left, right):
	o_l = ord(cl) - 65
	new_c_l = chr((o_l + rotate_val_l) % 26 + 65)
	new_o_l = ord(new_c_l) - 65

	o_r = ord(cr) - 65
	new_c_r = chr((o_r + rotate_val_r) % 26 + 65)
	new_o_r = ord(new_c_r) - 65

	new_o = (new_o_l + new_o_r) % 26
	res.append(chr(new_o + 65))

print(''.join(res))
"""
s = input()

l = len(s)

left, right = s[:l//2], s[l//2:]
rotate_val_l = sum(ord(x) - 65 for x in left)
rotate_val_r = sum(ord(x) - 65 for x in right)

tmp_l = []
for c in left:
    o = ord(c) - 65
    new_c = chr((o + rotate_val_l) % 26 + 65)
    tmp_l.append(new_c)

tmp_r = []
for c in right:
    o = ord(c) - 65
    new_c = chr((o + rotate_val_r) % 26 + 65)
    tmp_r.append(new_c)

res = []
for l, r in zip(tmp_l, tmp_r):
    o_l, o_r = ord(l) - 65, ord(r) - 65
    new_o = (o_l + o_r) % 26
    res.append(chr(new_o + 65))

print(''.join(res))