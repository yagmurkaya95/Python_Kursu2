####OBJECT ORIENTED####
###OOP-TEMELLERİ###
"""

1-INHERITANCE(Miras alma kalıtım)
2-Polymorphism-Çok Biçimlilik
3-Encapsulation-Kapsülleme
4-Abstraction-Soyutlama

"""
#
# ad="Tarık"
# soyad="Hamarat"
# yas=25
# boy=1.85
# kilo=75
#
# ad2="Kağan"
# soyad2="Solhan"
# yas2=10
# boy2=1.85
# kilo2=60
#
# class Personel:
#     ad=""
#     soyad=""
#     yas=0
#     medeniDurum=""
#     sgkGirisTarihi=""

#Instance(Örnek oluşturma)
# personeller=list()
# p=Personel()
# p.ad="Tarık"
# p.soyad="hamarat"
# p.medeniDurum="Bekar"
# print(type(p.soyad))
# print(p.soyad)
# personeller.append(p)
#
# p1=Personel()
# p1.ad="Kağan"
# p1.soyad="Solhan"
# p1.medeniDurum="Evli"
# personeller.append(p1)


# print(personeller)
#Nesne taşıyan listeyi yazdırma
# for i in personeller:
#     print(i.ad)
#Nesne taşıyan listeyi Filtreleme
# for i in personeller:
#     if i.medeniDurum=="Bekar":
#         print(i.ad,i.soyad)

##CLASS METOTLAR,STATIC METOTLAR,SELF METOTLAR

"""
class ClassName:
    **Class Özellikleri
    Class method:Sadece class üzerindeki özelliklere ulaşmak için kullanılır.
    Self Method:Class içerisinde nesne üzerinden çağrılır.
    Static Method:Hem class hem object üzerinden erişilebilir.
"""
# class Ogrenci:
#     ad=""
#     soyad=""
#     numara=0
#
#    def RegisterList(self):
#         o=list()
#         self.ad = input("Ad giriniz")
#         self.soyad = input("Soyad giriniz")
#         self.numara = int(input("Numara giriniz"))
#         o.append(self)
#         for i in o:
#             print(i.ad,i.soyad)
#
# listem=list()
# ogr=Ogrenci()
# ogr.RegisterList()

#SORU:BUZDOLABI Marka Model Hacim Fiyat
#Kayıt metodu
# class Buzdolabi:
#     marka=""
#     model=""
#     hacim=""
#     fiyat=""
#     def Ekle(self,liste):
#             self.marka=input("Marka:")
#             self.model = input("Model:")
#             self.hacim = input("Hacim:")
#             self.fiyat = input("Fiyat:")
#             liste.append(self)
#
#     def Listele(self,liste):
#         for i in liste:
#             print(i.marka,i.model,i.hacim,i.fiyat)


#
# listem=list()
# for i in range(2):
#     b = Buzdolabi()
#     b.marka=input("Marka giriniz")
#     listem.append(b)
#
# for i in listem:
#     print(i.marka)

##ÖĞRENCİ VE ÖĞRETMEN KAYIT
##Öğrenci Ad soyad Okul-No Branş
##Öğretmen Ad soyad Hoca-No Branş
#Listeye Ekleme-Listeleme
class Ogretmen:
    ad=""
    soyad=""
    Hocano=""
    Brans=""
    def Kayıt(self,liste):
        self.ad=input("Ad:")
        self.soyad=input("Soyad:")
        self.Hocano=input("Hoca no:")
        liste.append(self)
        for i in liste:
            print(i.ad,i.soyad,i.Hocano)

ogretmenlist=list()
ogrt=Ogretmen()
ogrt.Kayıt(ogretmenlist)

class Ogrenci:
    ad=""
    soyad=""
    OgrNo=""
    Brans=""
    def Kayıt(self,liste):
        self.ad=input("Ad:")
        self.soyad=input("Soyad:")
        self.OgrNo=input("Hoca no:")
        liste.append(self)
        for i in liste:
            print(i.ad,i.soyad,i.OgrNo)

ogrlist=list()
ogr=Ogrenci()
ogr.Kayıt(ogrlist)

