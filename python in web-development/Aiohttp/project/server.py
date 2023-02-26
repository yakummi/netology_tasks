from aiohttp import web
from sqlalchemy import Column, Integer, String, func, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import json


PG_DSN = 'postgresql+asyncpg://app:secret@127.0.0.1:5431'
engine = create_async_engine(PG_DSN)
Session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

class Advertisements(Base):
    __tablename__ = "advertisements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    owner = Column(String, unique=True, index=True)
    header = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())


app = web.Application()

async def orm_context(app: web.Application):
    print('Server successfully started!')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()
    print('Server successfully stopped!')

@web.middleware
async def session_middleware(requests: web.Request, handler):
    async with Session() as session:
        requests['session'] = session
        return await handler(requests)

app.cleanup_ctx.append(orm_context)
app.middlewares.append(session_middleware)

async def get_advertisement(advertisement_id: int, session: Session):

    advertisement = await session.get(Advertisements, advertisement_id)

    if advertisement is None:
        raise web.HTTPNotFound(text=json.dumps({
            'status': 'Error',
            'message': 'We could not find this advertisement'
        }), content_type='application/json')

    return advertisement

class AdvertisementView(web.View):
    async def get(self):
        session = self.request['session']
        advertisement_id = int(self.request.match_info['advertisement_id'])
        advertisement = await get_advertisement(advertisement_id=advertisement_id,
                                                        session=session)

        return web.json_response({
            'id': advertisement.id,
            'description': advertisement.description,
            'owner': advertisement.owner,
            'header': advertisement.header,
            'creation_time': advertisement.creation_time.isoformat()
    })

    async def post(self):
        session = self.request['session']
        json_data = await self.request.json()
        advertisement = Advertisements(**json_data)
        session.add(advertisement)
        await session.commit()

        return web.json_response({
            'advertisement_id': advertisement.id,
            'message': 'The advertisement was successfully created'
        })

    async def delete(self):
        advertisement_id = int(self.request.match_info['advertisement_id'])
        advertisement = await get_advertisement(advertisement_id=advertisement_id,
                                                session=self.request['session'])
        await self.request['session'].delete(advertisement)
        await self.request['session'].commit()
        return web.json_response({'status': 'success'})


app.add_routes(
    [
        web.get('/advertisements/{advertisement_id:\d+}/', AdvertisementView),
        web.post('/advertisements/', AdvertisementView),
        web.delete('/advertisements/{advertisement_id:\d+}/', AdvertisementView)
    ]
)

if __name__ == '__main__':
    web.run_app(app=app)
