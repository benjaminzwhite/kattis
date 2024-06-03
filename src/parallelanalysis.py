# Parallel Analysis
# https://open.kattis.com/problems/parallelanalysis
# TAGS: dict
# CP4: 2.3f, Hash Table (map), H
# NOTES:
"""
This is a straightforward exercise but, I am guessing, it has a 4.5+ difficulty due to the very confusing description.
(from reading guides to competitions, I understand that apparently some ICPC competitions are designed to have questions like this)

There are many components of the description that are NOT USED (it mentions e.g. "p the number of cores"
but this is not relevant to the task), meanwhile some of the important stuff like: "Assume that every instruction executes in one clock
tick, and that all cores share a single clock." is still not 100% clear and is buried in the reading comprehension O_o

---

Reformulation/explanation of what is being asked:

- You have a list of instructions (with very confusing input format: num_ops, [reads], write. Here '[reads]' are "addresses" you READ FROM, then 'write' is an address you write TO
- EACH "ENTIRE INSTRUCTION" (i.e. the individual lines that you process during the input() consisting of SEVERAL numbers) TAKES 1 SEC/TIME UNIT NO MATTER HOW LONG IT IS (!??! really not very intuitive, this is the bit in the description "Assume that every instruction executes in one clock tick")
- You have a super PC that in principle can handle everything in parallel: ignore details they are COMPLETELY IRRELEVANT
- The only bottleneck is, if an instruction LATER in the list must READ from an address that has been WRITTEN earlier in the list, then you must WAIT FOR THAT PARTICULAR INSTRUCTION (and any other earlier dependencies) TO BE PROCESSED FIRST

That's it, so just track last_time_address_is_written, that's all you need to do

---

I left some comments in code below at places where I was having doubts about my reading comprehension of the exercise task

"""
T = int(input())
for testcase in range(1, T + 1):

    n = int(input())

    last_time_address_is_written = {}

    finish_time = 1 # there is at least one instruction and ALL INSTRUCTIONS TAKE 1 sec O_o SO FINISH_TIME IS AT BEST = 1, might be later

    #curr_time = 0 # UPDATE: don't need to track this either

    for _ in range(n):
        #curr_time += 1
        #earliest_can_be_started = curr_time <-- NO !!! IT SEEMS LIKE THIS IS WRONG INTERPRETATION
        
        earliest_can_be_started = 0
        num_ops, *reads, write = map(int, input().split())

        #processing_time = num_ops <-- NO !!! UPDATE: IT'S NOT, IT'S ALWAYS 1 -> I THOUGHT WE'RE MOVING ACROSS THE READS AND SOMEHOW ZIPPING TO CHECK WHAT CAN BE DONE IN PARALLEL

        for r in reads:
            # afaict (after re-reading this stuff 1000 times) 
            # -> you can read IMMEDIATELY after all other previous writings have been carried out 
            # so the earliest_can_be_started is just the latest of all previous write events (AND NOT +1 which i was doing in first version)
            earliest_can_be_started = max(earliest_can_be_started, last_time_address_is_written.get(r, 0))

        # OK AFTER READING AGAIN: EACH INSTRUCTION TAKES 1 SECOND, SO ALL YOU ARE DOING IS "WAIT FOR ANY PREVIOUS ONES, THEN ADD 1 SECOND"
        # so say for example this current instruction requires 1 (or more, ITS IRRELEVANT) read from an address that is written previously
        # in the list:
        # then you must: wait for that address to be written, which occurs at time: earliest_can_be_started
        # then you must: wait +1 second SINCE ALL INSTRUCTIONS TAKE 1 second
        # then propagate this forwards for whatever the "end write address" is for this instruction (SINCE THAT'S THE PART THAT AFFECTS SUBSEQUENT INSTRUCTIONS)
        last_time_address_is_written[write] = earliest_can_be_started + 1 # ALL INSTRUCTIONS TAKE 1 SECOND

        finish_time = max(finish_time, last_time_address_is_written[write])

    print(testcase, finish_time)