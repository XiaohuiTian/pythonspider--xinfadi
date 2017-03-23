from urllib.request import *
from bs4 import BeautifulSoup

soup = BeautifulSoup(markup=urlopen(url="http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"),features="html5lib")
tables = soup.find_all(name="table",class_="hq_table")
goodses = []
for table in tables:
    trs = table.find_all("tr")
    del trs[0]

    for tr in trs:
        tds = tr.find_all("td")

        goodses.append({
            "name":tds[0].get_text(),
            "lowPrice":tds[1].get_text(),
            "averagePrice":tds[2].get_text(),
            "maxPrice":tds[3].get_text(),
            "guige":tds[4].get_text(),
            "unit":tds[5].get_text(),
            "publishDate":tds[6].get_text(),
        })

print(goodses)
