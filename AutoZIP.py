from colorama import Fore
from zipfile import ZipFile
import os,time,sys,random,string

p = f'{Fore.WHITE}[{Fore.RED}ZIP{Fore.WHITE}] '
pi = p
s = f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}ZIP{Fore.WHITE}] '

def smart():
    zip_label = input(f'{pi}Zip name: ')
    amount = int(input(f'{pi}File amount: '))
    color_change = 0
    file_count = 0
    zip = ZipFile(f'{zip_label}.zip', 'w')
    for i in range(amount):
        file_count += 1
        string_len = random.randint(500, 5000)
        label_len = random.randint(50, 75)
        filetype = ''.join(random.choice(string.ascii_letters) for i in range(25))
        file_label = ''.join(random.choice(string.ascii_letters) for i in range(label_len))
        randomstring = ''.join(random.choice(string.printable) for i in range(string_len))
        filename = f'{file_label}_{file_count}.{filetype}'
        file = open(f'{filename}', 'w')
        file.write(f'{randomstring}')
        file.close()
        zip.write(f'{filename}')
        os.remove(f'{filename}') 
        msg = f' > Successfully added {filename} to zip archive'
        if color_change == 0:
            print(f'{Fore.GREEN}[{Fore.WHITE}ZIP{Fore.GREEN}]{msg}')
            color_change = 1
        else:
            print(f'{Fore.LIGHTGREEN_EX}[{Fore.WHITE}ZIP{Fore.LIGHTGREEN_EX}]{msg}')
            color_change = 0
        os.system(f'title Auto ZIP - Progress: {file_count}/{amount}')
    print(f'\n{s}Successfully created zip archive with {file_count} files')
    zip.close()

def auto():
    zip_label = input(f'{pi}Zip name: ')
    file_label = input(f'{pi}File name: ')
    amount = int(input(f'{pi}File amount: '))
    string_len = int(input(f'{pi}String length (recommended 500+): '))
    ft = input(f'{p}File type (zip/rar): ')
    if ft == 'rar':
        filetype = 'rar'
    else:
        filetype = 'zip'
    zip = ZipFile(f'{zip_label}.{filetype}', 'w')
    file_count = 0
    print(f'{p}Config was applied, zipbomb is being created.. please wait.')
    time.sleep(0.5)
    for i in range(amount):
        file_count += 1
        filename = f'{file_label}_{file_count}.txt'
        content = ''.join(random.choice(string.printable) for i in range(string_len))
        open(f'{filename}', 'x')
        t = open(f'{filename}', 'w')
        t.write(f'{content}')
        t.close()
        zip.write(f'{filename}')
        try:
            os.remove(f'{filename}')
        except Exception as e:
            print(f'{p}Error: {Fore.RED}{e}')
        os.system(f'title Auto ZIP - Progress: {file_count}/{amount}')
        print(f'{s}Successfully created and added {filename} to {filetype} archive')
    zip.close()
    print(f'\n{s}Successfully created zipbomb named {zip_label}.{filetype} with {file_count} files')

def onlaunch():
    os.system('title AutoZIP')
    print(f'''{Fore.RED} ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████  ▒███████▒ ██▓ ██▓███  
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒ ▒ ▒ ▄▀░▓██▒▓██░  ██▒
{Fore.BLUE}▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒░ ▒ ▄▀▒░ ▒██▒▓██░ ██▓▒
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░  ▄▀▒   ░░██░▒██▄█▓▒ ▒
{Fore.GREEN} ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒███████▒░██░▒██▒ ░  ░
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░▒▒ ▓░▒░▒░▓  ▒▓▒░ ░  ░
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░░▒ ▒ ░ ▒ ▒ ░░▒ ░     
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░ ░ ░ ░ ░ ▒ ░░░       
      ░  ░   ░                  ░ ░    ░ ░     ░           
                                     ░                     
           
''')
    select()

def select():
    os.system('title AutoZIP')
    c = input(f'{pi}')
    if c == 'help':
        print(f'{pi}Commands:\n{p}{Fore.LIGHTBLACK_EX}> start <auto/smart>')
    elif c == 'start auto':
        auto()
    elif c == 'start smart':
        smart()
    else:
        print(f'{p}{Fore.RED}Invalid selection: {Fore.LIGHTRED_EX}try "help"')
    select()

onlaunch()