# Ordinary Ordinals
# https://open.kattis.com/problems/ordinaryordinals
# TAGS: mathematics, recurrence
# CP4: 0, Not In List Yet
# NOTES:
"""
---- APPROACH 1 ----
1) Recursion for the braces (igoring the surrounding 2 braces):

n = 3 # <- for example given
acc = 0
prev = 0

for _ in range(n):
    curr = prev + 2
    acc += curr
    prev = acc

braces = acc + 2 # adding the 2 boundary braces
print(braces) # <----- 2**(n+1)

2) Same recursion for the commas but different I.C.:

n = 3 # <- for example given
acc = 1 # starting from n=2 term so have 1 , already
prev = 0

for _ in range(n-2):
    curr = prev + 2
    acc += curr
    prev = acc

commas = acc
print(commas) # <----- 2**(n-1) - 1

so total answer is braces + commas

res = braces + commas 

and we see that res = 2**(n+1) + 2**(n-1) - 1 for n>1 (due to initial condition in the commas calculation)

---- APPROACH 2, better: ----

if s1 = { {}, {{}} } then to get next term you
                  ^v____ insert 1x (,) here
        { {}, {{}} , .... }
                       ^v___ then insert 1x (copy of s1) here

        { {}, {{}} , {{}, {{}}} }
        __________ * ---------- _   

In above: __ is old s1, * is new comma, --- is copy of s1

So each step s2 has 2*|s1| + 1 chars (double len of prev + 1 char due to the , )
Initial condition needs to be s1={{}} otherwise doesnt handle the comma behavior
So res is 4, 2*4+1 = 9, 2*9+1 = 19, 2*19+1 = 39, etc.

--> solving rec gives 2**(n+1) + 2**(n-1) - 1 as before OK //

--> simplify  gives  4*2**(n-1) + 2**(n-1) - 1
-->                  5*2**(n-1) - 1 
"""
n, m = map(int, input().split())

if n == 0:
    print(2 % m)
else:
    res = (5 * pow(2, n - 1, m) - 1) % m
    print(res)