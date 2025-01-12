# Palindrome Substring
# https://open.kattis.com/problems/palindromesubstring
# TAGS: string, dynamic programming
# CP4: 6.7b, Palindrome (Checking)
# NOTES:
"""
Solved with Manacher's algorithm - code is reused from elsewhere/toolbox hence the comments O_o
"""
def get_palindromes_manacher(s):
    palindromes = []
    PADDING_CHAR = '_'
    assert PADDING_CHAR not in s
    s = PADDING_CHAR.join(s)

    R, C = -1, -1 # Rightmost location of known palindromes, and its centre
    radius = [1] * len(s) # expansion radius around each char, can update with manacher step when you know you are in a palidnrome. INIT TO 1 since PADDING_CHARS between real chars
    for i in range(len(s)):
        if i <= R:
            # manacher optimization: use the fact that we are within a known palindrome, so look at the mirror imagine of i about the center, C
            # since the situation of the mirror char is the same as that of i
            mirror_i = C - (i - C)
            radius[i] = min(radius[mirror_i], R - i)
        
        l = i - radius[i]
        r = i + radius[i]
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # while curr_substring is a palindrome, try expand it:
            palindromes.append(s[l:r + 1].replace(PADDING_CHAR, ''))
            l -= 1
            r += 1
            radius[i] += 1

        # while loop overshoots so undo last step:
        l += 1
        r -= 1
        radius[i] -= 1

        # update manacher info if curr palindrome extends past previous rightmost palindrome endpoint, R: 
        if r > R:
            R, C = r, i

    return palindromes

# -- Queries --
while True:
    try:
        s = input()
        res = get_palindromes_manacher(s)
        for pal in sorted(set(p for p in res if len(p) > 1)):
            print(pal)
        print() # empty line
    except EOFError:
        break