from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

page = 51
while True:
    # find(找第一個符合的) find all(找所有符合的)
    # find答案:一個  find_all答案:List
        url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
        print("處理url", url)
        try:
            response = urlopen(url)
        except HTTPError:
            print("好像最後一頁了")
            break
        html = BeautifulSoup(response)
        for r in html.find_all("li", class_="list-rst"):
            ja = r.find("small", class_="list-rst__name-ja")
            en = r.find("a", class_="list-rst__name-main")
            ratings = r.find_all("b", class_="c-rating__val")
            # 萃取紙條(.text)  萃取特別特徵([特徵])
            print(ratings[0].text,
                ja.text,
                en.text,
                en["href"])
            page += 1


