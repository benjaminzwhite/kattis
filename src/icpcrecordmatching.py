# ICPC Record Matching
# https://open.kattis.com/problems/icpcrecordmatching
# TAGS: dict
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
Basically just reading comprehension and input/parsing stuff
- annoying input format (don't know how many lines of each type so can't really append to correct lists after N/M inputs etc)
- you have to do case insensitive searching but case SENSITIVE printing, you have to sort outputs CASE INSENSITIVE etc etc

My code is not very DRY because I was expecting lots of debugging but it worked first submit

For optimizations, I think a single pass would work, since if you didn't pair off the I_DATA while iterating
through I_DATA, then any unpaired elements in O_DATA are therefore themselves going to be BAD_O since they do
not have a pairable k,v in I_DATA
"""
I_DATA, O_DATA, I_NAMES, O_NAMES = {}, {}, {}, {}

while True:
    l = input()
    if l == '':
        break

    fst, snd, email = l.split()
    I_DATA[email] = (snd, fst)
    I_NAMES[(snd.lower(), fst.lower())] = email

while True:
    try:
        l = input()
        fst, snd, email = l.split()
        O_DATA[email] = (snd, fst)
        O_NAMES[(snd.lower(), fst.lower())] = email
    except:
        break

# not very DRY O_o
BADS_I, BADS_O = [], []
for k, v in I_DATA.items():
    k_ = k.lower()
    v0_ = v[0].lower()
    v1_ = v[1].lower()
    if all(k_ != kk.lower() for kk in O_DATA) and all((v0_, v1_) != vv for vv in O_NAMES):
        BADS_I.append(('I', k, v[0], v[1]))

for k, v in O_DATA.items():
    k_ = k.lower()
    v0_ = v[0].lower()
    v1_ = v[1].lower()
    if all(k_ != kk.lower() for kk in I_DATA) and all((v0_, v1_) != vv for vv in I_NAMES):
        BADS_O.append(('O', k, v[0], v[1]))

if not BADS_I and not BADS_O:
    print("No mismatches.")
else:
    BADS_I = sorted(BADS_I, key=lambda x: x[1].lower()) # sort by lexicographic email order IGNORING CASE (reading comprehension)
    BADS_O = sorted(BADS_O, key=lambda x: x[1].lower())
    for t in BADS_I:
        print(*t)
    for t in BADS_O:
        print(*t)