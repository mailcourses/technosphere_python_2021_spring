import asyncio
import aiohttp
import time


URL = "https://loremflickr.com/320/240"


async def download(url, session):
    async with session.get(url, allow_redirects=True) as resp:
        data = await resp.read()
        with open(f"photo_{time.time()}", "wb") as f:
            f.write(data)


async def run():
    t1 = time.time()
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            await download(URL, session)

    t2 = time.time()
    print("single", t2 - t1)

    tasks = []
    t1 = time.time()
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(download(URL, session)))
        await asyncio.gather(*tasks)

    t2 = time.time()
    print("gather", t2 - t1)


if __name__ == "__main__":
    asyncio.run(run())
