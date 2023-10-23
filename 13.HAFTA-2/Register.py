from tkinter import *
from tkinter import messagebox
from User import User
import sqlite3
vt=sqlite3.connect("users.db")
cur=vt.cursor()

def Register():
    user =User()
    user.name=Name.get()
    user.surname=Surname.get()
    user.username=Username.get()
    user.password=Password.get()
    komut="INSERT INTO USER(NAME,SURNAME,USERNAME,PASSWORD) values (?,?,?,?)"
    cur.execute(komut,(user.name,user.surname,user.username,user.password))
    vt.commit()
    messagebox.showinfo("BİLGİ","KAYIT BAŞARILI")
    Name.delete(0,END)
    Surname.delete(0,END)
    Username.delete(0,END)
    Password.delete(0,END)


pencere=Tk()
pencere.geometry("700x800+300+200")
pencere.title("Regıster Panel")

name=Label(pencere,text="Name:",fg="purple",bg="yellow",font=("Comic Sans",16))
name.place(x=5,y=10)

Name=Entry(pencere,text="",font=("Comic Sans",16), bd=3)
Name.place(x=110,y=10)

surname=Label(pencere,text="Surname:",fg="purple",bg="yellow",font=("Comic Sans",16))
surname.place(x=5,y=50)

Surname=Entry(pencere,text="",font=("Comic Sans",16), bd=3)
Surname.place(x=110,y=50)

username=Label(pencere,text="Username:",fg="purple",bg="yellow",font=("Comic Sans",16))
username.place(x=5,y=90)


Username=Entry(pencere,text="",font=("Comic Sans",16), bd=3)
Username.place(x=110,y=90)

password=Label(pencere,text="Password:",fg="purple",bg="yellow",font=("Comic Sans",16))
password.place(x=5,y=130)

Password=Entry(pencere,text="",font=("Comic Sans",16), bd=3)
Password.place(x=110,y=130)

register=Button(pencere,text="REGISTER",font=("Comic Sans",16), bd=3,width=20,command=Register).place(x=110,y=170)

pencere.mainloop()



