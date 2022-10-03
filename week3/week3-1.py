from unittest import result
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

dataAll = data["result"]["results"]

with open("data.csv", mode="w", encoding="utf-8") as file:
    for data in dataAll:
        pic = data["file"]
        pic_1 = pic.split("https")
        if int(data["xpostDate"][0:4]) > 2014:
            file.write(data["stitle"] + "," + data["address"][5:8] + "," +
                       data["longitude"] + "," + data["latitude"] + "," + "https" + pic_1[1] + "\n")
