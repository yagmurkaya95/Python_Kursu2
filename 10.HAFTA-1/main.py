#HASTA KAYIT SİSTEMİ
##ÖDEV HERŞEY AYNI KAYIT SİLME GÜNCELLEME OLACAK
#EK OLARAK:
#Datetime ile kayıt zamanınıda listeye ekleyin
#HASTANE KAYIT
#HASTA AD SOY AD YAS ŞİKAYET
#not(ŞİKAYET BİLGİSİDE EKLENECEK ŞİKAYETE GÖRE İLAÇ ÖNERİSİ) SADECE HAKAN ABİYE ÖZEL







while True:

    secim=int(input("1-Çalışan kayıt\n2-Çalışan Sil\n3-Çalışan Bilgi Güncelle\n4-Çıkış"))
    #Kayıt Ekleme
    if secim==1:
        print("Kayıt Ekleme Ekranı")
        while True:
            birimsec=int(input("1-IK\n2-Muhasebe\n3-IT\n4-Çıkış"))
            if birimsec==1:
                Ekle("IK")
            elif birimsec==2:
                Ekle("Muhasebe")
            elif birimsec==3:
                Ekle("IT")
            elif birimsec==4:
                break
    elif secim==2:
        print("Silme ekranı")
        while True:
            birimsec = int(input("1-IK\n2-Muhasebe\n3-IT\n4-Çıkış"))
            if birimsec == 1:
                Sil("IK")
            elif birimsec == 2:
                Sil("Muhasebe")
            elif birimsec == 3:
                Sil("IT")
            elif birimsec == 4:
                break
    elif secim==3:
        print("Güncelleme Ekranı")
        while True:
            birimsec = int(input("1-IK\n2-Muhasebe\n3-IT\n4-Çıkış"))
            if birimsec == 1:
                Guncelle("IK")
            elif birimsec == 2:
                print("Muhasebe")
            elif birimsec == 3:
                print("IT")
            elif birimsec == 4:
                break
    elif secim==4:
        break