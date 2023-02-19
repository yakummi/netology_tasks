import asyncio
from aiohttp import ClientSession

async def main():
    async with ClientSession() as session:
        response_get = await session.get('http://127.0.0.1:8080/advertisements/',
                                         json={'advertisement_id': 1})
        response_post = await session.post('http://127.0.0.1:8080/advertisements/',
                                      json={'description': 'nice desc2',
                                           'owner': 'yakummi2',
                                            'header': 'youtube header2',
                                           })
        print(response_get.status)



asyncio.run(main())
