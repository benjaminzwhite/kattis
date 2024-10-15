# Adding Words
# https://open.kattis.com/problems/addingwords
# TAGS: dict, interpreter
# CP4: 2.3f, Hash Table (map), H
# NOTES:
"""
Description is a bit unclear:

if you have a definition first of e.g. fun = 2 then a later definition of fun = 7777, then YOU MUST DELETE: 

(1) the fun:2 k,v pair in d_keys_to_vals AND 
(2) the 2:fun k,v pair in d_vals_to_keys

so that you can assign the new k,v and v,k pairs without the previous value still remaining in the dicts

---

Implementation details:

I initialise d_keys_to_vals = {'+':'+', '-':'-', '=':''}, since I will create a string for eval(), I want
to REMOVE the = symbol in any valid string so that eval can produce the answer (= should not appear in eval(3+4=) for example, just eval(3+4))
- I use d_keys_to_vals.get(token, "FAIL_EVAL") with a Try/Except so that if a token doesnt appear in d_keys_to_vals, eval() will be
  called on something like eval(3 + FAIL_VAL) which will then fail with an Exception.
- "clear" means you reinitialize both dicts, of course the d_keys_to_vals needs to be re-seeded with the operation assignments though
"""
import sys

d_keys_to_vals = {'+':'+', '-':'-', '=':''}
d_vals_to_keys = {}

for line in sys.stdin:
    xs = line.split()
    if xs[0] == "clear":
        d_keys_to_vals = {'+':'+', '-':'-', '=':''}
        d_vals_to_keys = {}
    elif xs[0] == "def":
        if xs[1] in d_keys_to_vals: # SEE NOTES ABOVE - some tests have REDEFINITIONS OF PREVIOUSLY DEFINED VARIABLES, SO NEED TO REMOVE BOTH k,v and v,k PRIOR ASSIGMENTS IN BOTH DICTS
            val_to_delete = d_keys_to_vals[xs[1]]
            del d_keys_to_vals[xs[1]]
            del d_vals_to_keys[val_to_delete]
        d_keys_to_vals[xs[1]] = xs[2]
        d_vals_to_keys[xs[2]] = xs[1]
    elif xs[0] == "calc":
        tmp = ' '.join(d_keys_to_vals.get(token, "FAIL_EVAL") for token in xs[1:])
        try:
            res = str(eval(tmp))
            if res in d_vals_to_keys:
                print(' '.join(x for x in xs[1:]) + f" {d_vals_to_keys[res]}")
            else:
                print(' '.join(x for x in xs[1:]) + f" unknown")
        except:
            print(' '.join(x for x in xs[1:]) + f" unknown")