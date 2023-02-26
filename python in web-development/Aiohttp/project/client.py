import asyncio
from aiohttp import ClientSession

async def main():
    async with ClientSession() as session:
        response_post = await session.post('http://127.0.0.1:8080/advertisements/',
                                      json={'description': 'nice fghfhf',
                                           'owner': 'fgh',
                                            'header': 'gfhgf header2',
                                           })
        print(response_post.status)

        response_get = await session.get('http://127.0.0.1:8080/advertisements/1/')
        print(await response_get.json())




asyncio.run(main())
