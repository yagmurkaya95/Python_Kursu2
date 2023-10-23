###ÖRNEK###
#
# import os ##Projeye dahil ediyorum
# dosyaAdresi="C:\\TEST\\"
#
# dosyaAdresi=dosyaAdresi+"karealma.txt"
# dosya=open(dosyaAdresi,"w")
#
# for i in range(1,11):
#     dosya.write(str(i)+"Sayısının Karesi:"+str(i**2)+"\n")
#
# dosya.close()

#SORU: 1-100 arası ürteilen 10 adet rastgele sayıyı Rastgele.txt isimli
# bir dosyaya atınız

# import os
# import random
#
# os.mkdir("C:\\rastgele")
# dosyayolu="C:\\rastgele\\"
# dosyayolu=dosyayolu+"rastgele.txt"
# dosya=open(dosyayolu,"w")
# dosya.write("Rastgele Sayılar\t\tTam Sayılar\n")
#
# for i in range(10):
#     dosya.write(str(random.randint(1,100))+"\t\t\t\t"+str(random.randint(1,100))+"\n")


# import os
# import random
#
# os.mkdir("C:\\rastgele")
# dosyayolu="C:\\rastgele\\"
# dosyayolu=dosyayolu+"rastgele.txt"
# dosya=open(dosyayolu,"w")
# dosya.write("Olay zamanı\t\tOlay sırası\t\tRastgele sayı\n")
#
# for i in range(10):
#     dosya.write(str(random.randint(1,100))+"\t\t\t\t"+str(random.randint(1,100))+"\n")

#ÇÖZÜM

# import random
# import datetime
#
# dizin="C:\\log"
# dosya=open(dizin+"\\log.txt","w")
# dosya.write("zaman\t\t\t\t\t+Olay sırası\t\tRastgele Sayı\n")
# for i in range(1,11):
#     dosya.write(str(datetime.datetime.now())+"\t\t\t"+str(i)+"\t\t\t"+str(random.randint(1,100))+"\n")

#
#İlk adım-> 1-100 arasında 20 tane sayı üretilsin
#2.adım -> Üretilen sayıları bir listeye atın
#3.adımda -> Liste elemanları tek mi çift mi Kontrol edilsin
#4.adım -> tekcift.txt dosyayı içerisine aşağıdaki formatta yazdırılsın
# Tekler   Çiftler
#   1
#            24

# import random
#
# list=[]
# for i in range(1,21):
#     list.append(random.randint(1,100))
#
# dizin="C:\\tekcift"
# dizin=dizin+"\\tekcift.txt"
# dosya=open(dizin,"w")
#
# dosya.write("ÇİFT\t\t\tTEK\n")
# for i in list:
#     if i%2==0:
#         dosya.write(str(i)+"\n")
#     else:
#         dosya.write("\t\t\t"+str(i)+"\n")



