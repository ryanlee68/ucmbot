from dataclasses import dataclass
import asyncio
import aiohttp
import time

# https://api.presence.io/ucmerced/v1/organizations/events/
# association-for-computing-machinery-uc-merced

# https://api.presence.io/ucmerced/v1/events/{uri}}
# https://api.presence.io/ucmerced/v1/events/flask-workshop-pt-2

loop = asyncio.new_event_loop()

async def get_events():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.presence.io/ucmerced/v1/'\
        'organizations/events/association-for-computing-machinery-uc-merced') \
        as resp:
            print(resp.status)
            await asyncio.sleep(2)
            # print([a["uri"] for a in await resp.json()])
            print(await resp.json())

# @dataclass
# class events:
#     pass

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(get_events())
# print(type(file[0]))
# for a in file: print(a["uri"])
# list = [a["uri"] for a in file]
# print(file)
print("hello")