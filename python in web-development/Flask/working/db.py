from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
import atexit
import json
from sqlalchemy.orm import sessionmaker

with open(file="config/database.json") as file:
    config_json = json.load(file)

PG_DSN = f"{config_json['TYPE_DB']}://{config_json['USER_NAME']}:{config_json['USER_PASSWORD']}@{config_json['IP_ADDRESS']}/{config_json['DB_NAME']}"

mymetadata = MetaData()

engine = create_engine(PG_DSN)

Base = declarative_base(metadata=mymetadata)
Session = sessionmaker(bind=engine)

class Advertisements(Base):

    __tablename__ = "advertisements"

    id = Column(Integer, primary_key=True, autoincrement=True) # id объявления
    description = Column(String, nullable=False)
    header = Column(String, nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    owner = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)


