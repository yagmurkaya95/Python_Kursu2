# ####List###
# ##İçerisinde birden fazla veriyi tutabilir.
# # sayilar1=[] #Boş bir liste tanımlamış.
# # sayilar2=list() #Boş bir liste tanımlamış olduk
# #
# # sayilar3=[0,1,2,3,4,5] #El ile liste elemanları atamış olduk.
# #
# # print(sayilar3)
# # print(sayilar3[0])
# # print(sayilar3[3])
#
# # sayiListe=[10,7,6,5,33,44,19]
# # print(sayiListe[5])
#
# # karisikListe=[34,"İstanbul",46,"KahramanMaraş",58,"Sivas"]#İnt ve String ifade içeren Liste
# # print(karisikListe[1])
#Etkinlik
##Boş bir liste tanımlansın bu liste içerisine Ad-soyad-yaş-doğum yeri-plaka

# ##Listeye Eleman Ekleme
# EklemeListesi=[12,23,45]
# EklemeListesi+=[60]
# EklemeListesi+=["Tokat"]
# # Listeye Eleman Ekleme 2.Yol
# EklemeListesi.append(17)
# EklemeListesi.append("Çanakkale")
# # print(EklemeListesi)
# #Listeden Veri Silme#
# # EklemeListesi.remove(60)
# # EklemeListesi.remove("Çanakkale")
# # print(EklemeListesi)
# ##İndis ile eleman silme
# # del EklemeListesi[1]
# # print(EklemeListesi)
# ##Çoklu eleman Ekleme
# # EklemeListesi+=[10,"Balıkesir",41,"Kocaeli"]
#
# #İstenilen indekse eleman Ekleme
# # EklemeListesi.insert(3,"Tarık")
# # EklemeListesi.insert(0,"Yaren")
# # EklemeListesi.insert(2,"Gamze")
# # EklemeListesi.insert(9,"Kağan")
# print(EklemeListesi)

#İstenilen elemanın indeksini bulma
# sayilar = [10,20,30,40,20,20,20,20]
# # print(sayilar.index(20,2))#2.indeksten başla ilk 20 yi gördüğünde indisini yazdır
# # print(sayilar.index(20,5))
#
# #Dizinin uzunluğunu bulma
# print(len(sayilar))
#
# #Dizi içerisinde bir elemandan kaç tane var olduğunu bulma
# print("Listedeki 20 adeti:",sayilar.count(40))
#
listem = ["Manisa","Çanakkale","Kocaeli","Konya","Sivas","Gaziantep"]
sayiListesi=[150,63,45,65,213,90]
#Sondan başlayarak elemanları yazdırmamıza yarar.
# print(listem[-1])
# print(listem[-2])
# print(listem[-6])
#Sort Metodu ->Liste elemanlarını küçükten büyüğe sıralar
# listem.sort()
# sayiListesi.sort()
#
#
# print(sayiListesi)
# Elemanları tersten sıralamaya yarar
# sayiListesi.reverse()
# print(sayiListesi)

#POP METODU
# sayilar = [10,20,30,40,50]
# soneleman = sayilar.pop()
# print(soneleman)
# soneleman2 = sayilar.pop(2)# 2.indeks 3.elemanı listeden çıkar
# print(soneleman2)

#In komutu
# rakamlar = [1,4,5,6,7,8]
# kontrol=20 in rakamlar
#
# if 5 in rakamlar:
#     print("Rakamlar içerisinde 5 sayısı var")
# else:
#     print("Rakamlar içerisinde 5  sayısı yok")

# if 5 not in rakamlar:
#     print("Rakamlar içerisinde 5 sayısı yok")
# else:
#     print("Rakamlar içerisinde 5  sayısı var")

#İki listeyi toplama
# list1=[1,2,3]
# list2=[4,5,6]
# list3=["Tarık","Hamarat","İstanbul"]
# listeler=list1+list2+list3
# print(listeler)
#Max metodu
list=[1,4,23,54,67]
# print(max(list))
# #Min Metodu
# print(min(list))

#For döngüsü ile liste içindeki elemanları yazdırma
# rakamlar=[i for i in range(10)]

# for i in list:
#     print(i,end=" ")

#Listeleri Kopyalama

# liste1=[11,22,33]
# # liste2=liste1
# liste2=liste1.copy()
# print(liste2)

##ALIŞTIRMALAR##
#Kullanıcıdan 10 sayı alıp bir listeye atın ve listenin ortalamasını yazdırın.
# list=[]
# toplam=0
# for i in range(5):
#     sayi=int(input("Sayi giriniz"))
#     list.append(sayi)
#     toplam+=sayi
#
# for i in list:
#     toplam+=i
# print("Ortalama:",(toplam)/len(list))
# print(list)

#1-100 arasında 20 adet sayı üretip bir listeye atınız
# list=[]
# import random
# for i in range(20):
#     list.append(random.randint(1,100))
#
# print(list)
#Kullanıcıya 3 tahmin hakkı verip listeden 1 sayıyı tahmin etmesini isteyiniz
# list=[23,67,87,56]
#
# for i in range(3):
#     tahmin=int(input("Tahmininiz"))
#     if(tahmin in list):
#         print("Tebrikler doğru tahmin")
#         break
#     else:
#         print("Tahmin yanlış")
#










