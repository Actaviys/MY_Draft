import requests
from bs4 import BeautifulSoup


url = "https://doc.qt.io/qt-5/widget-classes.html"
heabers = {
    "Acept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

req = requests.get(url)
src = req.text
# print(src)

with open("index.html", "w+") as file:
    file.write(src)