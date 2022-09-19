import asyncio
from datetime import datetime


async def deep_sleep(num, time):
    print(f"{num} - pre: {time}")
    await asyncio.sleep(time)
    print(f"{num} - post: {time}")


async def deep_sleep_2(num, time):
    print(f"{num} - pre: {time}")
    await asyncio.sleep(time)
    print(f"{num} - post: {time}")


async def first():
    await deep_sleep("11", 1)
    await deep_sleep_2("12", 2)
    await deep_sleep("13", 0)


async def second():
    await deep_sleep_2("21", 2)
    await deep_sleep("22", 1)
    await deep_sleep("23", 0)


async def third():
    await deep_sleep("31", 2)
    await deep_sleep_2("32", 0)
    await deep_sleep("33", 1)


async def loop():
    await first()
    await second()
    await third()


if __name__ == '__main__':
    start = datetime.now()
    asyncio.get_event_loop().run_until_complete(loop())
    print(f"total: {datetime.now() - start}")


# results:
# 11 - pre: 1
# 11 - post: 1
# 12 - pre: 2
# 12 - post: 2
# 13 - pre: 0
# 13 - post: 0
# 21 - pre: 2
# 21 - post: 2
# 22 - pre: 1
# 22 - post: 1
# 23 - pre: 0
# 23 - post: 0
# 31 - pre: 2
# 31 - post: 2
# 32 - pre: 0
# 32 - post: 0
# 33 - pre: 1
# 33 - post: 1
# total: 0:00:09.012187
