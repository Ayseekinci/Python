from datetime import datetime

simdi = datetime.now()  # şuanki tarih ve zamanı verir.
result = datetime.now()

result = simdi.year   # şimdiki yılı verir.
result = simdi.day  # gün bilgisi
result = simdi.month  # ay bilgisi
result = simdi.hour  # şuanki saat
result = simdi.minute  # şuanki dakika
result = simdi.second  # şuanki saniye

result = datetime.ctime(simdi)  # şuanki bilgileri daha detaylı verir.

# Y=yıl ,X=saat ,d=gün bilgisi verir.
result = datetime.strftime(simdi, '%Y , %X, %d')
result = datetime.strftime(simdi, '%A')  # A= gün bilgisi
result = datetime.strftime(simdi, '%B')  # B=ay bilgisi
print(result)

t = ('7 April 1998 hour 13:47:25')
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
print(result)

# Doğum tarihi örneği

birtday = datetime(1998, 5, 7, 19, 47, 23)
print(birtday)

# Tarihler arasında fark

result = simdi-birtday
print(result)
