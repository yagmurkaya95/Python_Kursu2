####Replace###
# metin="Benim adım Tarık"
# print(metin.replace("Tarık","Eren"))
# metin2="Benim adım Tarık.Bana Tarık derler"
# print(metin2.replace("Tarık","Doğukan",1))

##sansur ismin bir modül oluşturun.
#Burada bir metod tanımlayın

#Bu metod Liste,gelen kelime,ve değiştirelecek kelime olacak
#şekilde 3 parametre alıcak
#def sansur(list,yasaklıKelime,YeniKelime)

#main içerisinde kelimeyi alabilirsiniz

# import Sansur
#
# c=input("Cümle giriniz")
# print(Sansur.sansur(c,"masa"))

####HAZIR STRING METOTLAR#####
# metin="tarık"
# print(metin.capitalize())
# metin="tarık tablette tarihi kitaplar okutuyor"
# harf=input("Aramak istediğiniz harf giriniz")
# print(metin.count(harf))

#Endswith
# metin="Eren1"
# harf=input("harf giriniz")
# print(metin.endswith(harf))
# metin="tarıkaba"
#(metin.find("a",0)) ## "a" bulunmasını istediğimiz karakteri
#yazarız ("",başlangıç indeksi,nereye kadar bakılacak indeks)
#Aranan kelime ilk önce hangi indeksde ise onun indeks numarasını
#alır.
#FORMAT
# durum1="Benim adım {ad},Ben {yas} yaşındayım".format(ad="Tarık",yas=25)
# print(durum1)
# durum2="Benim adım {0},benim yaşım {1}".format("Tarık",25)
# print(durum2)
# durum3="Benim adım {},yaşım {}".format("Tarık",36)
# print(durum3)
# ad="Tarık"
# yas=23
# print(f"{ad} {yas}")
##INDEX
# metin="Tarık"
# print(metin.index("a"))
##ISALPHA ##Dizideki karakterler alfabade(Harf) ise TRUE döndürür
# metin="ErenKağan"
# print(metin.isalpha())
#ISDECIMAL
# metin="\u0030"
# print(metin.isdecimal())
#ISDIGIT
# metin="123"
# print(metin.isdigit())
#
# a = "\u0030" #unicode for 0
# b = "\u00B2" #unicode for ²
#
# print(b)
# print(a)
# print(a.isdigit())
# print(b.isdigit())
#ISLOWER
# metin="Tarık"
# print(metin.islower())
#ISUPPER
# metin="TARIK"
# print(metin.isupper())
#ISNUMERIC
# metin="4"
# print(metin.isnumeric())
#ISSPACE
# metin=" "
##NOTTEĞER STRING İFADE DOLU İSE SONUÇ FALSE
##YANİ HİÇ BOŞLUK YOK ANLAMINDA
# deger=input("Tarık")
# if deger.isspace()!=False:
#     print("Değer giriniz!!!")
# else:
#     print("Tc kimlik başarılı şekilde kaydedildi.")
# print(deger.isspace())

###ISSPACE METODUNU ARAŞTIRIN...












