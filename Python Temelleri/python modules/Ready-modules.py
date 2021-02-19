
"""import math


values = dir(math)# math modülünün içerisindeki bileşenlerin isimleri value aktar

values = help(math) # math modülünün içerisindeki bileşenlerin ne işe yaradığına dair bilgiler verir
values = math.factorial(5)  # 5 in fakrtöriyelini hesaplar.=120
values = math.ceil(5.8)  # Sayısı yukarı doğru yuvarlama yapar.
print(values)"""

"""
# Modül ismi kullanılmadan yapma.
from math import(factorial, sqrt, ceil)

Values = factorial(7)
Values = sqrt(9)
Values = ceil(7.7)

print(Values)"""

"""
import random
result = random.random()  # 0.0 ile 1.0 arasında rast gele sayı üretir
result = random.random()*25  # Üretilen her bir sayıyı 25 ile çarpar
result = random.uniform(2, 19)  # 2 ile 19 sayıları arasında sayı üretir
result = random.randint(1, 100)  # 1 ile 100 arasında tam sayı üretir

# name listesindeki her defasında farklı farklı yazdırır
name = ['Ayse', 'Belinay', 'Enes', 'Yağmur']
result = random.choice(name)

liste = list(range(10))  # 0,1,2,3,4,5,6,7,8,9 sayılarını yazar
random.shuffle(liste)  # Listedeki sayıları her defasında farklı yazar
result = liste

liste = range(100)
result = random.sample(liste, 4)  # 0 ie 100 arasında rastgele 4 sayı yazdır

print(result)
"""
