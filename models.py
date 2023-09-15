import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()



class Publisher(Base):
    __tablename__ = "publisher"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(length=40),unique=True)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Book(Base):
    __tablename__ = "book"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(length=40),unique=True)
    id_publisher = sa.Column(sa.Integer, sa.ForeignKey("publisher.id"),nullable=False)

    publisher = relationship(Publisher, backref="book")
    def __str__(self):
        return f"{self.id}: {self.title}"

class Shop(Base):
    __tablename__ = "shop"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(length=40),unique=True)
    def __str__(self):
        return f"{self.id}: {self.name}"
class Stock(Base):
    __tablename__ = "stock"

    id = sa.Column(sa.Integer, primary_key=True)
    id_book = sa.Column(sa.Integer, sa.ForeignKey("book.id"),nullable=False)
    id_shop = sa.Column(sa.Integer,sa.ForeignKey("shop.id"),nullable=False)
    count = sa.Column(sa.Integer)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")
    def __str__(self):
        return f"{self.id}|{self.count}"

class Sale(Base):
    __tablename__ = "sale"

    id = sa.Column(sa.Integer,primary_key=True)
    price = sa.Column(sa.Integer)
    data_sale = sa.Column(sa.Date)
    id_stock = sa.Column(sa.Integer, sa.ForeignKey("stock.id"),nullable=False)
    count = sa.Column(sa.Integer)

    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f"{self.price}|{self.data_sale}"
def create_tables(engine):
    Base.metadata.create_all(engine)