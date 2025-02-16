# Menu Updates
# https://open.kattis.com/problems/menuupdates
# TAGS: priority queue, interpreter
# CP4: 0, Not In List Yet
# NOTES:
"""
The difficulty is reading comprehension mainly: EVERY QUERY TAKES PLACE ON INCREASING DAY, 1 QUERY PER DAY

To reformulate statement a bit more clearly: the 'r' operation/replace just means "put back value in list of available values, but with a time delay"

In other words, if you see "r 6" on day 15 and the global delay is say 7, then it means that, IN 7 DAYS FROM NOW, the value 6 should be added back to the minheap
-> 7 days from now is 15+7 = day 22. 

So, on each day, before you try heappop() the min value, all you need to do is to first check if there are any vals that are on "cooldown" and
are ready to be inserted back into the minheap

So in the above example, on day 21 you would heappop() normally, and get whatever_curr_min is = say 123
Then on day 22, when you perform this "check for vals on cooldown" you would LOOK BACK to cooldown[22 - global_delay=7] i.e. cooldown[15]
and you would see that the value 6 had been placed on cooldown at that previous day, SO IS AVAILABLE ONCE AGAIN STARTING TODAY, So
before you do any other operations, you ADD 6 TO THE minheap AGAIN.

CARE! you do it before any subsequent processing because 6 may turn out to be smaller than the "current" minheap value otherwise

---

Implementation notes:

I got WA on first submit as I had the "if day-delay in cooldown... heappush" check WITHIN the op=='a' block

In fact, you should do this check REGARDLESS of the op=='a', i.e. always, on each day, check which previous values in c are now off cooldown
and ready to be added back to minheap
(this is why I said earlier it's confusing that each day is a day that passes, even for days where the query is 'r' -> reading comprehension O_o)
"""
from heapq import heappush, heappop, heapify

delay, days = map(int, input().split())

h = list(range(1, days + 10)) # 10 is sentinel
heapify(h)

cooldown = {}
for day in range(1, days + 1):
    op, *val = input().split()
    if day - delay in cooldown:
        heappush(h, *cooldown[day - delay])
    
    if op == 'a':
        # check if an item, which was previously placed on cooldown, is now available again:
        # it is available if it was added to cooldown{} more than |delay| days ago -> i.e. is day-delay a key in cooldown{}
        # If so, you can add it to heap - it may or may not be a lower value that will go to the front of the minheap, ready for use now
        curr_item = heappop(h)
        print(curr_item)
    else:
        cooldown[day] = [int(val[0])]