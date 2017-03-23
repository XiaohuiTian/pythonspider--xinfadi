from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql

class DB:

    session = None

    def __init__(self):

        DB_CONNECT_STRING = 'mysql+pymysql://username:pwd@host/db?charset=utf8'
        engine = create_engine(DB_CONNECT_STRING, echo=True)
        DB_Session = sessionmaker(bind=engine)
        self.session = DB_Session()

    def __del__(self):
        self.session.close()