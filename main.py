import sys, random, os, time
from colorama import Fore

if not os.path.exists('Results'):
    os.makedirs('Results/Edits')
    
def simpleedit():
    os.system('title AUTOEDIT V1 - Adding Special Symbol - module ')
    with open('combo.txt', 'r') as f: 
        lines = f.read().split('\n')   
        random.shuffle(lines)
        output_file = open('Results/Edits/Symbols.txt','w+')
        edited = []
        for line in lines:
            email, password = line.split(':')
            edited.append({'email':email,'password':password})
            print(Fore.LIGHTGREEN_EX+'[EDITED] '+Fore.LIGHTBLUE_EX+line,end='\n')
            output_file.write('{}:{}!\n'.format(email, password))
        output_file.close()
        print(Fore.GREEN+'Done !')
        time.sleep(3)
        sys.exit()
        
def extractdomain():
    os.system('title AUTOEDIT V1 - Extract Domain - module ')
    with open('combo.txt', 'r') as f: 
        lines = f.read().split('\n')   
        random.shuffle(lines)
        output_file = open('Results/Edits/ExtractSpecificDomain.txt','w+')
        edited = []
        domaintoextract = input(str(Fore.LIGHTCYAN_EX+'Domain To Extract ? ->> '))
        for line in lines:
            if domaintoextract in line:
                
                email, password = line.split(':')
                edited.append({'email':email,'password':password})
                print(Fore.LIGHTGREEN_EX+'[EXTRACTED] '+Fore.LIGHTBLUE_EX+line,end='\n')
                output_file.write('{}:{}\n'.format(email, password))
        output_file.close()
        print(Fore.GREEN+'Done !')
        time.sleep(3)
        sys.exit()
        
def appendtotheend():
    os.system('title AUTOEDIT V1 - Append To The End Of The Password - module ')
    with open('combo.txt', 'r') as f: 
        lines = f.read().split('\n')   
        random.shuffle(lines)
        output_file = open('Results/Edits/AppendToTheEnd.txt','w+')
        edited = []
        appendend = input(str(Fore.LIGHTCYAN_EX+'What do You Want To Append  ->>  '))
        for line in lines:
            email, password = line.split(':')
            edited.append({'email':email,'password':password})
            print(Fore.LIGHTGREEN_EX+'[EDITED] '+Fore.LIGHTBLUE_EX+line,end='\n')
            output_file.write('{}:{}{}\n'.format(email, password, appendend))
        output_file.close()
        print(Fore.GREEN+'Done !')
        time.sleep(3)
        sys.exit()   

def capitalizepass():
    os.system('title AUTOEDIT V1 - Capitalize Pass -  module ')
    with open('combo.txt', 'r') as f: 
        lines = f.read().split('\n')   
        random.shuffle(lines)
        output_file = open('Results/Edits/CapitalizedPass.txt','w+')
        edited = []
        for line in lines:
            email, password = line.split(':')
            edited.append({'email':email,'password':password})
            print(Fore.LIGHTGREEN_EX+'[EDITED] '+Fore.LIGHTBLUE_EX+line,end='\n')
            output_file.write('{}:{}\n'.format(email, password.title()))
        output_file.close()
        print(Fore.GREEN+'Done !')
        time.sleep(1)
        sys.exit()
        

def lowercasepass():
    os.system('title AUTOEDIT V1 - Lowercase Password - module ')
    with open('combo.txt', 'r') as f: 
        lines = f.read().split('\n')   
        random.shuffle(lines)
        output_file = open('Results/Edits/LowercasePassword.txt','w+')
        edited = []
        for line in lines:
            email, password = line.split(':')
            edited.append({'email':email,'password':password})
            print(Fore.LIGHTGREEN_EX+'[EDITED] '+Fore.LIGHTBLUE_EX+line,end='\n')
            output_file.write('{}:{}\n'.format(email, password.lower()))
        output_file.close()
        print(Fore.GREEN+'Done !')
        time.sleep(1)
        sys.exit()
        
def capitalizeandsymbolpass():
    os.system('title AUTOEDIT V1 - Capitalize And Add Symbol - module ')
    with open('combo.txt', 'r') as f: 
        lines = f.read().split('\n')   
        random.shuffle(lines)
        output_file = open('Results/Edits/CapitalizedAndSymbol.txt','w+')
        edited = []
        for line in lines:
            email, password = line.split(':')
            edited.append({'email':email,'password':password})
            print(Fore.LIGHTBLUE_EX+'[EDITED] '+Fore.LIGHTCYAN_EX+line,end='\n')
            output_file.write('{}:{}!\n'.format(email, password.title()))
        output_file.close()
        print(Fore.GREEN+'Done !')
        time.sleep(1)
        sys.exit()     
        
