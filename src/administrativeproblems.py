# Administrative Difficulties
# https://open.kattis.com/problems/administrativeproblems
# TAGS: dict, interpreter
# CP4: 2.3h, Balanced BST (map)
# NOTES:
"""
Very frustrating (hence ALLCAPS comments below lol) the exercise is simple but I got WA for many submits; I'm still not
sure why, but my exact original solution (after trying different things to debug like sorting lists etc.) worked when
I implemented a DIY ceiling function:

q, r = divmod(x, 100)
increment by q , and add 1 if r != 0 to get the "round up behavior" and this was AC.

Note that the above will generate Python FLOATS not INTS (math.ceil generates ints) so e.g. will return for 1247.873
13.0 rather than 13; not sure if this is the origin of the problem or if it makes an actual mathematical difference
in some edge cases, in which case the wording of "rounding up" is not very clear to me.
"""
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    CARS = {}
    EVENTS = [] # UPDATE AFTER SUBMIT - THIS ISN'T NEEDED, I WAS DOIGN THIS WHILE DEBUGGING - EVENTS ARE INDEED IN CORRECT ORDER ALREADY
    AGENTS = {}

    # input n cars
    for _ in range(n):
        car = input()
        car_name, price, pickup, cost_per_km = car.split()
        CARS[car_name] = {"price":int(price), "pickup":int(pickup), "cost_per_km":int(cost_per_km)}

    # input m events - add to EVENTS, but also seed the AGENTS dict with the names and default properties of agents as you encounter them
    # UPDATE AFTER SUBMIT - THIS ISN'T NEEDED, I WAS DOIGN THIS WHILE DEBUGGING - EVENTS ARE INDEED IN CORRECT ORDER ALREADY
    # UPDATE USE EVENTS LIST AND APPEND IN ORDER OF THE INPUTS() SINCE DESCRIPTION SAYS THEY ARE IN CHRONOLOGICAL ORDER
    # -> im trying to debug, maybe error occurs when multiple events share same time? So input() order tells you which one is "first" e.g. if 2 events occur at t=123?
    for _ in range(m):
        event = input()
        time, agent, action, car_name = event.split()
        EVENTS.append((agent, action, car_name))
        if agent not in AGENTS:
            AGENTS[agent] = {"car_name":"", "total_cost":0, "inconsistent":False}

    # process the EVENTS in chronological order
    # UPDATE AFTER SUBMIT - THIS ISN'T NEEDED, I WAS DOIGN THIS WHILE DEBUGGING - EVENTS ARE INDEED IN CORRECT ORDER ALREADY
    # SO WHAT IS THE POINT OF HAVING THE time VARIABLE IN INPUTS SINCE IT IS NEVER USED???? EVERYTHING ALREADY IN ORDER
    for event in EVENTS:
        agent, action, car_or_cost = event # 3rd element of tuple can be: a CAR_NAME if p, or a COST_% if a, or a TOTAL_KM if r.
        if action == 'p':
            # check for inconsistency first:
            if AGENTS[agent]["car_name"] != "" or (car_or_cost not in CARS): # if they dont have 0 cars then pickup is inconsistent [2nd or statement isnt needed I think, I added during debugging]
                AGENTS[agent]["inconsistent"] = True
            if AGENTS[agent]["inconsistent"] == False:
                AGENTS[agent]["car_name"] = car_or_cost
                AGENTS[agent]["total_cost"] += CARS[car_or_cost]["pickup"]
        elif action == 'r':
            # check for inconsistency
            if AGENTS[agent]["car_name"] == "": # if they dont have a car then return is inconsistent
                AGENTS[agent]["inconsistent"] = True
            if AGENTS[agent]["inconsistent"] == False:
                curr_car = AGENTS[agent]["car_name"]
                to_add = int(car_or_cost) * CARS[curr_car]["cost_per_km"]
                AGENTS[agent]["total_cost"] += to_add
                AGENTS[agent]["car_name"] = ""
        elif action == 'a':
            if AGENTS[agent]["car_name"] == "": # if they dont have a car then accident is inconsistent
                AGENTS[agent]["inconsistent"] = True
            if AGENTS[agent]["inconsistent"] == False:
                curr_car = AGENTS[agent]["car_name"]
                to_add =  int(car_or_cost) * CARS[curr_car]["price"] 
                q, r = divmod(to_add, 100) # UPDATE AFTER SUBMIT - HAVE TO DO DIY CUSTOM CEIL() FUNCTION TO GET AC ??!?!?!?
                AGENTS[agent]["total_cost"] += q
                if r:
                    AGENTS[agent]["total_cost"] += 1


    # IMPLEMENT THIS REQUIREMENT:
    # "A spy will always return a car they picked up."
    # IE MAKE SURE AGENT HAS car_name == "" AT THE END OF THE EVENTS
    # Then check for INCONSISTENT boolean
    for agent, details in sorted(AGENTS.items()):
        if details["car_name"] != "":
            details["inconsistent"] = True
        if details["inconsistent"] == False:
            print(agent, details["total_cost"])
        else:
            print(agent, "INCONSISTENT")