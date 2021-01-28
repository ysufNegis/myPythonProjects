import os
while True:
    a = int(input(""" Merhaba , nasılın ? Hızlı matemaitk uygulamasına hoş geldin. Aşağıda numaralara göre lütfen karar ver.
    1)Sayının karesiniz bulmak
    2)0 ile seçilen sayı arasında ki sayıların tek veya çift sayılarını bulma
    3)sayıyı asal çarpanlara ayırmak için
    4)Uygulamadan çıkış yap \n örnek: 1  :  """))
    if(a==1):
        print("kare hesaplama açıldı")
        print("--------------------------------")
        girdi = int(input("Sayıyı giriniz: "))
        sonuc = girdi*girdi
        girdi = str(girdi)
        sonuc = str(sonuc)
        print("---------------------------------------------- \n" + girdi+" sayısının karesi: "+sonuc)
        devam = int(input("""Seçim yapınız
        1)Devam etmek için
        2)Çıkış yapmak için \n örnek:2 : """))
        if(a==2):
            break
    elif(a==2):
        print("Tek veya çift hesaplama modu açıldı")
        print("-----------------------")
        secim = input("Tek sayıları hesaplamak için tek yazın \n Çift sayıları hesaplamak için çift yazın :  ")
        if(secim == "tek" and "Tek" and "TEK" and "TeK"):
            sayi = int(input("Sayıyı giriniz : "))
            sayac = 1
            while(sayi>=sayac):
                sayi2 = sayi
                sayi2 = str(sayi2)
                sayac = sayac + 1
                
                if(sayac%2==1):
                    sayacstr = sayac
                    sayacstr = str(sayacstr)

                    print(sayi2+" ile 0 arasındaki tek sayılar: "+sayacstr)
            print("---------------------------------------")
        elif(secim == "çift" and "cift" and "ÇİFT" and "CIFT" and "CİFT"):
            sayi = int(input("Sayiyi giriniz : "))
            sayac = 1
            while(sayi>=sayac):
                sayi2 = sayi
                sayi2 = str(sayi2)
                sayac = sayac + 1
                sayacstr = sayac
                sayacstr = str(sayacstr)
                if(sayac%2==0):
                    print("0 ile "+sayi2+" arasındaki çift sayılar "+sayacstr)
                    #burası değişkenlik gösterir
    
        devam = input("""
Seçim yapınız
1)Devam etmek için
2)Çıkış yapmak için    

varsayılan: 1  
---------------------------------------
seçim: """)
        
        if(devam == "2"):
            os.system("taskkill /F /IM python.exe")
            break
        elif(devam > "2"):
            print(" -------------------------------------------------- \n doğru bir argüman girin")

    




    elif(a==4):
        os.system("taskkill /F /IM python.exe")
    elif(a==3):
        os.system("python modül1.py")
        break
        
print("--------------------------------------------------------------------")
print("Bizi tercih ettiğiniz için teşekkür ederiz yine bekleriz :D")