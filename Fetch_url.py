import asyncio
import aiohttp


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                raise Exception(f'{response.status}')

async def main():
    content = await fetch_url("https://www.jetbrains.com/ru-ru/pycharm/buy/?fromIDE=&section=personal&billing=yearly")
    print(content) #


asyncio.run(main())