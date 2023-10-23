
# SORU: 1-200 arasında 20 sayı üretip bunu sayilar isimli listeye atayın.
# import random
# list=[]
# for i in range(20):
#     #sayi=random.randint(1,200)
#     list.append(random.randint(1,200))
#
# print(list)

#Yukarıdaki listenin elemanlarını tek mi çift mi ayırın.Tekleri ayrı Çiftleri Ayrı bi listeye atın

# import random
# list=[]
# for i in range(20):
#     #sayi=random.randint(1,200)
#     list.append(random.randint(1,200))
#
# print(list)
#
# cift=[]
# tek=[]
#1.YOL
# for i in list:
#     if i%2==0:
#         cift.append(i)
#     else:
#         tek.append(i)
#2.YOL
# for i in range(len(list)):
#     if list[i]%2==0:
#         cift.append(list[i])
#     else:
#         tek.append(list[i])

#
# print("Tek liste:",tek)
# print("Cift Liste:",cift)
##ECENİN ÇÖZÜMÜ
# import random
# list=[]
# list1=[]
# list2=[]
# for i in range(20):
#     number=random.randint(1,200)
#     list.append(number)
#
# print(list)
#
# for i in list:
#     if i%2==0:
#         list1.append(i)
#
#     else:
#         list2.append(i)
#
# print(list1)
# print(list2)

##Klavyeden alınan 5 kelimeyi bir listeye atan program

#Girilen kelimelerin listede olup olmadığını kontrol ettiriniz
# list=[]
# for i in range(5):
#     kelime=input("kelime giriniz")
#     list.append(kelime)
#
# k=input("Kelime kontrolü!")
#
# if k in list:
#     print("Kelime listede var")
# else:
#     print("Kelime yok")

##RAKAMLARDAN DİK ÜÇGEN
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

#KISA YÖNTEM
# for i in range(1,10):
#     print(f"{i}"*i,)

#UZUN YÖNTEM
# for i in range(10):
#     for j in range(i):
#         print(i,end=" ")
#     print( )

##PİRAMİT
# sayac=1
# for satir in range(1,11):
#     print(" "*(10-satir),end=" ")
#     print("*"*sayac)
#     sayac+=2

##1-50 arasında 15 adet sayı üretip bir listeye atın
#Listedeki sayıların toplamını ve ortalamasını bulun
# import random
#
# list=[]
# toplam=0
#
# for i in range(15):
#     list.append(random.randint(1,50))
#
# for i in list:
#     toplam+=i
#
# print(f"Toplam:{toplam}")
# print(f"Ortalama:{toplam/len(list)}")

