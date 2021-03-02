import numpy as np

# 10 ile 100 arasında rastgele 6 sayı üretip aynı index deki dizileri topla

numbers1 = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)
print(numbers1)
print(numbers2)
result = numbers1+numbers2
result = numbers1+10  # numbers1 deki sayılara 10 ekler
result = np.sin(numbers2)  # numbers2 deki sayıların sinüs alır.
print(result)


# üretilen sayıları matrise çevirip birleştirme

numbers3 = numbers1.reshape(2, 3)
numbers4 = numbers2.reshape(2, 3)
print(numbers3)
print(numbers4)
result = np.vstack((numbers3, numbers4))  # dikey olarak birleştirir.
result = np.hstack((numbers3, numbers4))  # yatay olarak birleştirir.
print(result)


# üretilen sayılarda işlemler

say1 = np.random.randint(15, 50, 3)
print(say1)
result = say1 > 20  # sayılar 20 den büyük mü?
result = say1 % 2 == 0  # sayılar çift mi?
print(result)
