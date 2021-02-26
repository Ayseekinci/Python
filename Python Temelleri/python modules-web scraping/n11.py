
import requests
from bs4 import BeautifulSoup


url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
list = soup.find_all("li", {"class": "column"})

for li in list:
    name = li.div.a.h3.text
    name = name.strip()
    link = li.div.a.get("href")
    eskifiyat = li.find("div", {"class": "proDetail"}
                        ).find_all("a")[0].text.strip().strip('TL')
    yenifiyat = li.find("div", {"class": "proDetail"}
                        ).find_all("a")[1].text.strip().strip('TL')
    print(
        f"name:{name}  link:{link}  eski fiyat: {eskifiyat}  yeni fiyat: {yenifiyat}")


url2 = "https://www.n11.com/bilgisayar/masaustu-bilgisayar"
html = requests.get(url2).content
soup = BeautifulSoup(html, "html.parser")
list = soup.find_all("div", {"class": "column"}, {"type": "hidden"})

print(list)


url3 = "https://www.n11.com/bilgisayar/ipad-ve-tablet"
html = requests.get(url3).content
soup = BeautifulSoup(html, "html.parser")
list = soup.find_all("div", {"class": "column"}, {"title": "maske"}, limit=1)

print(list)