def proedits():
    os.system('title AUTOEDIT V1 - ProEdits - module ')
    with open('combo.txt', 'r') as f: 
        lines = f.read().split('\n')   
        random.shuffle(lines)
        output_file = open('Results/Edits/ProEdits.txt','w+')
        edited = []
        for line in lines:
            try:
                email, password = line.split(':')
                edited.append({'email':email,'password':password})
                print(Fore.LIGHTBLUE_EX+'[EDITED] '+Fore.LIGHTCYAN_EX+line,end='\n')
                output_file.write('{}:{}\n'.format(email, password))
                output_file.write('{}:{}\n'.format(email, password.title()))
                output_file.write('{}:{}!\n'.format(email, password.title()))
                output_file.write('{}:{}!\n'.format(email, password.lower()))
                output_file.write('{}:{}$\n'.format(email, password.title()))
                output_file.write('{}:{}$\n'.format(email, password.lower()))
            except:
                pass
        output_file.close()
        print(Fore.GREEN+'Done !')
        print(Fore.GREEN+'Shuffling lines  ')
        
    with open('Results/Edits/ProEdits.txt', 'r') as f: 
        lines2 = f.read().split('\n')   
        random.shuffle(lines)
            
        output_file.close()
        print(Fore.GREEN+'doneeeee')
        time.sleep(1)
        sys.exit()  
def combocleaner():
            
    os.system('title AUTOEDIT V1 - Adding Special Symbol - module ')
            
    with open('combo.txt', 'r') as f: 
        lines = f.read().split('\n')   
        random.shuffle(lines)
        output_file = open('Results/cleancombo.txt','w+')
        edited = []
        try:
            for line in lines:
                email, password = line.split(':')
                edited.append({'email':email,'password':password})
                print(Fore.LIGHTGREEN_EX+'[EDITED] '+Fore.LIGHTBLUE_EX+line,end='\n')
                output_file.write('{}:{}\n'.format(email, password))
            output_file.close()
            print(Fore.GREEN+'Done !')
            time.sleep(3)
            sys.exit()
        except:
            print(Fore.LIGHTGREEN_EX+'[REMOVED LINE] '+Fore.LIGHTBLUE_EX+line,end='\n')
            pass    
        
def menu():
    os.system('title AUTOEDIT V1 - Idle ')
    print(Fore.LIGHTMAGENTA_EX+"""

                      888                          888 d8b 888    
                      888                          888 Y8P 888    
                      888                          888     888    
     8888b.  888  888 888888 .d88b.   .d88b.   .d88888 888 888888 
        "88b 888  888 888   d88""88b d8P  Y8b d88" 888 888 888    
    .d888888 888  888 888   888  888 88888888 888  888 888 888    
    888  888 Y88b 888 Y88b. Y88..88P Y8b.     Y88b 888 888 Y88b.  
    "Y888888  "Y88888  "Y888 "Y88P"   "Y8888   "Y88888 888  "Y888 
                                                                  
                                                                  
            [Automated Combo Editing Tool By cracked.io/jetson]
                    """)
    time.sleep(0.5)
    print(Fore.LIGHTRED_EX+'Basic Modules')
    print(Fore.LIGHTRED_EX+'')
    print(Fore.LIGHTRED_EX+'[1] Add Special Symbol To Password')
    print(Fore.LIGHTRED_EX+'[2] Capitalize First Letter In Password')
    print(Fore.LIGHTRED_EX+'[3] Capitalize And Add Symbol')
    print(Fore.LIGHTRED_EX+'[4] Capitalize First Letter In Email')
    print(Fore.LIGHTRED_EX+'[5] Append To The End Of Password')
    print(Fore.LIGHTRED_EX+'[6] Email:Pass To User:Pass (coming)')
    print(Fore.LIGHTRED_EX+'[7] Lowercase The Pass')
    print(Fore.LIGHTRED_EX+'[8] Extract Lines With Specific Domains')
    print(Fore.LIGHTRED_EX+'[9] Extract Pass With Minimum Lenght')
    print(Fore.LIGHTRED_EX+'')
    print(Fore.LIGHTCYAN_EX+'Streaming Targetted Edits')
    print(Fore.LIGHTCYAN_EX+'[1] Mycanal (coming)')
    print(Fore.LIGHTRED_EX+'')
    print(Fore.LIGHTGREEN_EX+'Gaming Targetted Edits')
    print(Fore.LIGHTGREEN_EX+'[1] Minecraft (coming)')
    print(Fore.LIGHTRED_EX+'')
    print(Fore.LIGHTBLUE_EX+'Special !')
    print(Fore.LIGHTBLUE_EX+'[99] Max Edits')
    print(Fore.LIGHTRED_EX+'')
    print(Fore.LIGHTWHITE_EX+'Cleaning Combos (coming)')
    print(Fore.LIGHTWHITE_EX+'[88] Clean Combos(coming)')
    print(Fore.LIGHTRED_EX+'')
    choix = input(str(Fore.LIGHTYELLOW_EX+'What do You want ?  ->>  '))
    
    if choix == "1":
        simpleedit()
    elif choix == "2":
        capitalize()
    elif choix == "3":
        capitalizeandsymbolpass()
    elif choix == "4":
        capitalizeemail()
    elif choix == "5":
        appendtotheend()
    elif choix == "6":
        emailtouser()
    elif choix == "7":
        lowercasepass()
    elif choix == "8":
        extractdomain()
    elif choix == "9":
        ExtractMinimumLenght()
    elif choix == "99":
        proedits()
    elif choix == "88":
        combocleaner()
    else:
        sys.exit()
menu()