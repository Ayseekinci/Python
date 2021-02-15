carbrands=['Honda','Opel','Audi','Bmw','Ford']

result=len(carbrands) #Kaç karakter var
print(result)

print(carbrands[0])        #ilk araba markası
print(carbrands[3])        #3. indexteki araba markası
carbrands[2]='Toyota'      #2. indexteki araba markasını Toyata ile değiştir.
print(carbrands)
result='Opel' in carbrands   #Listede opel markası var mı ?
result=carbrands[-1]      #-1 indekindeki değer nedir?
print(result)
print(carbrands[:3])      #Listenin ilk 3 elamanı.
carbrands[-2:]='Ferrari','Renault'   #listenin son iki elamanını değiştir.
carbrands[5:6]='Dacia','Fiat'        #listeye dacia ve fiat markasını ekler.
del carbrands[2]        #2. indexteki araba markasını siler.
print(carbrands)

result=carbrands[::-1]     #listedekileri tersten yazar.
print(result)  


studentA= ['Ayşe' , 'Ekinci' ,'1998', '(90,60,80)' ]  #verileri liste içerisine aktardık.
studentB=['Sena ','Turan' ,'2010','(70,80,80)']       #verileri liste içerisine aktardık.
studentC=['Ahmet', 'Bilgin' ,'2000', '(60,70,80)']    #verileri liste içerisine aktardık.
print(studentA , studentB , studentC)                 #listeleri yazdırdık.
result= studentA[0] + studentB[2] + studentC[3][1]    #studentA listesindeki 0.indeksi+ studentB list. 2.indeksi + studentC list. 3. indeksi ve 3.index içerisindeki 1. indeksi aldık.
print(result)











