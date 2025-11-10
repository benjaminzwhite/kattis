# Veður - Vindhraði
# https://open.kattis.com/problems/vedurvindhradi
# TAGS: basic
# CP4: 1.4i, Control Flow, Level 3
# NOTES:
xs = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6, float('inf')]
names = ['Logn', 'Andvari', 'Kul', 'Gola', 'Stinningsgola', 'Kaldi', 'Stinningskaldi', 'Allhvass vindur', 'Hvassvidri', 'Stormur', 'Rok', 'Ofsavedur', 'Farvidri']

y = float(input())
for i, x in enumerate(xs):
    if x >= y:
        print(names[i])
        break