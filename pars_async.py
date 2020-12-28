import json
import asyncio
import aiohttp

async def request_data(url, subreddit):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            x = await resp.json()
            # заголовок
            ti = x['data']['children'][0]['data']['title']
            # ссылка
            li = x['data']['children'][0]['data']['permalink']
            d = dict(title=ti, link=li)
            # сборка dict с указанием subreddit
            dd = {subreddit : d, }
            return dd

async def main():
    reddits = {"python", "compsci", "microbork"}
    res = await asyncio.gather(*(request_data(f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5',
                                              subreddit) for subreddit in reddits))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())