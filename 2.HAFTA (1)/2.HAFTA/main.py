##Atama Operatörü
# (=)
# sayi=5
# İşlemli Atama Operatörleri
# sayi=5
# print(sayi)
# sayi+=5 sayi=sayi+5
# print(sayi)
# sayi-=3 sayi=sayi-3
# print(sayi)
# sayi*=5 sayi=sayi*5
# sayi/=1 sayi=sayi/1
# print(sayi)

# Aritmetik Operatörler
# +,-,*:toplama,çıkarma,çarpma
# /: ondalıklı Bölme
# // :tamsayı bölme
# ** :Üs alma 7**2 dersek 7 nin karesini al
# % :Mod alma(Bölme işlemindeki kalanı verir) sayi=7%2 kalan kısmı verir.
# sayi=5//2

##Karşılaştırma Operatörleri
# sayi1=8
# sayi2=8
#
# sonuc1=sayi1==sayi2
# sonuc2=sayi1!=sayi2
# sonuc3=sayi1>=sayi2
# sonuc4=sayi1<=sayi2
# print(sonuc1)
# print(sonuc2)
# print(sonuc3)
# print(sonuc4)

# print(8%4==1)
# print(8%4==0)

# MANTIKSAL OPERATÖRLER
# Birden fazla koşul kontrolü yapılacak ve her koşulun ayrı olarak doğruluğu sorgulanacaksa
# Mantıksal Operatörler Devreye girer.
"""
0:False
1:True

AND BAĞLACI
and
Username    Password   Sonuc
   0          0      =   0
   0          1      =   0
   1          0      =   0
   1          1      =   1
"""
# username="tarik"
# sifre="123"
#
# kullaniciadi=input("Kullanici adinizi girin")
# password=input("Şifrenizi giriniz")
#
# girisDurumu=kullaniciadi==username and sifre==password
#
# print(girisDurumu)

##MANTIKSAL VEYA OPERATÖRÜ
# or
"""
0:False
1:True

0  0  = 0
0  1  = 1
1  0  = 1
1  1  = 1



"""
# email="trkhamarat"
# phone="5555"
# sifre="123"
#
# user=input("Email/phone")
# password=input("Sifre gir")
#
# girisDurumu= (user==email or user==phone) and password==sifre
#
# print(girisDurumu)

##Soru Kullanıcı adı ve şifre bilgisi tanımlayınız
##ve giriş için bunları and bağlacı ile kontrol ettiriniz.

#
# ilce="Mecidiyeköy"
#
# # print("Mec" in ilce)
# #
# # print("köy" in ilce)
#
# print("ad" not in ilce)

###IF-ELSE AKIŞ KONTROL #######
"""Program akışında bir sonuca duruma veya değere bağlı olarak kod akışı devam edecek ise
if else bir defa tanımlanır.Alternatif durumlar için ise elif bloğu kullanırız.
"""
"""




"""

# if kosul1:
#     #Kosul 1 sağlanırsa çalışacak kod kısmı
# elif kosul2:
#     # kosul 2 sağlanırsa açlışacak kod kısmı
# elif kosul3:
#     # kosul 3 sağlanırsa açlışacak kod kısmı
# else:
#     #Hiçbir koşul sağlanmazsa else kısmı çalışır.

# yas=int(input("Yas giriniz"))
# if yas>17:
#     print("Ehliyet alabilir")
# else:
#     print("Ehliyet alamaz")

##SORU:HAFTANIN KAÇINCI GÜNÜNDE OLDUĞUMUZU KULLANICIDAN ALALIM VE GİRİLEN SAYIYA GÖRE
# KARŞILIK GELEN GÜNÜ EKRANA YAZDIRALIM
# .lower() --> klavyeden okunan değeri küçük harfe çevirir.
# .upper() --> klavyeden okunan değeri büyük harfe çevirir.

# gun=input("Gün").upper()
# if gun=="pazartesi":
#     print("PAZARTESİ")
# elif gun=="salı":
#     print("SALI")
# elif gun=="çarşamba":
#     print("ÇARŞAMBA")
# elif gun=="perşembe":
#     print("PERŞEMBE")
# elif gun=="cuma":
#     print("CUMA")
# elif gun=="cumartesi":
#     print("CUMARTESİ")
# elif gun=="pazar":
#     print("PAZAR")
# else:
#     print("BÖYLE BİR GÜN YOK!")

##Kare alma sayi**2 sayi**3
##SORU Klavyeden girilen sayi 100 den büyükse karesini
##Küçükse küpünü ekrana yazdırın

# sayi=int(input("Sayiyi giriniz"))
#
# if sayi>100:
#     print("Sayinin karesi:",sayi**2)
# elif sayi==100:
#     print("Sayimiz:",sayi)
# else:
#     print("Sayinin küpü:",sayi**3)

##Kullanıcıdan alınan sayının tek mi çift mi olduğunu ekrana yazdıralım
# sayi=int(input("Sayiyi giriniz"))
# if sayi%2==0:
#     print("Çifttir")
# else:
#     print("Tektir")

##PRINT FORMATLARI
# sayi=5
# ad="Tarık"
# print("Sayi:",sayi)
# print("Sayi:{} Ad:{}".format(sayi,ad))
# print(f"SAYİ:{sayi+5} Isim:{ad}")
# print(f"Sayi:{sayi} Isim:{ad}")

##KLAVYEDEN GİRİLEN DEĞERİN TAMSAYI KONTROLÜ
# sayi=input("Sayi giriniz")
# sayi=int(sayi)
# print(type(sayi))

# sayi=12
# if type(sayi)==float:
#     print("Ondalıklı")
# elif type(sayi)==int:
#     print("Tamsayi")

##ARALIK KONTROLU
# sayi=10
#
# if sayi>=0 and sayi<11:
#     print("0-10 aralığı")
# elif sayi>10 and sayi<21:
#     print("11 -20 aralığı")
# elif 20<sayi<31:
#     print("21-30 aralığı")

# Öğrencinin Vize ve final notlarını alınız ortalamayı hesaplayın.
# Ortalamaya denk düşen harf notunu ekrana yazdırın
# 0-24=>FF
# 25-44=>DD
# 45-54=>CD
# 55-69=>CC
# 70-84=>BB
# 85-100=>AA
# vize=int(input("Vize giriniz"))
# final=int(input("Final notu giriniz"))
# ortalama=(vize+final)/2
#
# if ortalama>=0 and ortalama<=24:
#     print("FF")
# elif ortalama>24 and ortalama<=44:
#     print("DD")
# elif ortalama>44 and ortalama<=54:
#     print("CD")
# elif ortalama>54 and ortalama<=69:
#     print("CC")
# elif ortalama>69 and ortalama<=84:
#     print("BB")
# elif ortalama>84 and ortalama<=100:
#     print("AA")
# else:
#     print("HATALI NOT GİRİŞİ")

# vize=float(input("Vize:"))
# final=float(input("Final:"))
# ortalama=(vize+final)/2 #ortalama vizenin %40 ile finalin %60 toplamını ile hesaplanıyor
# print(ortalama)
# if 0<=ortalama<25:
#     print("FF")
# elif 24<ortalama<45:
#     print("DD")
# elif 44<ortalama<55:
#     print("CC")
# elif 54<ortalama<70:
#     print("CB")
# elif 69<ortalama<85:
#     print("BB")
# elif 84<ortalama<=100:
#     print("AA")

