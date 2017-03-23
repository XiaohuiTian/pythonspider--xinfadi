from sqlalchemy import Column,Integer,Numeric,String,Date,DateTime,TIMESTAMP
from Model import Base
import time

class Goods(Base.Base):

    __tablename__ = "jpgk_news_goods"

    id = Column(String(32), primary_key=True,autoincrement=False)
    name = Column(String(50),nullable=False,)
    category = Column(Integer,nullable=False)
    type = Column(Integer,default=2,nullable=False)
    status = Column(Integer,default=1,nullable=False)
    unit = Column(String(20),default="斤",nullable=False)
    description = Column(String,nullable=True)
    create_time = Column(DateTime,nullable=False)
    update_time = Column(TIMESTAMP)

    def __init__(self,goodsId,name,categoryId,unit):

        self.id = goodsId
        self.name = name
        self.category = categoryId
        self.unit = unit
        self.create_time = time.time()