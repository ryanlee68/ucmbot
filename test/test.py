import aiohttp
import asyncio
from dateutil import parser
from dateutil.tz import *
import datetime

async def foo():
     async with aiohttp.ClientSession() as session:
        async with session.get('https://api.presence.io/ucmerced/v1/events/') as events:
            assert events.status == 200
            return await events.json()
# https://api.presence.io/ucmerced/v1/organizations/events/association-for-computing-machinery-uc-merced
# https://api.presence.io/ucmerced/v1/dashboard/events
# https://api.presence.io/ucmerced/v1/events/

loop = asyncio.get_event_loop()
obj = loop.run_until_complete(foo())
# date = obj[0]['startDateTimeUtc']
# date = obj[0]

# yourdate = parser.parse(date)
date = obj['upcomingEvents'][0]['startDateTimeUtc']
# LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
yourdate = parser.parse(date).replace(tzinfo=None)
print(yourdate)
# make a function that returns the amount of time before the lastest event
    # 1. requires getting the text from the link on line 8
    # 2. with that text, get the time that event is
    # 3. find difference between current time and that event time
d1 = datetime.datetime.now().replace(tzinfo=None)
# d2 = d1.astimezone()

c = yourdate - d1

print(f"Current time: {format(d1)}")
print(f"Event time: {format(yourdate)}")
print(f"Difference: {format(c)}")
# await foo()
# with open('hello.txt', 'r') as file:
#     print(file.read())
