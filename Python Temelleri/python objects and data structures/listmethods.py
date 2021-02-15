numbers =[1,5,2,8,6,10,3,4,2,10]
latters =['a','n','z','b','g','k']

value=min(numbers)              #en küçük sayı değerini alır.
value=max(latters)              #en büyük harfi alır.
value=numbers[3:6]              #3. indek il 6. index arasındakileri yazdırır.
print(value)
latters[3]='AYŞE'               #3. indekse Ayşe yazısını ekler.
latters[6:]='W','EKİNCİ','C'    #en sona w,ekinci,c  karakterlerini ekler.
latters.append('alfaba')        #en sona alfaba karakterini ekler.
print(latters) 
numbers.append(138)             #en sona 138 sayısını ekler.
numbers.insert(4,101)           #4. indekse 101 sayısını ekler.
numbers.pop(7)                  #7. indexteki sayıyı siler.
numbers.remove(8)               #8 sayısını siler
numbers.sort()                  #listeyi sıralar.
print(numbers)
latters.reverse()               #listesyi tersten sıralar.
print(latters)
value=len(latters)              #kaç karakter olduğunu bulur.
print(value)
value=numbers.count(10)         #10 sayısından kaç tane olduğunu bulur.
print(value)
latters.clear()                 #latters dizisinin hepsini siler.
print(latters)


#str="Python,Programlama,Java"karakter dizisini listeye çevir.

str="Python,Programlama,Java".split(',')
print(str)

#Kullanıcıdan alacağımız 3 tane araba marka bilgisini bir listede saklayın.

markalar=[]
marka=input("1.Marka : ")
markalar.append(marka)
marka=input("2.Marka : ")
markalar.append(marka)
marka=input("3.Marka : ")
markalar.append(marka)

print(markalar)



