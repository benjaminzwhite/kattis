# Musical Scales
# https://open.kattis.com/problems/musicalscales
# TAGS: array
# CP4: 1.6f, Real Life, Medium
# NOTES:
"""
Don't understand music or musical notation so did it with big variable names carefully etc O_o

Implementation:
Use a notes list that is duplicated 2x compared the real 12 notes; this is simple trick to handle wraparound indexing easily.
increments list corresponds to the pattern of tone/tone/semitone/tone/tone/tone/semitone (+2,+2,+1,+2,+2,+2,+1)
"""
n = input()
song = set(input().split())

# x2 notes to handle wraparound
notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
increments = [2, 4, 5, 7, 9, 11, 12]

res = []

# only iterate over the first 12 "real" notes in the duplicated notes list
for i, scale in enumerate(notes[:12]):
    allowed = [scale] + [notes[i + j] for j in increments]
    if all(x in allowed for x in song):
        res.append(scale)

if not res:
    print("none")
else:
    print(*res)