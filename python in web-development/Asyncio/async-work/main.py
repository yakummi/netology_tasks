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

n = 40 # кол-во персонажей

async def main():
    for i in range(1, n+1):
        coroutine = get_swapi_people(i)
        result = await coroutine
        db.add_player(id_player=i,
                      birth_year=result['birth_year'],
                      eye_color=result['eye_color'],
                      films=result['films'],
                      gender=result['gender'],
                      hair_color=result['hair_color'],
                      height=result['height'],
                      homeworld=result['homeworld'],
                      mass=result['mass'],
                      name=result['name'],
                      skin_color=result['skin_color'],
                      species=result['species'],
                      starships=result['starships'],
                      vehicles=result['vehicles'])

if __name__ == '__main__':
    asyncio.run(main())