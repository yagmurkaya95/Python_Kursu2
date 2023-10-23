##SORU:
##Kullanıcının girdiği küçük sayıdan büyük sayıya kadar olan sayıları
#sayilar.txt isimli dosya içerisine yazdırınız.
#Klasör ve Txt dosyası oluşturma kısmı
# import os
# os.mkdir("C:\\sayilar")
# dizin="C:\\sayilar\\"
# dosya=open(dizin+"sayilar.txt","w")

#Başlangıç ve bitiş değerleri alma ve kontrol ettirme
# bas=int(input("Başlangıç"))
# bit=int(input("Bitiş"))
# if bas>bit:
#     bit,bas=bas,bit
# with open("sayilar.txt","w") as file:
#     while bas<bit:
#         file.write(str(bas)+"\n")
#         bas+=1

###DOSYA OKUMA İŞLEMLERİİ###

# dosya=open("personeller.txt","r+",encoding="utf-8")
#readLine():her çalışmadan 1 data okur

# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())
#ELEMANLARI WHİLE DÖNGÜSÜ İLE EKRANA YAZDIRMA
# while(True):
#     isim=dosya.readline()
#     if(isim!=""):
#         print(isim.rstrip("\n"))
#         continue
#     else:
#         print("Eleman bitti")
#         break

#READLINES ile bütün dosyayı tek seferde okursunuz.
# print(dosya.readlines()) ##
#TXT DOSYASI İÇİNDEKLERİ LİSTEYE ATMA VE EKRANA YAZDIRMA
# ogrencilerlistesi=dosya.readlines()
# print(ogrencilerlistesi)
# for i in ogrencilerlistesi:
#     print(i,end="")
#DOSYAYI LİSTEYE ATIP İÇİNDE ELEMAN ARAMA

# for i in ogrencilerlistesi:
#     if ("Icardi"+"\n")==i:
#         print("VAR")
#         break

# for i in range(len(ogrencilerlistesi)):
#     print(ogrencilerlistesi[i])

#read():Belirtilen karakter sayısı kadar okuma yapar
# print(dosya.read(18))

# isimler=["Tarık","KAĞAN","Yağmur","Çağla","Eren"]
#
# ad="Tarık Hamarat"
# print(ad.split("k"))

#dosya=open("sinif.txt","r",encoding="utf-8")
#1-Öncelikle ogrenciler.txt isimli bir dosya oluşturun
#2-İçerisine NOT İSİM SOYİSİM olacak şekilde veriler giriniz.
#3-Bu dosya içerisindeki verileri readlines() kullanarak bir
#listeye atın.
#4-Listeyi forla döndürün.Her bir i yi splitle boşluklardan bölerek
#0. indeksdekini not listesine 1.indeksdekini isim listesine atın
#5-Notlar listesinin ortalamasını yazdırın
#6-Notlar listesindeki Maksimum ve minimum öğrencilerinin indekslerini
#alarak bu indeksleri isimler listesinde yerlerine koyun
#Böylece en başarılı ve başarısız öğrenci ismi çıksın

# dosya=open("sinif.txt","r",encoding="utf-8")
# isimler=[]
# notlar=[]
#
# ogrenciler=dosya.readlines()
# for i in ogrenciler:
#     notlar.append(int(i.split(" ")[0]))
#     isimler.append(i.split(" ")[1])
# print(notlar)
# print(isimler)
#
# print(sum(notlar)/len(notlar))
# print(isimler[1])
# print(notlar[1])
# print(isimler[notlar.index(max(notlar))])
# print(isimler[notlar.index(min(notlar))])


