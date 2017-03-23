from sqlalchemy import Column,Integer,Numeric,String,Date,DateTime,TIMESTAMP,ForeignKey
from Model import Base
import time
from sqlalchemy.orm import relationship

class Price(Base.Base):

    __tablename__ = "jpgk_news_goods_standard"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)
    # goods_id = Column(String(32),nullable=False,ForeignKey(column='jpgk_news_goods_standard.goods_id'))
    goods_id = Column(String(32),nullable=False)
    lowest_price = Column(Numeric)
    avg_price = Column(Numeric)
    highest_price = Column(Numeric)
    price = Column(Numeric)
    status = Column(Integer,default=1,nullable=False)
    publish_date = Column(Date)
    create_time = Column(DateTime,nullable=False)
    update_time = Column(TIMESTAMP)

    def __init__(self,guige,goodsId,lowPrice,averagePrice,maxPrice,publish_date):

        self.name = guige
        self.goods_id = goodsId
        self.lowest_price = lowPrice
        self.avg_price = averagePrice
        self.highest_price = maxPrice
        self.price = averagePrice
        self.publish_date = publish_date
        self.create_time = time.time()