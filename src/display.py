# Digital Display
# https://open.kattis.com/problems/display
# TAGS: basic, string
# CP4: 1.6n, Output Formatting, E
# NOTES:
"""
- Wants you to print 2 empty lines after each test, except for "end" input - no blank lines after that.

- Better practice would be to define e.g. R_ADD = "    +", R_BAR = "    |" etc. and fill in the dict
like that (more modifiable/futureproof) rather than retyping several times (this is how to code golf it also)

"""
D = {'1':["    +","    |","    |","    +","    |","    |","    +"],
     '2':["+---+","    |","    |","+---+","|    ","|    ","+---+"],
     '3':["+---+","    |","    |","+---+","    |","    |","+---+"],
     '4':["+   +","|   |","|   |","+---+","    |","    |","    +"],
     '5':["+---+","|    ","|    ","+---+","    |","    |","+---+"],
     '6':["+---+","|    ","|    ","+---+","|   |","|   |","+---+"],
     '7':["+---+","    |","    |","    +","    |","    |","    +"],
     '8':["+---+","|   |","|   |","+---+","|   |","|   |","+---+"],
     '9':["+---+","|   |","|   |","+---+","    |","    |","+---+"],
     '0':["+---+","|   |","|   |","+   +","|   |","|   |","+---+"],
     ':':[" "," ","o"," ","o"," "," "]}

while True:
    s = input()
    if s == "end":
        print("end")
        break

    for i in range(7):
        print('  '.join(D[c][i] for c in s))    
    print()
    print()