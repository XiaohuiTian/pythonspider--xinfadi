from Spider import Spider
from ErrorWith import MyEmail
# from bs4 import BeautifulSoup
# from urllib.request import *
import time
# from Model import DB
# from Model import Price
# from Model import Goods
# import pymysql
# import hashlib
import schedule




if __name__ == "__main__":

    def spider_job():
        try:
            spider = Spider.Spider()
            spider.spider(categoryId=1)
            spider.spider(categoryId=2)
            spider.spider(categoryId=3)
            spider.spider(categoryId=4)
            spider.spider(categoryId=5)

            print("success")

            time.sleep(5)

        except Exception as err:

            # 错误预警，发送邮件
            errStr = ",".join(err.args)
            myEmail = MyEmail.MyEmail()
            myEmail.tag = "新发地商品数据爬去异常"
            myEmail.to_list = ["tianxh@jpgk.com.cn"]
            myEmail.content = errStr
            myEmail.send()
            print(errStr)

            # 生成exe命令: pyinstaller  -F xfdspider.py

    # spider_job()
    schedule.every(2).hours.do(spider_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
