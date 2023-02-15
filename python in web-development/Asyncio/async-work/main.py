import aiohttp
import asyncio
from database import db

URL = 'https://swapi.dev/api/people/'

async def get_swapi_people(people_id):
    session = aiohttp.ClientSession()
    response = await session.get(url=URL+str(people_id)+'/')
    response_json = await response.json()
    await session.close()
    return response_json

n = 10 # кол-во персонажей

async def insert_people(people_chunk, id):
    db.add_player(id_player=id,
                  birth_year=people_chunk['birth_year'],
                  eye_color=people_chunk['eye_color'],
                  films=people_chunk['films'],
                  gender=people_chunk['gender'],
                  hair_color=people_chunk['hair_color'],
                  height=people_chunk['height'],
                  homeworld=people_chunk['homeworld'],
                  mass=people_chunk['mass'],
                  name=people_chunk['name'],
                  skin_color=people_chunk['skin_color'],
                  species=people_chunk['species'],
                  starships=people_chunk['starships'],
                  vehicles=people_chunk['vehicles'])

async def main():
     for i in range(1, n):
         coroutine = get_swapi_people(i)
         result = await coroutine
         await insert_people(result, i)

if __name__ == '__main__':
    asyncio.run(main())
