# Estimating the Area of a Circle
# https://open.kattis.com/problems/estimatingtheareaofacircle
# TAGS: basic, geometry
# CP4: 7.2c, Circles
# NOTES:
from math import pi

while True:
	r, m, c = input().split()
	if (r, m, c) == ('0','0','0'):
		break
	
	r = float(r)
	m = int(m)
	c = int(c)
	
	print(pi * r * r, 4 * c * r * r / m)