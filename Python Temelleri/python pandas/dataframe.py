import pandas as pd
from numpy.random import randn

s1 = pd.Series([2, 3, 1, 9, 5])
s2 = pd.Series([1, 5, 3, 2, 9])
# s1 ve s2 deki sayıları birleştirp pandas biçimde ve Kolonlara isimler vererek yazmak.
data = dict(sayilar1=s1, sayilar2=s2)  # kolon isimleri sayilar1 ve sayilar2
df = pd.DataFrame(data)
print(df)

# index numaralarını kendimiz belirleyerek  not örneği yapmak.
data = (["Ayşe", 80], ["Yağmur", 70], ["Enes", 75], ["Fatih", 90])
df = pd.DataFrame(data, columns=['İsim', 'Not'], index=[1, 2, 3, 4])
print(df)


# Sütun ve kolonlara göre seçme işlemleri
islem = pd.DataFrame(randn(3, 3), index=["A", "B", "C"], columns=[
    "Column1", "Column2", "Column3"])

print(islem)
result = islem
result = islem["Column1"]  # column1 bilgisini alır.
result = islem[["Column1", "Column2"]]  # birden fazla column seçimi için.
print(result)

# Satıra göre seçme işlmeleri
result = islem.loc["A"]
print(result)
result = islem.loc["A":"C"]  # A ile C arasındaki satırları yazar.
# Baştan B satırına kadar ve column2 ye kadar olanları yazdır.
result = islem.loc[:"B", :"Column2"]
result = islem.iloc[0]  # 0.indekstekini yazdırır yani A satırını
result = islem.loc["A", "Column3"]  # A indexteki column3ü yazdırır.
print(result)

# Yeni column4 eklemek.
islem["Column4"] = pd.Series(randn(3), ["A", "B", "C"])
print(islem)
# yeni column5 ekleyip var olan columnlardan verilerini toplayıp eklmek.
islem["Column5"] = islem["Column2"]+islem["Column3"]

islem.drop("Column5", axis=1)  # varolan kolonu silme
print(islem)
result = islem.columns  # kaç tane columns olduğunu gösterir.
result = islem.head(1)  # ilk column görüntüler
result = islem.tail(2)  # son iki columns gösterir.
result = islem["Column3"].head(2)  # column3 ün ilk 2 verisini gösteriri.
print(result)

# sadece column1 ve column3 ün son 2 kaydını al.
result = islem[["Column1", "Column3"]].tail(2)
print(result)
# Columns içerisindeki 1 den büyük olanları gösteren örnek
result = islem[islem > 1]
print(result)
# column2 deki 1 den küçük olan değerleri gösteren örnek
result = islem[islem["Column2"] < 1]["Column2"]
print(result)
