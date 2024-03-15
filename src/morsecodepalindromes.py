# Morse Code Palindromes
# https://open.kattis.com/problems/morsecodepalindromes
# TAGS: string, basic
# CP4: 0, Not In List Yet
# NOTES:
d = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

s = input()

m = ''.join(d[c.upper()] for c in s if c.isalnum())

if len(m) > 0 and m == m[::-1]:
    print(1)
else:
    print(0)