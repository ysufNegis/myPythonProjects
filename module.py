import os
while True:
    #buraya hesaplama gelecek------------------------------------------------------------------------------
    sayi = int(input("Asal çarpanlarını bulacağınız sayıyı giriniz : "))

    j = 2
    while(j<=sayi):
        if(sayi%j==0):
            
            jstr = j
            jstr = str(jstr)
            sayistr = sayi
            sayistr = str(sayistr)
            print(sayistr+" sayısının çarpanları : "+jstr)
            sayi = sayi/j
        else:
            j+=1


    
    #---------------------------------------------------------------------------------------------------
    devam = input("------------------------------------------------------- \n Tekrar hesaplamak için 1'e basın \n Ana sayfaya dönmek için  2'e \n Uygulamayı kapatmak 3'e basın:  ")
    if(devam == "2"):
        print("-----------------------------------------------------")
        os.system("python matttool.py")

    elif(devam == "3"):
        
        exit()
    
        while True:
            devam = input("------------------------------------------------------- \n Tekrar hesaplamak için 1'e basın \n Ana sayfaya dönmek için  2'e \n Uygulamayı kapatmak 3'e basın : ")
            if(devam == "2"):
                print("-----------------------------------------------------")
                
                break

            elif(devam == "3"):
                exit()
            else:
                print("------------------------------------- \n geçersiz argüman")


            


    
