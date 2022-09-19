import asyncio
from datetime import datetime


async def deep_sleep(num, time):
    print(f"{num} - pre: {time}")
    await asyncio.sleep(time)
    print(f"{num} - post: {time}")


async def first():
    await asyncio.gather(
        deep_sleep("11", 1),
        deep_sleep("12", 2),
        deep_sleep("13", 0)
    )


async def second():
    await asyncio.gather(
        deep_sleep("21", 2),
        deep_sleep("22", 1),
        deep_sleep("23", 0)
    )


async def third():
    await asyncio.gather(
        deep_sleep("31", 2),
        deep_sleep("32", 0),
        deep_sleep("33", 1)
    )


async def loop():
    await asyncio.gather(
        first(),
        second(),
        third()
    )


if __name__ == '__main__':
    start = datetime.now()
    # asyncio.run(loop())
    asyncio.get_event_loop().run_until_complete(loop())
    print(f"total: {datetime.now() - start}")


# results:
# 11 - pre: 1
# 12 - pre: 2
# 13 - pre: 0
# 21 - pre: 2
# 22 - pre: 1
# 23 - pre: 0
# 31 - pre: 2
# 32 - pre: 0
# 33 - pre: 1
# 13 - post: 0
# 23 - post: 0
# 32 - post: 0
# 11 - post: 1
# 22 - post: 1
# 33 - post: 1
# 12 - post: 2
# 21 - post: 2
# 31 - post: 2
# total: 0:00:02.002305

