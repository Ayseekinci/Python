import re

str = "Merhaba Benim adım Ayşe.Benim yaşım 23"

result = re.findall("Benim", str)  # Cümlenin içinde karakter araması yapar.

result = re.findall("[abc]", str)  # abc karakterlerini arar.

result = re.findall("[^abc]", str)  # abc dışındaki tüm karakterleri arar.

result = re.findall("[a-k]", str)  # a dan k ye kadar karakterleri arar.

result = re.findall("...", str)  # 3 basmaklı karakteri gösterir.

result = re.findall("^M", str)  # Cümle M ile başlıyor mu ?

result = re.findall("s$", str)  # cümle s ifadesi ile bitiyor mu?

result = re.findall("[0-9]{2}", str)  # 2 basamaklı rakam aramada kullanılır.

result = result.string  # Benim kelimesini hangi cümlede arıyor onu gösterir.

result = len(result)  # Kaç tane Bneim kelimesi var?

result = re.split(" ", str)  # Cümledeki her boşluktan sonra kelimleri böl.

result = re.sub(" ", "-", str)  # Cümledeki her boşluğa'-' karakterini koyar.

result = re.search("Benim", str)  # Benim kelimesinin index numaralarını verir.

# result = result.span()  # index numaradını verir
# result = result.start()  # Benim kelimesi hangi karakterden başlıyor onu söyler
# result = result.end()  # Bitiş karakterini söylüyor.
# result = result.group()  # Hangi kelimeyi aradığını söylüyor=Benim kelimesini.


print(result)
