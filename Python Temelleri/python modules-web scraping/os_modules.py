import os
import datetime

result = os.name  # kullanıgınız işletim sistemini adını verir.
result = os.getcwd()  # şuan kullandığınız klasör hakkında bilgi verir.
print(result)


# şuan kullandığım os_modules klasörüne yeni dosya adında yeni klasör ekledi
os.mkdir("yenidosya")


# eklediğimiz yenidosyanın içine farklı dosya kaydetme
os.makedirs("yenidosya/yedekklasör")

# oluşturduğumuz yeni dosyanın adını değiştirildi olarak değişti
os.rename("yenidosya", "degistirildi")

os.rmdir("newdirectory")  # newdirectory adındaki klasörü siler.

# Listeleme İşlemleri
result = os.listdir()   # Şuan kayıtlı olan listeleti gösterir.
print(result)

for liste in os.listdir():
    if liste.endswith('.py'):  # .py uzantılı dosyaları gösterir.
        print(liste)

# kayıtlı olan dosyalarınız hakkında bilgi gösterir.
result = os.stat("datatime_modules.py")
print(result)

# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişim tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# dosyanın tam konumunu almak için kullanılır.
result = os.path.abspath("os_modules.py")

# os_modules.py böyle bir klasör varmı ? diye bakılıyor.
result = os.path.exists("os_modules.py")
print(result)
