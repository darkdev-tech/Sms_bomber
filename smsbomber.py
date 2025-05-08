import os
import requests
import time

def clear():
    os.system('clear')

def banner():
    print("""
\033[1;32m
  ____  __  __ ____   ____                      _             
 / ___||  \/  | __ ) / ___| _ __   ___ ___   __| | ___  _ __  
 \___ \| |\/| |  _ \| |  _ | '_ \ / __/ _ \ / _` |/ _ \| '_ \ 
  ___) | |  | | |_) | |_| || | | | (_| (_) | (_| | (_) | | | |
 |____/|_|  |_|____/ \____||_| |_|\___\___/ \__,_|\___/|_| |_|

        XENOCRYPT TECH | SMS BOMBER
    \033[0m
    """)

def bomb(number, count):
    for i in range(count):
        try:
            # Example API — replace with working endpoints
            response = requests.get(f"https://api.waifu.pics/sfw/smile") # Dummy test API
            print(f"[{i+1}] Sent to {number} | Status: {response.status_code}")
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    clear()
    banner()
    num = input("Enter Victim Number (e.g. +2547xxxxxxx): ")
    cnt = int(input("Enter SMS count: "))
    print("\nStarting attack...\n")
    bomb(num, cnt)
