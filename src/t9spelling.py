# T9 Spelling
# https://open.kattis.com/problems/t9spelling
# TAGS: cipher
# CP4: 1.6k, Cipher, Easier
# NOTES:
d = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777', 's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999', ' ': '0'}

N = int(input())

for case_num in range(1, N + 1):
    s = input()
    arr = []
    
    for c in s:
        if arr and arr[-1][0] == d[c][0]:
            # checks if this char is on same key as the previously added char by comparing the first digit of their associated code
            # e.g. a,b,c are on same key so their codes start with same digit (here 2)
            arr.append(' ')
        arr.append(d[c])
    
    res = ''.join(arr)
    
    print(f"Case #{case_num}: {res}")