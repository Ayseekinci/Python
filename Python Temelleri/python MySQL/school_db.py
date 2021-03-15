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
# ayse = Student()
# ayse.saveStudent("999", "Ayse", "Ekinci", datetime(2004, 5, 17), "K")

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
# Student.saveStudents(ogrenciler)

    @staticmethod
    def StudentInfo():
        sql = "Select * From student"  # tüm kayıtlara eriş.
        # sql = "Select Ad,Soyad From student Where Cinsiyet='K'" #sadece kız öğrencilerin ad ve soyadını yazdırır.
        Student.mycursor.execute(sql)

        try:
            # birden fazla kayıda erişir.
            results = Student.mycursor.fetchall()
            for result in results:
                # print(f"Ad:{result[0]} \t Soyad:{result[1]}")#Sadece kız öğrencilerin ad ve soyad yazdır.
                print(
                    f"Ogrenci No:{result[1]} Ad:{result[2]} \t Soyad:{result[3]}")

        except mysql.connector.Error as err:
            print('hata', err)
        finally:
            Student.connection.close()
# Student.StudentInfo()

    @staticmethod
    # id göre seçme işlemi
    def getStudentId(id):
        sql = "Select * From student Where Id=%s"
        value = (id,)
        Student.mycursor.execute(sql, value)

        try:
            return Student.mycursor.fetchone()  # fetchone=tek bir kişi yazdırman için
        except mysql.connector.Error as err:
            print('hata', err)
        finally:
            Student.connection.close()
# sec = Student.getStudentId(2)#2.ID de kişiye eriş.
# print(sec)

    @staticmethod
    # Günceleme
    def updateStudent(OgrenciNo, Ad, Soyad, DogumTarihi, Cinsiyet):

        sql = "update student set Ad = %s, Soyad= %s, DogumTarihi = %s, Cinsiyet= %s where OgrenciNo = %s"
        values = (Ad, Soyad, DogumTarihi, Cinsiyet, OgrenciNo)
        Student.mycursor.execute(sql, values)

        try:
            Student.connection.commit()
            print(f" { Student.mycursor.rowcount } Tane güncellendi..")
        except mysql.connector.Error as err:
            print("Error", err)

# student = Student()
# OgrenciNo = 101
# Ad = 'B'
# Soyad = 'C'
# DogumTarihi = '1997, 6, 4'
# Cinsiyet = 'K'
# student.updateStudent(OgrenciNo, Ad, Soyad, DogumTarihi, Cinsiyet)

    @staticmethod
    def deleteStudent(id):
        sql = "delete from student where ID = %s"
        value = (id,)
        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f" { Student.mycursor.rowcount } silindii..")
        except mysql.connector.Error as err:
            print("Error", err)

#id = 101
# Student.deleteStudent(id)


# ogrenciler = [

# ("36", "Ahmet", "Yılmaz", datetime(2004, 5, 17), "E"),
# ("37", "Elif", "Balık", datetime(2005, 8, 15), "K"),
# ("38", "Ayşe", "Yorulmaz", datetime(2005, 7, 22), "K"),
# ("39", "Emir", "Sönmez", datetime(2006, 5, 7), "E"),
# ("40", "Sude", "Kaya", datetime(2005, 3, 12), "K"),
# ("41", "Volkan", "Ünal", datetime(2005, 10, 26), "E")
# ]
