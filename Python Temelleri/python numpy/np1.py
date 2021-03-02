import numpy as np

np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
np_liste = np_array.reshape(3, 3)  # matris şeklinde düzenler
print(type(np_array))
print(np_liste)
print(np_array.ndim)  # kaç boyutlu olduğunu gösterir.
print(np_liste.shape)  # kaça kaç matrisli olduğunu gösterir.
result = np_array[5]  # 5.index deki sayıyı yazdırır.
result = np_array[3:]  # 3.indexten sonrayı yazdırır.
result = np_array[::]  # tüm listeyi yazdırır.
result = np_array[-2]  # sondaki indeksi yazdırır.
print(result)

result = np.arange(1, 10)  # 1 ile 10 arasındaki sayılar
result = np.arange(10, 100, 3)  # 10 ile 100 arasında 3 er 3 er artarak yazar.
result = np.ones(10)  # 1 lerden oluşan 10 tane dizi oluşturur.
result = np.linspace(0, 100, 5)  # 0 ile 100 arasını eşit aralıklarla böler
result = np.random.randint(0, 10)  # 0 ile 10 arasında rastgele birsayı üretir.

# sadece bitiş değerini vererek 0 ile 20 arasında rastgele sayı üretir.
result = np.random.randint(20)
# 1 ie 10 arasında 3 tane rastgele sayı üretir.
result = np.random.randint(1, 10, 3)
print(result)

# 0 ile 50 arasındaki sayıları 5 e 10 luk matris oluştur ve satırların toplamını bul.
np_array = np.arange(50)
np_liste = np_array.reshape(5, 10)
print(np_liste.sum(axis=1))
print(np_liste.sum(axis=0))  # sütunların toplamını verir.

# 1 ile 100 arasında rastgele 10 sayı üret en büyüğünü bul ve index numarasını yazdır .
np_sayi = np.random.randint(1, 100, 10)
print(np_sayi)
result = np_sayi.max()
print(result)
result = np_sayi.argmax()
print(result)

# 10 ile 50 arasında rastgele 5 sayı üret en küçüğünü ve  ortalamasını bul.
np_sayi = np.random.randint(10, 50, 5)
print(np_sayi)
result = np_sayi.min()
print(result)
result = np_sayi.mean()
print(result)

# birden fazla satırlarda işlemler
sayilar = np.array([[0, 5, 10], [15, 20, 25], [60, 70, 80]])
result = sayilar[2, 2]  # 2.gruptaki 2.index elemanını yazar.
result = sayilar[:, 2]  # tüm elemanlardaki 2.indextekilerin hepsinin yazdırır.
# bütün elemanlar arasında 0 ile 2. indexlerdeki yazıları yazdırır.
result = sayilar[:, 0:2]

print(result)
