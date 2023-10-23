##################FONKSİYONLAR##########################
#Fonksyion Nedir?
"""
Programımızda belirli bir işi yapan kod bloklarının tekrar kullanılması durumunda
tekrar tekrar yazılmadan çağrılmasını sağlayan programlayıcının oluşturmuş olduğu
hazır modüllerdir.

1 Modül 1 defa tanımlanıp istediğimiz kadar ve istediğimiz yerde kullanabilmemizi sağlar

Fonksiyonlar yazdığımız programın modüler olmasını sağlar,ayrıca kod okunabilirliğini arttırır.
"""
#Fonksiyon çağrıldığı yerden önce tanımlanmalıdır

#Fonksiyon Nasıl oluşturulur ?
"""
def fonksiyonismi(varsa parametre):
    #Fonksiyon içerisinde çalışacak kodları buraya yazıyorum
    
"""
#
# def MerhabaYaz():
#     print("Merhaba")
#
#
# MerhabaYaz()

#global keyword,fonksiyon içerisindeki değişkenleri local olmaktan çıkartır.

# def Degistir():
#     global sayi1,sayi2
#     sayi1,sayi2=100,200
#     print(sayi1+sayi2)
#
#
#
#
# Degistir()
#
# print(sayi1+sayi2)

##Parametre Alan Fonksiyonlar
# def Topla(s1,s2):
#     sonuc=s1+s2
#     print(f"Toplam:{sonuc}")
#
# Topla(45,67)

##Topla  ve çıkar adında iki metot tanımlayın Kullanıcıdan alınan değerlerle
#Toplama ve çıkarma işlemlerini yaptırın.
# def Topla(s1,s2):
#     sonuc=s1+s2
#     print(f"Toplam:{sonuc}")
# def Cikar(s1,s2):
#     sonuc=s1-s2
#     print(f"Fark:{sonuc}")

#
# sayi1=int(input("Sayi1 giriniz"))
# sayi2=int(input("Sayi2 giriniz"))
#
# Topla(sayi1,sayi2)
#
# sayi3=int(input("Sayi1 giriniz"))
# sayi4=int(input("Sayi2 giriniz"))
#
# Cikar(sayi3,sayi4)

# def dortislem(s1,s2,islem):
#     if islem=='+':
#         sonuc=s1+s2
#         print(sonuc)
#     elif islem=='-':
#         sonuc=s1-s2
#         print(sonuc)
#     elif islem=='*':
#         sonuc=s1*s2
#         print(sonuc)
#     elif islem=='/':
#         sonuc=s1//s2
#         print(sonuc)
#
# sayi1=int(input("birinci sayıyı giriniz"))
# sayi2=int(input("ikinci sayıyı giriniz"))
# islem=input("işlem tipini giriniz")
# dortislem(sayi1,sayi2,islem)


#Kendisine gönderilen ismi gönderilen sayı kadar ekrana yazdıran metot

# def EkranaYazdir(isim,sayi):
#     for i in range(sayi):
#         print(isim)
#
# ad=input("Ad giriniz ")
# adet=int(input("Kaç kere çalışacak giriniz"))
# EkranaYazdir(ad,adet)

#Kendisine gönderilen sayı adedi kadar isim alıp listeye atan program
# isimler=list()
# def İsimEkle(sayi):
#     for i in range(sayi):
#         isim=input("Ad giriniz")
#         isimler.append(isim)
#     print(isimler)
#
#
# adet=int(input("Adet giriniz"))
# İsimEkle(adet)


#kendisine gönderilen sayının Tek mi? Çift mi ? olduğunu ekrana yazdıran fonks.

#ÖDEV  # Parametre olarak aldığı listedeki tek elemanları yazdıran fonksiyonu yazınız.