"""
x,y,z=3,8,5
print(x,y,z)

values=1,6,7
print(type(values))   #valuesin tipinin ne olduğunu gösterir.

x,y,z=values     #x y z değişkenlerine valuesin değerlerini atar.
print(x,y,z) 

number=5,3,4,9,6

x,y,*z=number  # x=5 y=3 geriye kalanları  da z değişkenine atar.
print(x,y,z)
print(x,y,z[1])   # x=5 y=3 ve z değişeninde 1. indeksini atar z=9 olur."""


x,y,z=2,5,107
numbers=1,5,7,10,6


#Kullanıcıdan aldığıız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
sayi1=int(input("1.sayi : "))
sayi2=int(input("2.sayi : "))
sonuc=(sayi1*sayi2)-(x+y+z)
print(sonuc)


#y nin x e kalansız bölümü 
x //=y
print(x)

#x+y+z nin mod 3 nedir?
son=(x+y+z) %3
print(son)

#ynin x. kuvvetini hesaplayınız
y =y**x
print(y)

# x,*y,z=numbers işlemine göre z'nin küpü kaçtır? ve y değerleri toplamı kaçtır?
x,*y,z=numbers
print(x,y,z)
z **=3
print(z)
result=y[0]+y[1]+y[2]
print(result)




#girilen iki sayıdan hangisi büyüktür.
i=int(input("1.sayi : "))
j=int(input("2.sayi : "))

result=i>j
print(f"i:{i} j:{j} den büyük :{result}")




#Kullanıcıdan 2 vize (%60) ve final(%40) notunun alıp ortalamayı hesaplayınız. eğer ortalama 50 ve üstüyse geçti.

vize1=float(input("vize1 notunuz : "))
vize2=float(input("vize2 notunuz : "))
final=float(input("final notunuz : "))

ortalama=(((vize1+vize2)*0.6 /2)+(final*0.4))
print(f"ortalama :  {ortalama} ve geçme durumunuz {ortalama>=50}")



#Girilen bir sayının tek mi çift mi olduğunu bulunuz.
sayi=float(input("Bir sayi giriniz :"))

tekcift=(sayi%2==0)

print(f"girilen sayinin çift olma durumu  :{tekcift} ")



#Girilen bir sayının pozitif mi negatif mi olma durumu.
sayi=int(input("Bir sayi giriniz :"))

isaret= (sayi>0 )

print(f"sayinin pozitif olma durumu : {isaret}")



#






