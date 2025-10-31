# Peach Powder Polygon
# https://open.kattis.com/problems/peachpowderpolygon
# TAGS: logic
# CP4: 5.7a, Game Theory (Basic)
# NOTES:
"""
Parity/invariant consideration:

If you look at the N=6 case, the node 1 is connected to nodes
2,6 adjacent and 4 opposite i.e. all 3 of OPPOSITE parity to 1
Similarly for 2 which is connected to 1,3 and 5.

So in such a case: since both players start on opposite polarity
nodes, and they toggle to opposite polarity nodes to what they are
currently on, they can never meet.

This occurs when N//2 is ODD

Meanwhile if N//2 is EVEN then the "diagonal" vertex is of same parity
e.g. see then N=8 case where 1 is connected to 2,8 and 5

Here, then, the pursuer can find a strategy to get to a node of the correct parity eventually
"""
N = int(input())

if (N // 2) % 2 == 1:
    print("Yes")
else:
    print("No")