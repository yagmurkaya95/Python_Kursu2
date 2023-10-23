###SQL -VERİTABANI ###

"""
SQL NEDİR ? AÇILIMI NEDİR?
STRUCTURED QUERY LANGUAGE

SQL YAZILIMI:MSSQL,Oracle,SQLİTE,MySQL,PostgreSQL


Database:Her proje bir database ile entegre olmalıdır.Genelde proje ile aynı ismi taşır.
"""
#
# import sqlite3
# vt=sqlite3.connect("okul.db")

#DDL :Create,alter,drop,truncate

# cursor=vt.cursor()
# komut="""
#     create table if not exists Ogrenci
#     (
#     Numara int,
#     Isim text,
#     Soyisim varchar(20),
#     Sinif varchar(20)
#     )
#
# """
# cursor.execute(komut)

#DML-Crud komutlar:Insert,Select,Update,Delete
#DML komutlarında insert,update,delete yapıldığında commit() function çağrılmalıdır.
#TABLOYA VERİ EKLEME
# komut="INSERT into Ogrenci (Numara,Isim,Soyisim,Sinif) values (1,'Tarık','Hamarat','Lise1')"
# komut="INSERT into Ogrenci (Isim,Numara,Soyisim,Sinif) values ('Yağmur',234,'Kaya','Lise2')"

# cursor.execute(komut)
# vt.commit()

#GÜNCELLEME
# komut="Update Ogrenci set Sinif='Lise5' where Isim='Tarık' "
# cursor.execute(komut)
# vt.commit()



#TABLODAN VERİ SİLME
# komut="Delete from Ogrenci where Numara=234"
# cursor.execute(komut)
# vt.commit()

##TABLODAN VERİ OKUMA
# komut="SELECT Numara,Isim,Soyisim,Sinif FROM Ogrenci"
# cursor.execute(komut)

# print(cursor.fetchone())
# print(cursor.fetchone())

# ogrenciler=cursor.fetchall()
# print(ogrenciler)

# students=[(3,'Kerem','Demirci','Lise1'),(4,'Duru','Demirci','Lise2')]
# komut="Insert into Ogrenci values(?,?,?,?)"
# cursor.executemany(komut,students)
# vt.commit()


##TKINTER##

from tkinter import *

pencere=Tk()
pencere.geometry("400x500+800+200") #width x height +xKordinat +yKordinat

yazi=Label(pencere,text="Ad:",fg="purple",bg="yellow",font=("Comic Sans",16))
yazi.place(x=5,y=10)

ad=Entry(pencere,text="",font=("Comic Sans",16),bd=3)
ad.place(x=100,y=10)

yazi2=Label(pencere,text="Soyad:",fg="purple",bg="yellow",font=("Comic Sans",16))
yazi2.place(x=5,y=70)

soyad=Entry(pencere,text="",font=("Comic Sans",16))
soyad.place(x=100,y=70)

btn_Degistir=Button(pencere,text="DEĞİŞTİR",font=("Comic Sans",16)).place(x=100,y=133)

sonuc=Label(pencere,text="SONUC:",fg="purple",bg="yellow",font=("Comic Sans",16))
sonuc.place(x=5,y=140)

#Program çalıştırmak için kullanılır.
pencere.mainloop()