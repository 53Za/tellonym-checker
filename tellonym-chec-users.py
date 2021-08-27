import requests
import time
from colorama import Fore, Back, Style
head={
    'authority': 'tellonym.me',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
mta7=open("404.txt","a")
file=open("list.txt","r").read().splitlines()
for user in file:
    url=(f'https://tellonym.me/{user}')
    t=requests.get(url,headers=head)
    print(Fore.GREEN+ str(t.status_code ) + f'{ user}')
    if t.status_code ==404:
        mta7.write(f'{user}\n')
    time.sleep(5)    
mta7.close()    
