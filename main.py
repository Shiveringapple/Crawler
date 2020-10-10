from urllib.request import urlopen, urlretrieve
import json
import os

# range(12) == range(0, 12) -> [0, 1, 2,..., 11)
for m in range(0, 12):
    url = "https://www.google.com/doodles/json/2020/" + str(m + 1) + "?hl=zh_TW"
    print("現在在處理的頁面:", url)
    response = urlopen(url)

    doodles = json.load(response)
    # doodles是List，d是Dictionary
    for d in doodles:
        url = "https:" + d["url"]
        print(d["title"], url)
        print(url.split("/")[-1])

        dirname = "doodles/" + str(m + 1) + "/"
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        fname = dirname + url.split("/")[-1]

        urlretrieve(url, fname)   # 與以下做法相同
        # # 針對圖片做處理
        # response = urlopen(url)
        # img = response.read()
        # # 存檔三步驟
        # f = open(fname, "wb")
        # f.write(img)
        # f.close()

