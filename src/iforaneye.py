# An I for an Eye
# https://open.kattis.com/problems/iforaneye
# TAGS: dict, string
# CP4: 2.3f, Hash Table (map), H
# NOTES:
"""
Basically just do what the text says. Can make the code below DRYer since it's the same logic for 4,3,2.

CARE! you need to maintain the capitalization of the original.

---

Since you should prioritize higher length replacements if 2 are possible e.g. be and bee in "been"
-> therefore I iterate down in size from 4,3,2 since largest lookup in `d` is of length 4 and smallest is 2
-> then I update i += the length of replaced substring, so that you don't overwrite "new letters"
"""
d = {"at":"@", "and":"&", "one":"1", "won":"1", "to":"2","two":"2","too":"2","for":"4","four":"4","bea":"b","be":"b","bee":"b","sea":"c","see":"c","eye":"i","oh":"o","owe":"o","are":"r","you":"u","why":"y"}

n = int(input())

for _ in range(n):
    s = input()

    phrase = []
    for word in s.split():
        i = 0
        t = []
        while i < len(word):
            if word[i:i + 4].lower() in d:
                tmp = d[word[i:i + 4].lower()]
                if word[i].isupper():
                    tmp = tmp.capitalize()
                t.append(tmp)
                i += 3
            elif word[i:i + 3].lower() in d:
                tmp = d[word[i:i + 3].lower()]
                if word[i].isupper():
                    tmp = tmp.capitalize()
                t.append(tmp)
                i += 2
            elif word[i:i + 2].lower() in d:
                tmp = d[word[i:i + 2].lower()]
                if word[i].isupper():
                    tmp = tmp.capitalize()
                t.append(tmp)
                i += 1
            else:
                t.append(word[i])
            i += 1
        new_word = ''.join(t)
        phrase.append(new_word)

    print(' '.join(phrase))