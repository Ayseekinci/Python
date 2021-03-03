import pandas as pd
import numpy as np

numbers = [5, 10, 7, 13]

pandas_series = pd.Series(numbers)  # listeyi index numaralarına göre yazdırır.
# index numaralarını sayı değilde a b c d diye tanımlar.
pandas_series = pd.Series(numbers, ['a', 'b', 'c', 'd'])
print(pandas_series)
result = pandas_series[:2]  # ilk iki elemanı yazdırır.
result = pandas_series['a']  # a ya karşılık gelen sayıyı verir.
result = pandas_series.sum()  # sayıların toplamını verir.
result = pandas_series.min()  # en küçük sayıyı verir.
result = pandas_series+pandas_series  # sayıları iki kere toplayıp verir.
result = np.sqrt(pandas_series)  # sayıların karekökünü alır.
print(result)


letters = ['a', 'b', 'd', 'c']
pandas_series = pd.Series(letters)  # listeyi index numaralarına göre yazdırır.
print(pandas_series)

scalar = 5
pandas_series = pd.Series(scalar)  # 5 sayısını index numarası ile yazdırır.
pandas_series = pd.Series(5, [1, 2, 3])  # sayıları index şeklinde yazdırır.
print(pandas_series)


# 10 ile 100 arasında rastgele üretilen 6 sayıyı pandas biçiminde sıralama
random_numbers = np.random.randint(10, 100, 6)
pandas_series = pd.Series(random_numbers)
print(pandas_series)


# Örnek
arac2019 = pd.Series([20, 30, 40, 60], ["opel", "fiat", "ford", "bmw"])
arac2020 = pd.Series([10, 30, 70, 20], ["opel", "fiat", "ford", "bmw"])
toplam = arac2019+arac2020
print(toplam)  # hepsini toplayıp verir.
print(toplam["fiat"])  # sadece fiat aracını toplayıp verir.
