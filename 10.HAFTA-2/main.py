###TRY-EXCEPT###
#Hata yakalama(exception) beklenmedik durumlarda programımızın bir hata mesajı
#vermesi,programın çökmesini engellemesi ve istediğimiz bir hata mesajını
#ekrana verdirmesi için kullanılır.

"""
try:
    #Hata kontrolü yapılacak kod bloğunu koyarız.
except:
    #Burada ise hata mesajı verdirilir.Ve hata mesajı verdiğinde
    #Çalışacak kod bu kısma yazılır.
"""

# while True:
#     try:
#         sayi = int(input("Sayi"))
#         break
#     except:
#         print("Rakam giriniz")

#FINALLY

# try:
#     dosya=open("try.txt","w")
#     sayi1=int(input("Sayi giriniz"))
#     dosya.write(str(sayi1))
# except:
#     print("Sayı Rakam olarak giriniz")
# finally:
#     #FINALLY try veya except farketmeksizin çalışır.
#     dosya.close()

#ValueError:Veri dönüştürme işlemi sırasında kullanıcının uygun olmayan bir veri girmesi
#Halinde bu uyarıyı verir.
# sayi=int(input("asdads"))

#ZeroDivisionError
# sayi=12
# sayi2=0
# print(sayi/sayi2)
#
# while True:
#     try:
#         sayi1=int(input("1.Sayi giriniz"))
#         sayi2=int(input("2.Sayi giriniz"))
#         print(sayi1/sayi2)
#         break
#     except ValueError:
#         print("Rakam giriniz lan!!!!")
#     except ZeroDivisionError:
#         print("Sıfıra bölünme hatası")

##SORU: YUKARIDA YAZMIŞ OLDUĞUM KODU ÖYLE Bİ HALE GETİRİNKİ
#1.Sayıyı istedikten sonra 2. sayı hatalı girilirse 1. sayı tekrardan istemesin
#2.Sayıyı tekrardan istesin
#2.Sayıdan sonra sayıları toplayın
#Ve programı bitirin

# while True:
#     try:
#         sayi1=int(input("1. sayıyı giriniz"))
#         break
#     except ValueError:
#         print("1.Sayı rakam girilmedi")
#
# while True:
#     try:
#         sayi2=int(input("2. sayıyı giriniz"))
#         print(sayi1/sayi2)
#         break
#     except ValueError:
#         print("2.Sayı rakam girilmedi")
#     except ZeroDivisionError:
#         print("0 a bölünemez")


#HATA FIRLATMA:TANIMLAMA raise() ####
# try:
#     not1=int(input("Değer giriniz"))
#     if not1<0 or not1>100:
#         raise Exception("Yanlış not girildi")
#     print(not1)
# except OverflowError:
#     print("Vize Notu 0 ile 100 arasında olmalıdır.")

#ASSERT
# email=input("Email Adresiniz")
# assert email=="Trk@gmail.com".lower()
# print(email)


#Dortİslem adında bir metot tanımlayın#
#İki adet sayı alın
#Kullanıcıdan yapılacak işlemi seçiniz
#Eğer girilen ifade +,-,*,/ dışında bir ifade ise assert uyarısı verdirin.
#kullanıcıdan veri alınırken Valuerror verdiğinde değerler birdaha istensin.
#ZeroDivision hatası var mı yok m kontrol ettirilsin.
#
# harf=input("harf girin")
# assert harf=="a" or harf=="b" or harf=="c"
# print("abc birisi girildi")

def Dortislem():
    s1=int(input("1. sayıyı giriniz"))
    s2=int(input("2. sayıyı giriniz"))
    islem=input("İşlem(+,-,*,/)")
    assert islem=="+" or islem=="-" or islem=="/" or islem=="*"
    if islem=="+":
        print(s1+s2)
    elif islem=="-":
        print(s1-s2)
    elif islem=="*":
        print(s1*s2)
    elif islem == "/":
        print(s1 / s2)


try:
    Dortislem()
except ValueError:
    print("Değer hatası")
except ZeroDivisionError:
    print("Sıfıra bölme Hatası")
