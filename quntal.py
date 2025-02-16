import os
import time
import pwinput
from colorama import Fore, Style, init
init()
host = "quntal"
os.system("cls")
def boot_sequence():
    print("Starting up mterm...")
    time.sleep(0.2)
    print("Starting up greeter2...")
    time.sleep(0.1)
    print("Starting up nelservices...")
    time.sleep(0.2)
    print("Starting up botload-probe...")
    time.sleep(0.12)
    print("Starting up yash...")
    time.sleep(0.6)
    print("Deploying all packages...")
    time.sleep(0.1)
    print("Initializing...")
    time.sleep(0.2)
    print("Booting...")
    time.sleep(0.8)
    os.system("cls")
    print("Welcome to Quntal!")
    time.sleep(2)
    os.system("cls")
def print_logo():
    print(r"""               
                    _        _                                   
                   | |      | |
   __ _ _   _ _ __ | |_ __ _| |
  / _` | | | | '_ \| __/ _` | |
 | (_| | |_| | | | | || (_| | |
  \__, |\__,_|_| |_|\__\__,_|_|
     | |                    
     |_|                        
""")
import os
import requests
def setup(github_url):
    response = requests.get(github_url)
    if response.status_code == 200:
        file_name = github_url.split("/")[-1]
        temp_path = os.path.join(os.getcwd(), file_name)
        with open(temp_path, "wb") as file:
            file.write(response.content)
        main_folder = os.path.join(os.getcwd(), "main")
        if not os.path.exists(main_folder):
            os.makedirs(main_folder)
        destination_path = os.path.join(main_folder, file_name)
        os.rename(temp_path, destination_path)
    else:
        print(f"Error: {response.status_code}")
def quntal(username, passwd):
    login_file = os.path.join(os.getcwd(),"main","login.dll")  
    with open(login_file, "r") as file:
        users = file.readlines()
    for user in users:
        stored_username, stored_password = user.strip().split(",")
        if username == stored_username and passwd == stored_password:
            while True:
                x = input(Style.BRIGHT + Fore.BLUE + f"{username}@{host}" + Style.RESET_ALL + Fore.WHITE + " : " + Fore.GREEN + Style.DIM + "$ " + Fore.WHITE + Style.RESET_ALL)
                if x.startswith("pakage install"):
                    print("Searching..")
                    time.sleep(0.2)
                    if requests.get(f"https://raw.githubusercontent.com/berkayguldal1/quntal/main/{x[15:]}"+".py").status_code == 200:
                        print(f"Found {x[15:]} at quntal/pakage/{x[15:]}")
                    else:
                        print(f"Could not found {x[15:]}.")
                        continue
                    time.sleep(0.2)
                    print(f"Downloading {x[15:]}...")
                    setup(f"https://raw.githubusercontent.com/berkayguldal1/quntal/main/{x[15:]}"+".py")
                    print(f"pakage: Installed {x[15:]} (main/{x[15:]})")
                elif x == "exit":
                    os.system("cls")
                    print("Goodbye!")
                    time.sleep(1)
                    os.system("cls")        
                    return
                elif x == "clear" or x == "cls":
                    os.system("cls")
                elif x == "info":
                    print_logo()
                    print("previously xoxOS, now as Quntal!")
                elif x == "newuser":
                    wusername = input("Enter a username: ")
                    wpassword = pwinput.pwinput(prompt="Enter a password: ")
                    with open(login_file, "a") as file:
                        file.write(f"{wusername},{wpassword}\n")
                    print(f"Created user {wusername}.")
                else:
                    try:
                        file_path = os.path.join(os.getcwd(), "main", str(x) + ".py")
                        with open(file_path, "r") as file:
                            exec(file.read())
                    except Exception as e:
                        print(f"yash: Not able to run {x}, it's either missing or doesn't exist.")
    print("Invalid username or password.")
    time.sleep(1)
    os.system("cls")
    login()
def login():
    login_file=os.path.join(os.getcwd(),"main","login.dll")
    if not os.path.exists(os.path.join(os.getcwd(),"main")) or os.stat(login_file).st_size == 0:
        os.mkdir("main")
        print("No user found. Please create a new user.")
        fusername = input("Enter a username: ")
        fpassword = pwinput.pwinput(prompt="Enter a password: ")
        dpassword= pwinput.pwinput(prompt="Enter a dev account password: ")
        with open(login_file, "w") as file:
            file.write(f"{fusername},{fpassword}\n")
            file.write(f"dev,{dpassword}\n")
        print(f"Created user {fusername} and dev account.")
        time.sleep(1)
        os.system("cls")
    print_logo()
    username = input("Login: ")
    os.system("cls")
    time.sleep(0.6)
    print_logo()
    passwd = pwinput.pwinput(prompt="Password: ")
    time.sleep(0.8)
    os.system("cls")
    quntal(username, passwd)
boot_sequence()
login()