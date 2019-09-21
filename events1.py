# import gzip
# import urllib2
# import urlib.request
# import io
import requests

url = 'http://lorenzo.silverspringnet.com/monitor/fpl-mia/fpl-mia-2019-09-12/intermediate/fpl-mia-2019-09-12.events-byinsert.txt.gz'

# url = 'http://lorenzo.silverspringnet.com/monitor/pge/pge-2019-09-10/intermediate/pge-2019-09-10.events-byinsert.txt.gz'

#url = 'http://lorenzo.silverspringnet.com/monitor/aep/aep-2019-09-10/intermediate/aep-2019-09-10.events-byinsert.txt.gz'

# resp = urllib2.urlopen('http://lorenzo.silverspringnet.com/monitor/fpl-mia/fpl-mia-2019-09-10/intermediate/fpl-mia-2019-09-10.events-byinsert.txt.gz')

resp = requests.get(url, stream=True, timeout=10)

eventids = {}
didtype = {}
didsubtype = {}
eventcnt = 0

for events in resp.iter_lines():
    # print(events)

    # print(resp.con)

    # with gzip.open(resp, 'r') as ef:
    #   print(ef.read())

    if len(events) > 0:
        # print(events)

        eventlist = events.split()

        # print(eventlist)

        # for i, event in enumerate(eventlist):
        #     print(eventlist[i])
        eventid = int(eventlist[1])
        didtype[eventid] = int(eventlist[6])
        didsubtype[eventid] = int(eventlist[9])
        if eventid in eventids:
            eventids[eventid] = eventids[eventid] + 1
        else:
            eventids[eventid] = 1


totalevents = 0
print("Event Id, Did Type, Did Sub Type, Total Events")
totByDidType = {}

for event in sorted(eventids):
    print("{}, {}, {}, {}".format(
        event, didtype[event], didsubtype[event], eventids[event]))

    totalevents += eventids[event]

    if didtype[event] in totByDidType:
        totByDidType[didtype[event]] += eventids[event]
    else:
        totByDidType[didtype[event]] = eventids[event]

print("****** Summary by Did Type ********")
for didTypes in totByDidType:
    print("{} = {}".format(didTypes, totByDidType[didTypes]))

print("****** Total Events ********")
print("Total Events: %d" % (totalevents))

# ef.close()
