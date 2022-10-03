from msilib import type_binary
from tkinter import W
from turtle import ScrolledCanvas, end_fill
import bs4
import urllib.request as req


# 抓取頁面裡的資料
def getData(src):
    request = req.Request(src, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    good_info = ""
    nor_info = ""
    bad_info = ""
    for title in titles:
        if title.a != None:
            if title.a.string[0:4] == "[好雷]":
                good_info += title.a.string + "\n"
            if title.a.string[0:4] == "[普雷]":
                nor_info += title.a.string + "\n"
            if title.a.string[0:4] == "[負雷]":
                bad_info += title.a.string + "\n"
    return good_info, nor_info, bad_info


# 抓取上一頁的連結
def getSrc(src):
    request = req.Request(src, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]


with open("movie.txt", mode="w", encoding="utf-8") as file:
    # 抓取多個葉面的網址內容
    src = "https://www.ptt.cc/bbs/movie/index.html"
    good_info = ""
    nor_info = ""
    bad_info = ""
    count = 0
    while count < 11:
        # print(getData(src))
        # print(type(getData(src)))
        title = getData(src)
        for info in title:
            # print(info)
            if info[0:4] == "[好雷]":
                good_info += info
            if info[0:4] == "[普雷]":
                nor_info += info
            if info[0:4] == "[負雷]":
                bad_info += info
        src = "https://www.ptt.cc" + getSrc(src)
        count += 1
    file.write(good_info + nor_info + bad_info)
