import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class


class DbManager:

    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self, id):
        sql = "select * from student where id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            # return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6])
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('hata', err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('hata', err)

    def deleteStudent(self, studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi. ')
        except mysql.connector.Error as err:
            print('hata : ', err)

    def getStudentsByClassId(self, ClassId):
        sql = "select * from student where ClassId=%s"
        value = (ClassId,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('hata', err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO student(OgrenciNo,Ad,Soyad,DogumTarihi,Cinsiyet,ClassId) VALUES (%s, %s, %s, %s, %s,%s)"
        value = (student.OgrenciNo, student.Ad, student.Soyad,
                 student.DogumTarihi, student.Cinsiyet, student.ClassId)

        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi. ')
        except mysql.connector.Error as err:
            print('hata : ', err)

    def editStudent(self, student: Student):
        sql = "update student set  OgrenciNo=%s, Ad = %s, Soyad = %s, DogumTarihi = %s, Cinsiyet = %s, ClassId = %s where id= %s"
        value = (student.OgrenciNo, student.Ad, student.Soyad,
                 student.DogumTarihi, student.Cinsiyet, student.ClassId, student.id)

        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi. ')
        except mysql.connector.Error as err:
            print('hata : ', err)

        print("db silindi")

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass


db = DbManager()
#Student = db.getStudentById(111)
#Student[0].Ad = 'Murat'
# Student[0].OgrenciNo = "116"
# db.editStudent(Student[0])
# db.addStudent(Student[0])

# print(Student[0].Ad)
# print(Student[0].Soyad)
# print(Student.Cinsiyet)
# student = db.getStudentsByClassId(1)
# print(student[0].Ad)
