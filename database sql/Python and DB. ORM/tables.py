import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), nullable=False)

    def __str__(self):
        return f'{self.id} : {self.name}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(200), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    def __str__(self):
        return f'{self.id} : {self.title} : {self.id_publisher}'

class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), nullable=False)

    def __str__(self):
        return f'{self.id} : {self.name}'

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer)

    shop_id = relationship('Shop', backref='book_stock')
    book_id = relationship('Book', backref='shop_stock')

    def __str__(self):
        return f'{self.id} : {self.book_id}' \
               f'{self.shop_id} : {self.count}'

class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.DECIMAL(6, 2), nullable=False)
    date_sale = sq.Column(sq.DateTime)
    count = sq.Column(sq.Integer, nullable=False)
    stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)

    stock_id = relationship('Stock', backref="sale_id")

    def __str__(self):
        return f"{self.id} :  {self.price} : {self.date_sale}" \
               f"{self.stock_id} :  {self.count})"

def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
