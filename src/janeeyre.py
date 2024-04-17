# Jane Eyre
# https://open.kattis.com/problems/janeeyre
# TAGS: priority queue
# CP4: 2.3a, Priority Queue
# NOTES:
"""
Just 2 tricky things:

1) REMEMBER TO ADD JANE EYRE BOOK ITSELF TO THE PRIORITY QUEUE !!!

2) Input contains lines of the form "Name of book" num_pages <-- with the actual " characters in input
   So I take these inputs, split them, rejoin them to get "name of book", then add x[1:-1] to the priority queue IE REMOVE THE START AND END " CHARS
   Not sure if it's best practice, just always have problems with chars and reading in/escaping chars from OJ sites without being able to debug what's going on

Implementation notes: as far as the actual coding:
I store the arrivals in a SORTED LIST by ASCENDING TIME OF ARRIVAL, and tie break on ALPHABETICAL ORDER (IMPORTANT!!!)
Then, in the main loop I:
- finish reading current book -> += current time by how long it took
- now check if any new arrivals have been added to my "pile" i.e. minheap
- I do this by reading from the front of the arrivals list (which is sorted remember) all the entries whose arrival
  time is <= the new, updated, current time (i.e. after finishing latest book of X pages: curr_time += X) 

CARE! How you handle arrivals list: only add <= curr_time and ofc check that i_arrivals < len(arrivals)
"""
from heapq import heappush, heappop

n, m, k = map(int, input().split())

minheap = []
for _ in range(n):
    xs = input().split()
    name = ' '.join(xs[:-1])[1:-1]
    pages = int(xs[-1])
    heappush(minheap, (name, pages))
heappush(minheap, ("Jane Eyre", k)) # !!! remember to add this book in all cases O_o

arrivals = []
for _ in range(m):
    xs = input().split()
    time = int(xs[0])
    name = ' '.join(xs[1:-1])[1:-1]
    pages = int(xs[-1])
    arrivals.append((time, name, pages))

arrivals = sorted(arrivals, key = lambda t: (t[0], t[1])) # sort ASCENDING TIME , tie break on ASCENDING lexicographic order A,B,C.... booknames (this is default sorting behavior but nice to type out to remember the logic)
curr_time = 0
i_arrivals = 0

while True:
    # try adding all books which have arrival times <= whatever the current time is in this iteration of our loop
    while i_arrivals < len(arrivals) and arrivals[i_arrivals][0] <= curr_time:
        _, name, pages = arrivals[i_arrivals]
        heappush(minheap, (name, pages))
        i_arrivals += 1

    # else get the current book and read it - incremement time by curr_pages (and break if the book was Jane Eyre, we are done)
    curr_book, curr_pages = heappop(minheap)
    if curr_book == "Jane Eyre":
        curr_time += curr_pages
        print(curr_time)
        break
    else:
        curr_time += curr_pages