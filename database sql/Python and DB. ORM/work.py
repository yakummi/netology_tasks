import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from tables import create_tables, Publisher, Sale, Shop, Stock, Book
import config as c
from sqlalchemy_utils import database_exists, create_database

name_db = 'shop_book'
DSN = f'postgresql://{c.USER}:{c.PASSWORD}@{c.HOST}:{c.PORT}/{name_db}'
engine = sq.create_engine(DSN)
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

def publ(pers_input):
    if pers_input.isdigit():
        query = session.query(Publisher).filter(Publisher.id == pers_input).all()
    else:
        query = session.query(Publisher).filter(Publisher.name == pers_input).all()
    if query:
        for output in query:
            return output
    return 'Publisher not found'

def out_shop(pers_input):
    query = session.query(Shop)
    query = query.join(Stock)
    query = query.join(Book)
    query = query.join(Publisher)

    if pers_input.isdigit():
        query = query.filter(Publisher.id == pers_input).all()
    else:
        query = query.filter(Publisher.name == pers_input).all()
    if query:
        for output in query:
            return output
    return 'Publisher not found'


session.close()

if __name__ == '__main__':
    publisher = input('Write ID/NAME: ')
    print(publisher)
    print(out_shop(publisher))

