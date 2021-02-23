
from bs4 import BeautifulSoup
html_dokumani = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İLK WEB SAYFAM</title>
</head>

<body>
    <h1>
        Python Kursu
    </h1>
    <div class="Grup1">
        <h1>Programlama</h1>
        <ul>
            <li>Python</li>
            <li>C++</li>
            <li>Java</li>


        </ul>
    </div>
    <div class="Grup2">
        <h1>Modüller</h1>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>


        </ul>
    </div>
    <img src="unnamed.jpg" alt="">
     <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>,
     <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>,
     <a class="sister" href="http://example3.com/tillie" id="link3">Tillie</a>

</body>

</html>"""

soup = BeautifulSoup(html_dokumani, 'html.parser')

result = soup.prettify()  # ilgili html dosyasını düzenleyerek verir.
result = soup.title  # html de title bilgisini yazdırır.
result = soup.body  # html de ki bütün body içeriğini verir.
result = soup.title.string  # title içerindeki string yazılır.

# html de bulunan bütün h1 etiketindeki bilgileri verir.
result = soup.find_all('h1')
result = soup.find_all('h1')[0]  # sadece 1. h1 etiketinin biligisini verir.


# html de sadece 2.div de bulunan ul etiketini yazdırır.
result = soup.find_all('div')[1].ul

result = soup.find_all('a')  # html kısımdaki tüm a etiketlerini yazdır.
# html kısımdaki tüm a etiketlerinin linklerini yazdır.
for link in result:
    print(link)

print(result)
