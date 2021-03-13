import mysql.connector
from datetime import datetime
from connection import connection


class Student:
    connection = connection
    mycursor = connection.cursor()

    # def __init__(self, ogrenciNo, ad, soyad, dogumTarihi, cinsiyet):
    #     self.ogrenciNo = ogrenciNo,
    #     self.ad = ad,
    #     self.soyad = soyad,
    #     self.dogumTarihi = dogumTarihi,
    #     self.cinsiyet = cinsiyet

    def saveStudent(self, ogrenciNo, ad, soyad, dogumTarihi, cinsiyet):
        sql = "INSERT INTO student(OgrenciNo,Ad,Soyad,DogumTarihi,Cinsiyet) VALUES (%s, %s, %s, %s, %s)"
        value = (ogrenciNo, ad, soyad, dogumTarihi, cinsiyet)

        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi. ')
        except mysql.connector.Error as err:
            print('hata : ', err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO student(OgrenciNo,Ad,Soyad,DogumTarihi,Cinsiyet) VALUES (%s, %s, %s, %s, %s)"
        values = students
        Student.mycursor.executemany(sql, values)
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi. ')
        except mysql.connector.Error as err:
            print('hata : ', err)
        finally:
            Student.connection.close()


#ayse = Student()
#ayse.saveStudent("999", "Ayse", "Ekinci", datetime(2004, 5, 17), "K")


ogrenciler = [
    ("108", "Ahmet", "Yılmaz", datetime(2004, 5, 17), "E"),
    ("109", "Elif", "Balık", datetime(2005, 8, 15), "K"),
    ("110", "Ayşe", "Yorulmaz", datetime(2005, 7, 22), "K"),
    ("111", "Emir", "Sönmez", datetime(2006, 5, 7), "E"),
    ("112", "Sude", "Kaya", datetime(2005, 3, 12), "K"),
    ("113", "Volkan", "Ünal", datetime(2005, 10, 26), "E")
]
Student.saveStudents(ogrenciler)
