#Parametre olarak aldığı listedeki, tek elemanları yazdıran fonksiyonu yazınız.
#HAKAN
listem=[]
# def tekyaz(list,miktar):
#     for i in range(miktar):
#         sayi=int(input("Sayi giriniz: "))
#         list.append(sayi)
#     print(list)
#     for i in range(miktar):
#         if list[i]%2==0:
#             continue
#         else:
#             print(list[i])
# miktar=int(input("Kac defa veri gireceksiniz: "))
#
# tekyaz(listem,miktar)

# def CokluGoster(*sayilar):
#     for i in sayilar:
#         print(i)
#
# CokluGoster(2,3,4)
# CokluGoster(12,12,12,321,456,899,123)
"""
Kendisine gönderilen karakter,en,boy  parametrelerine göre ekrana
karakterden dikdörtgen çizen programı yazınız. en boy'a göre.

"""
"""
#SELİM
"""
# def dikdortgenolusturma(en,boy,karakter):
#     for i in range(boy):
#         print(f"{karakter}"*en)
# en=int(input("lütfen en giriniz: "))
# boy=int(input("lütfen boy giriniz: "))
# karakter=input("lütfen karakter giriniz: ")
#
# dikdortgenolusturma(en,boy,karakter)
##ÇAĞLA HANIM
# satir=int(input("dikdörtgen satır sayısını giriniz"))
# sutun=int(input("dikdörtgen sütun bilgisi giriniz"))
#
# for sutun in range (sutun):
#      print("*  "*satir)


#####DEĞER DÖNDÜREN FONKSİYONLAR####

# def toplama(s1,s2):
#     toplam=s1+s2
#
#
# S=toplama(23,45)
# print(s)

# def kuvvet(sayi,us):
#     sonuc=sayi**us
#     return sonuc #Sonucu döndürmek için kullanılır
#
# s=kuvvet(2,3)
# print(s)

#Kendisine gönderilen 4 sayının ortalamasını döndüren fonksiyonu yazınız.

# def ortalama(s1,s2,s3,s4):
#     return (s1+s2+s3+s4)//4
#
# print(ortalama(23,56,76,90))
"""
Kendisine gönderilen listedeki sayıların aritmetik ortalamasını bulan program.
"""
# def ortalama(notlar):
#     toplam=0
#     for i in notlar:
#         toplam+=i
#     return toplam//len(notlar)
#
# sinif=[45,65,87]
# print(ortalama(sinif))
"""
Kendisine parametre olarak gönderilen sayının faktörüyelini hesaplayıp döndüren fonk
"""
#EREN VE KAĞAN
# def faktryl(sayi):
#     carpim=1
#     for s in range(1,sayi+1):
#         carpim*=s
#     return carpim
# sayi=int(input("Sayi giriniz"))
# f=faktryl(sayi)
# print(f)
"""
Kendisine gönderilen sayının asal olup olmadığını döndüren fonksiyonu yazınız.
"""
# def AsalMi(sayi):
#     if(sayi==1):
#         return False
#     if(sayi==2):
#         return True
#     for  i in range(2,sayi):
#         if(sayi%i==0):
#             return False
#     return True
#
# if AsalMi(5):
#     print("Asal")
# else:
#     print("Asal değil")
#









