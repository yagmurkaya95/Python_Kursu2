##Döviz Ofisi olalım
##Gelen dolar ve euro için ayrı birer metot oluşturunuz
#Gelen parametre TL yi dolar/Euro ya çevirin
#Sonucu Geri döndürün.
#DOLAR-18
#EURO-19
# dolar=18
# euro=19
# def Euro(para):
#     sonuc=para/euro
#     return sonuc
# def Dolar(para):
#     sonuc = para / dolar
#     return sonuc
#
# tl=int(input("Dolara çevirmek istediğiniz tutarı giriniz"))
# print(Euro(tl))
# print(Dolar(tl))

###METOT İÇERİSİNDE METOT ÇAĞIRMA###RECURSIVE METHODS
# def Buyuk2(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# def Buyuk3(x,y,z):
#     return Buyuk2(x,Buyuk2(y,z))
#
# print(Buyuk3(11,23,9))

##TEK SATIRDA METOD TANIMLAMA

# kare=lambda s:s*s
# print(kare(4))
# sayi=int(input("Sayi giriniz"))
# print(kare(sayi))
# topla=lambda a,b:a+b
# sayi=int(input("Sayi giriniz"))
# sayi2=int(input("Sayi ikiyi giriniz"))
# print(topla(sayi,sayi2))

#Topla,çarp,Çıkar 3 tane tek satır metot tanımlayıp işlem sonuçlarını
# ekrana yazdırınız
# carpim=lambda s1,s2:s1*s2
# toplam=lambda s1,s2:s1+s2
# cikarma=lambda s1,s2:s1-s2
#
# print(carpim(45,50))
# print(toplam(40,5))
# print(cikarma(10,5))

##Modül oluşturup projeye dahil etme.
# import random
# 3 kere 3 parametre alan ve bu sayıların ortalamasını
# hesaplayıp bir listeye atan bir modül ve içerisinde bir fonk
#tanımlayın

import Test


list=[]
for i in range(3):
    Test.ortalama(list)

print(list)















