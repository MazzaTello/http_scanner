import requests
from colorama import Fore, init


init(autoreset=True)  # reset colors

try:
    url = input("Enter URL: ")

    # check if empty
    while url == "":
        url = input("Enter URL: ")

    # check http/https
    if not url.startswith(('http://', 'https://')):
        print(Fore.YELLOW + "URL must start with http:// or https://")
        exit()

    # get request
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()

    # show status
    print(Fore.CYAN + f"\nStatus: {resp.status_code} - {resp.reason}")

    # show headers
    print("\n--- Headers ---")
    for key, value in resp.headers.items():
        print(f"{key}: {value}")

    # show content
    print(f"\nContent Preview:\n{resp.text[:100]}...")

except requests.exceptions.Timeout:
    print(Fore.RED + "Timeout. Server too slow.")

except requests.exceptions.RequestException as e:
    print(Fore.RED + f"Error: {e}")