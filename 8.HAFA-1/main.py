####DOSYA İŞLEMLERİ#####
"""
Dosya işlemlerinde istenilen isimde bir txt  dosyası oluşturulması ve
Bu txt doyasının içerisine kullanıcıdan alınan veya program tarafından
ortaya çıkarılan verilerin kaydedilmesi.

open() =>Dosya açma işlemi
system() =>Komut(cmd) sistemleri komutlarını yazmaya yarar
getcwd() => Bulunduğumuz dizinin konumu verir
chdir() => Dizin geçişleri
listdir() => Dizindeki Dosya,klasör ne varsa listeler.
mkdir() => Dizindeki bir klasörü açmaya yarar
rmdir() =>Dizindeki klaösrü silmeye yarar
path() => exists methodu ile klasör kontrolü sağlanır

"""
import os #Dosya işlemlerinin yapılabilmesi için os kütüphanesinin projeye
#Dahil edilmesi gerekir.

# print(os.getcwd())
#Bu Komutla içinde bulunduğumuz dosya yolundan farklı bir konuma geçiş yapmış olduk.
# os.chdir(f"C:\\")
# print(os.getcwd())

#Benim projemin bulunmuş odluğu dizinde olan klasörleri/dosyaları
#Listeye atar ve bu şekilde listeler.
# print(os.listdir())
#Konum içerisinde böyle bir klasör var mı yok mu Kontrol edilmesi.
# for i in os.listdir():
#     if i=="deneme":
#         print("Deneme klasörü var")
#     else:
#         print("Böyle bir klasör yok")

#DOSYA OLUŞTURMA İŞLEMİ
#Mkdir() #Verilen adreste istenilen isimde bir klasör oluşturur.
# os.mkdir("C:\\TEST")

#Oluşturulmak istenen dosyanın o konumda olup olmadığını kontrol etmek için
#kullanılan komut
# if not os.path.exists("C:\\TEZ"):
#     os.mkdir("C:\\TEZ")
# else:
#     os.rmdir("C:\\TEZ")

#Belirtilen konumdaki dosyayı siler
# os.rmdir("C:\\TEZ")

#Kendi adında bir klasör oluştursun.
#Bu klasör var mı yok mu kontrol edilip oluşturalacak.
#Bu dosya silinsin

# if not os.path.exists("C:\\TEZ"):
#     os.mkdir("C:\\TEZ")
# else:
#      os.rmdir("C:\\TEZ")
#Hesap makinesini çalıştırma komutu
# os.system("calc") #Hesap makinesini çalıştır komutunu gerçekleştirir.
#Bilgisayarın hostname öğrenme komutu
# os.system("hostname")
#Bİlgisayarın ip adresini öğrenme komutu
# os.system("ipconfig")

#DateTime #
#Sistemden saat bilgisini almaya yarar.
# import datetime
# x=datetime.datetime.now()
# x=x.strftime("%y.%m.%d")
# # print(x)
#
# os.mkdir(f"C:\\TARIK\\{x}")

###DOSYA YETKİ MODLARI####
#w:Dosyaya sadece yazma yetkisi verir.
#a:Dosyaya ekleme yetkisi
#x:Dosyaya sadece yazma yetkisi verilir.(Dosya var ise uyarır yazmaz.
#oluşturur ve yazar
# r:Dosyaya sadece okuma yetkisi verir.

# dizin="C:\\TEST"
# dosya=open(dizin+"\\deneme.txt","w")
# dosya.write("Merhaba Dünya\t\t")
# dosya.write("Ben Kağan")
# dosya.close()

#SORU 1-10 sayılarının karelerini kare.txt isimli bir dosyaya aşağıdaki
#formatta yazdırınız
"""
1 sayısının karesini:1
2 sayısının karesi :4
3 sayısının karesi :9
4 sayısının karesi :16
"""
import os


