import sqlalchemy
import os

from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from models import create_tables, Publisher, Book, Shop, Sale, Stock

load_dotenv()
name = os.getenv("NAME")
password = os.getenv("PASSWORD")
name_db = os.getenv("NAMEDB")


DSN = f"postgresql://{name}:{password}@localhost:5432/{name_db}"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

# pb1 = Publisher(name="Пушкин")
# pb2 = Publisher(name="Дэн Браун")
# session.add_all([pb1,pb2])
# session.commit()

# sh1 = Shop(name="Буквоед")
# sh2 = Shop(name="Школьник")
# session.add_all([sh1,sh2])
# session.commit()

# bk1 = Book(title="Капитанская дочка",id_publisher = 1)
# bk2 = Book(title="Руслан и Людмила",id_publisher = 1)
# bk3 = Book(title="Евгений Онегин",id_publisher = 1)
# bk4 = Book(title="Медный всадник",id_publisher = 1)
# bk5 = Book(title="Ангелы и Демоны",id_publisher = 2)
# bk6 = Book(title="Код да Винчи",id_publisher = 2)
# bk7 = Book(title="Цифровая крепость",id_publisher = 2)
# bk8 = Book(title="Инферно",id_publisher = 2)
# session.add_all([bk1,bk2,bk3,bk4,bk5,bk6,bk7,bk8])
# session.commit()

# st1 = Stock(count=50,id_book= 1,id_shop = 1)
# st2 = Stock(count=45,id_book = 2,id_shop = 2)
# st3 = Stock(count=100,id_book = 3,id_shop = 1)
# st4 = Stock(count=74,id_book = 4,id_shop = 2)
# st5 = Stock(count=200,id_book = 5,id_shop = 1)
# st6 = Stock(count=123,id_book = 6,id_shop = 2)
# st7 = Stock(count=35,id_book = 7,id_shop = 1)
# st8 = Stock(count=115,id_book = 8,id_shop = 2)
# session.add_all([st1,st2,st3,st4,st5,st6,st7,st8])
# session.commit()
# sl1 = Sale(count=3,id_stock = 9,data_sale = "2023-01-08",price = 600)
# sl2 = Sale(count=5,id_stock = 10,data_sale = "2023-01-12",price = 600)
# sl3 = Sale(count=11,id_stock = 11,data_sale = "2023-05-23",price = 400)
# sl4 = Sale(count=2,id_stock = 12,data_sale = "2023-03-08",price = 300)
# sl5 = Sale(count=1,id_stock = 13,data_sale = "2023-02-23",price = 750)
# sl6 = Sale(count=6,id_stock = 14,data_sale = "2023-07-19",price = 900)
# sl7 = Sale(count=3,id_stock = 15,data_sale = "2023-05-14",price = 850)
# sl8 = Sale(count=2,id_stock = 16,data_sale = "2023-09-01",price = 1000)
# session.add_all([sl1,sl2,sl3,sl4,sl5,sl6,sl7,sl8])
# session.commit()
# for c in session.query(Publisher).all():
#     print(c)
name_publisher = input("Введите имя писателя: ")
subq = session.query(Publisher).filter(Publisher.name == name_publisher).subquery()

for c in session.query(Book.title,Sale.price,Shop.name,Sale.data_sale).join(subq, Book.id_publisher == subq.c.id).join(Stock,Book.id == Stock.id_book).join(Sale,Stock.id == Sale.id_stock).join(Shop,Stock.id_shop == Shop.id).all():
    print(*c,sep="|")


session.close()