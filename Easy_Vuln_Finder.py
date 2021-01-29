import os
import subprocess
import sys, string, os

count = 1





while(count<2):
    print("""___________                         ____   ____      .__            ___________.__             .___         
    
\_   _____/_____     ______ ___.__. \   \ /   /__ __ |  |    ____   \_   _____/|__|  ____    __| _/ ____ _______ 
 |    __)_ \__  \   /  ___/<   |  |  \   Y   /|  |  \|  |   /    \   |    __)  |  | /    \  / __ |_/ __ \\_  __ \
 |        \ / __ \_ \___ \  \___  |   \     / |  |  /|  |__|   |  \  |     \   |  ||   |  \/ /_/ |\  ___/ |  | \/
/_______  /(____  //____  > / ____|    \___/  |____/ |____/|___|  /  \___  /   |__||___|  /\____ | \___  >|__|   
        \/      \/      \/  \/                                  \/       \/             \/      \/     \/        
Easy Vuln Finder
By redahackaze.org MyPoison | ig: @yusuf.ngs    \n """)
    keyboard = input("The developers who make this application do not accept any responsibility. Do you accept my terms(Y/N) ? \n \neasyvuln > ")
    if(keyboard == "Y" or keyboard == "y" or keyboard == "yes" or keyboard == "YES"):
        while True:
            select = input("""\n1)Collecting information from the server.
2)Offensive Vuln analysis from target server.
3)For download requirements(If you have not installed the requirements, you must install the requirements)
4)For Exit

easyvuln > """)
            if(select == "1"):
                #deneme için
                selectattack = input("\n1)Nmap Analysis \n2)Automatic Analysis \n3)for exit \n \neasyvuln > ")
                count2 = 1
                while(count2<2):
                    if(selectattack == "1"):
                        target = input("Enter Target... \neasyvuln > ")
                        os.system("nmap.exe -sS -sU -T4 -A -v "+target)
                    elif(selectattack == "3"):
                        print("Process stoped...")
                        count2 += 1
                    else:
                        print("Try again. Wrong choice")


            elif(select == "3"):
                print("installing requirements....")
                os.system("start req\scansql\req.bat")
                
                
                
            elif(select == "2"):
                selectattack = input("\n1) Offensive Vuln With SQLMAP \n2)SQLI Vuln Scanner \n3)Automatic Attack \n4)for exit \n \neasyvuln > ")
                count2 = 1
                while(count2<2):
                    if(selectattack == "1"):
                        target = input("Enter the link with weakness easyvuln > ")
                        os.system("python sqlmap\sqlmap.py "+target+" --dbs")
                    elif(selectattack == "2"):
                        target = input("Enter the target(you must use the http/https) easyvuln > ")
                        os.system("python scansql\scanqli.py -u "+target)
                    elif(selectattack == "4"):
                        count2 += 1

                        
                #deneme için
                print(target)
            elif(select == "4"):
                count += 1
                break



            else:
                print("Enter correct argument")
    elif(keyboard != "Y"):
        print("You can't use it without accepting")
        break

print("\nSee you , bye :)")
