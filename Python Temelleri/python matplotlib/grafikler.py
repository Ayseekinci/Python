import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.title("İlk Grafik")  # başlık ekler.
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.plot(x, y, color="red")  # grafik oluşturur çizgi rengi kırmızı olur.
plt.show()  # diyagramı gösterir.

# tek bir grafik üzerinden 3 çizgi oluşturma.
x = np.linspace(0, 2, 100)

plt.plot(x, x, label="lineer", color="red")
plt.plot(x, x**2, label="karesi", color="blue")
plt.plot(x, x**3, label="küpü", color="yellow")
plt.xlabel("x eksen")
plt.ylabel("y eksen")
plt.legend()
# plt.show()

# alt alta üç tane grafik oluşturma.

x = np.linspace(0, 2, 100)#belli aralıkta oluşturulur.
fig, axs = plt.subplots(3)

axs[0].plot(x, x, color="red")
axs[0].set_title("1.grafik")
axs[1].plot(x, x**2, color="black")
axs[1].set_title("2.grafik")
axs[2].plot(x, x**3, color="blue")
axs[2].set_title("3.grafik")
plt.tight_layout()  # iç içe girmiş grafik başlıklarını düzeltir.

plt.show()


# yan yana 2 ye 2 lik grafik oluşturma

x = np.linspace(0, 2, 100)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, x, color="red")
axs[0, 0].set_title("1.grafik")
axs[0, 1].plot(x, x**2, color="black")
axs[0, 1].set_title("2.grafik")
axs[1, 0].plot(x, x**3, color="blue")
axs[1, 0].set_title("3.grafik")
axs[1, 1].plot(x, x**4, color="green")
axs[1, 1].set_title("4.grafik")
plt.tight_layout()

plt.show()

x = np.linspace(0, 2, 100)
y = x**3
z = x**2

figure = plt.figure()
axes = figure.add_axes([0, 0, 1, 1])  # grafiği tam ekrana sığdırır.
axes.plot(x, z, label="1.çizgi")
axes.plot(x, y, label="2.çizgi")
axes.legend(loc=4)  # içerisindeki paremetre yazıyı sağ alt köşeye getirir.

plt.show()

# yıllara göre atılan gol sayıları grafiği

yil = [2001, 2002, 2003, 2004, 2005]
oyuncu1 = [5, 9, 15, 24, 8]
oyuncu2 = [10, 19, 15, 14, 18]
oyuncu3 = [12, 13, 15, 4, 28]
plt.plot([], [], color="blue", label="oyuncu1")
plt.plot([], [], color="red", label="oyuncu2")
plt.plot([], [], color="yellow", label="oyuncu3")
plt.stackplot(yil, oyuncu1, oyuncu2, oyuncu3)

plt.title("Yıllara göre atılan goller")
plt.xlabel("Yıl")
plt.ylabel("Gol sayısı")

plt.legend(loc=2)
plt.show()


# Pasta grafiği
goal_type = 'Penaltı ', 'Serbest vuruş', 'Kaleye atılan şut'
gol = [22, 40, 38]
colors = ['yellow', 'blue', 'red']
plt.pie(gol, labels=goal_type, colors=colors,
        shadow=True, explode=(0.05, 0.05, 0.05), autopct="%1.1f%%")
# shadow=gölgelendirme , explode=dilimler arası boşluk,autopct=yüzdelik kısmı yazdırır.
plt.show()


# bar grafiği

plt.bar([0.25, 1.25, 2.25, 3.25], [10, 20, 30, 40], label="FORD", width=.4)
plt.bar([0.75, 1.75, 2.75, 3.75], [50, 20, 80, 70], label="BMW", width=.4)
plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe(km")
plt.title("Araç bilgileri")
plt.show()
