#Öğrenci listesi
ogrencilistesi = ["yusuf","ahmet","furkan","ayşe"]
#Öğrenci ekleme fonkisyonu
def ogrenciEkle(ogrenciadi):
    ogrencilistesi.append(ogrenciadi)
#Öğrenci kaldırma fonkisyonu
def ogrenciKaldir(ogrenciadi):
    ogrencilistesi.remove(ogrenciadi)

#Uygulama burada çalışıyor
while True:
    girdi = input("\n Öğrenci eklemek için 'ekle' \n Öğrenci kaldırmak için 'kaldır' yazın \n Çıkış yapmak için 'exit' yazın :    ")
    #Öğrenci eklendi fonkisyonu seçildiğinde ise aşağıda ki kodlar çalışacak
    if girdi == "ekle" and "EKLE" and "Ekle":
        print("--------------------------------- \n "+str(ogrencilistesi))
        ogrenciEkle(input("Eklemek istediğiniz öğrenci adını yazınız : "))
        print("-----------------------------------------------------------")
        print(" Şu an ki durum : "+str(ogrencilistesi))
        print("------------------------------------------------------------")
    #-----------------------------------------------------------------------------


    elif girdi == "kaldır" and "Kaldır" and "KALDIR" and "kaldir" and "KALDİR" and "Kaldir" :
        
        
        
        #Öğrencinin varlığını tespit edip ona göre kaldırmaya çalışan kod parçacığı
        sayac = 1
        while sayac<2:
            print(ogrencilistesi)
            b = input("Kaldıracağınız öğrenci adınızı yazınız : ")
            print("")
            
            for ogrenciarama in ogrencilistesi:
                if(ogrenciarama == b):
                    ogrenciKaldir(b)
                    print("Liste güncellendi \n Son durum : "+ str(ogrencilistesi))
                    sayac += 1
                    continue
                elif(ogrenciarama != b):
                    pass
            print(" Şu an ki öğrenci listeniz : "+str(ogrencilistesi))
            
    elif(girdi == "exit" and "EXİT" and "EXIT" and "exıt" and "Exit" and "Exıt"):
        break

print("----------------------------------------------------------------------------")
print("Bizi tercih ettiğiniz için teşekkürler \n son durum :  "+str(ogrencilistesi))
