from bs4 import BeautifulSoup
from urllib.request import *
import time
from Model import DB
from Model import Price
from Model import Goods
import pymysql
import hashlib

class Spider():

    def __init__(self):
        self.categoryId = 0
        self.dataCategoryId = 0
        self.havenGoodsIdArr = []

        self.db = DB.DB()
        self.parser = Parser()


    # 数据爬取
    def spider(self,categoryId):

        self.categoryId = categoryId
        self.dataCategoryId = categoryId + 100

        baseUrl = "http://www.xinfadi.com.cn/marketanalysis/" + str(categoryId) + "/list/"

        #获取当前的日期
        curDate = time.strftime("%Y-%m-%d")

        #统计当天有没有拉取成功
        isLa = self.db.session.execute("select * from jpgk_news_goods_standard as s INNER JOIN jpgk_news_goods as g on s.goods_id = g.id where s.publish_date = '"+curDate+"' AND g.category="+str(self.dataCategoryId)+" LIMIT 0,1").fetchall()

        if len(isLa) == 1:
            return True

        # 设置默认时间是当前时间
        defaultDate = curDate

        # 设置分页的统计变量
        pageNum = 1

        # 声明总商品的列表
        goodses = []

        while curDate <= defaultDate:

            # 发送次请求
            tmpUrl = baseUrl+str(pageNum)+".shtml"
            # print(tmpUrl)
            markUp = urlopen(url=tmpUrl)

            # 调用解析器，解析页面内容
            res = self.parser.parserHtmlToGoods(markUp=markUp,date=curDate,categoryId=self.dataCategoryId)

            # 从返回结果中取值
            goods = res["goods"]
            defaultDate = res["defaultDate"]

            # 把返回的商品结果合并到goodses集合中
            goodses.extend(goods)

            pageNum += 1

        #调用数据处理
        return self.dealwithData(goodses=goodses)

    #数据处理
    def dealwithData(self,goodses):

        goodsPriceArr = []
        goodsArr = []

        #查询所有的goods
        if(len(goodses) > 0 and len(self.havenGoodsIdArr) <= 0):

            print("******************************")
            havenGoods = self.db.session.query(Goods.Goods).filter(Goods.Goods.type == 2).all()

            # 从已存在的数据中取出
            for goodsObj in havenGoods:
                self.havenGoodsIdArr.append(goodsObj.id)

        try:

            # 数据整理
            for goods in goodses:

                idStr = goods["name"] + goods["guige"] + goods["unit"]
                md5 = hashlib.md5(idStr.encode(encoding="utf-8"))
                goodsId = md5.hexdigest()

                goodsPriceArr.append(Price.Price(guige=goods["guige"],goodsId=goodsId,lowPrice=goods["lowPrice"],averagePrice=goods["averagePrice"],maxPrice=goods["maxPrice"],publish_date=goods["publishDate"]))

                if self.havenGoodsIdArr.count(goodsId) == 0:
                    goodsArr.append(Goods.Goods(goodsId=goodsId,name=goods["name"],categoryId=goods["categoryId"],unit=goods["unit"]))

            self.db.session.add_all(goodsArr)
            self.db.session.add_all(goodsPriceArr)

            self.db.session.commit()

            # 主动释放内存
            del goodses

            return True

        except Exception as err:

            self.db.session.rollback()
            raise err


class Parser():

    def parserHtmlToGoods(self,markUp,date,categoryId):

        # 声明服务器时间，为只取当天的数据做准备
        serverDate = None

        # 使用类库分析返回的html，获取数据
        soup = BeautifulSoup(markUp,features="html5lib")
        tables = soup.find_all(name="table", class_="hq_table")

        # 声明要返回的数据
        goodses = []
        for table in tables:

            # 获取table中的tr
            trs = table.find_all("tr")
            # 删除第一行的标题行
            del trs[0]

            for tr in trs:

                # 获取tr中所有的td
                tds = tr.find_all("td")

                # 如果发布时间是当天，就添加到列表中
                if(tds[6].get_text() == date):

                    goodses.append({
                        "name":tds[0].get_text(),
                        "lowPrice":tds[1].get_text(),
                        "averagePrice":tds[2].get_text(),
                        "maxPrice":tds[3].get_text(),
                        "guige":tds[4].get_text(),
                        "unit":tds[5].get_text(),
                        "publishDate":tds[6].get_text(),
                        "categoryId":categoryId
                    })

                serverDate = tds[6].get_text()

        del markUp
        return {"goods":goodses,"defaultDate":serverDate}