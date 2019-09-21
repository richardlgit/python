
with open("fpl-mia-2019-09-10.events-byinsert.txt", "r") as ef:
    eventids = {}
    didtype = {}
    didsubtype = {}
    eventcnt = 0
    events = ef.readline()
    while len(events) > 0:
        # print(events)

        eventlist = events.split()

        # print(eventlist)

        # for i, event in enumerate(eventlist):
        #     print(eventlist[i])
        eventid = int(eventlist[1])
        didtype[eventid] = eventlist[6]
        didsubtype[eventid] = eventlist[9]
        if eventid in eventids:
            eventids[eventid] = eventids[eventid] + 1
        else:
            eventids[eventid] = 1

        events = ef.readline()

    totalevents = 0
    print("Event Id, Did Type, Did Sub Type, Total Events")

    for event in sorted(eventids):
        print("{}, {}, {}, {}".format(
            event, didtype[event], didsubtype[event], eventids[event]))
        totalevents += eventids[event]

    print("Total Events: %d" % (totalevents))
ef.close()
