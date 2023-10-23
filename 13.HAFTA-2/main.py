# from tkinter import *
# def Toplama():
#     r1=int(s1.get())
#     r2=int(s2.get())
#     toplam=r1+r2
#     sonuc["text"]=toplam
#     s1.delete(0,END)
#     s2.delete(0,END)
#
# pencere=Tk()
# pencere.geometry("400x500+300+200") #width X height + xKoordinat + yKoordinat
# pencere.title("HESAPLAMA")
#
#
#
# sayi1=Label(pencere,text="1.Sayı:",fg="purple",bg="yellow",font=("Comic Sans",16))
# sayi1.place(x=5,y=10)
#
# s1=Entry(pencere,text="",font=("Comic Sans",16),bd=3)
# s1.place(x=100,y=10)
#
# sayi2=Label(pencere,text="2.Sayı:",fg="purple",bg="yellow",font=("Comic Sans",16))
# sayi2.place(x=5,y=50)
#
# s2=Entry(pencere,text="",font=("Comic Sans",16),bd=3)
# s2.place(x=100,y=50)
#
# btn_topla=Button(pencere,text="Topla",command=Toplama)
# btn_topla.place(x=100,y=90)
#
#
# sonuc=Label(pencere,text="",fg="purple",font=("Comic Sans",16))
# sonuc.place(x=5,y=140)
#
#
# pencere.mainloop()

###3.UYGULAMA###
from User import User
from tkinter import *
from tkinter import messagebox
import sqlite3
def Login():
    vt=sqlite3.connect("users.db")
    cur=vt.cursor()
    kullaniciadi=Username.get()
    sifre=Password.get()
    cur.execute("Select Name,Surname,Username,Password from User where Username='"+kullaniciadi+"' and Password='"+sifre+"'")
    currentUser=cur.fetchone()

    if currentUser==None:
        messagebox.showerror("HATA","GİRİŞ BAŞARISIZ")

    else:
        messagebox.showinfo("BİLGİ","GİRİŞ BAŞARILI")


def Register():
    pencere.destroy()
    import Register
    Register.pencere.mainloop()

# u=User()

pencere=Tk()
pencere.geometry("700x200+300+200")
pencere.title("LOGIN PANELİ")

username=Label(pencere,text="Username",fg="purple",bg="yellow",font=("Comic Sans",16))
username.place(x=5,y=10)

Username=Entry(pencere,text="",font=("Comic Sans",16),bd=3)
Username.place(x=120,y=10)

password=Label(pencere,text="Password",fg="purple",bg="yellow",font=("Comic Sans",16))
password.place(x=5,y=50)

Password=Entry(pencere,text="",font=("Comic Sans",16),bd=3)
Password.place(x=120,y=50)

login=Button(pencere,text="LOGIN",font=("Comic Sans",16),bd=3,width=12,bg="green",fg="white",command=Login)
login.place(x=120,y=90)
register=Button(pencere,text="REGISTER",font=("Comic Sans",16),bd=3,width=12,bg="blue",fg="white",command=Register)
register.place(x=275,y=90)




pencere.mainloop()