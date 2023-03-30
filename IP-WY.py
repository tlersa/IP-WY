import requests, webbrowser, socket
from ast import Try
from email import header

try:
    import requests, webbrowser, socket
    from ast import Try
    from email import header
except ImportError:
    os.system("pip install requests")
    os.system("pip install webbrowser")
    os.system("pip install socket")
    os.system("pip install ast")
    os.system("pip install email")

    os.system("clear")

#--------------------------------
Black = "\033[1;30m"       #Black
White =" \033[1;37m"       #White
Gray = "\033[1;39m"        #Gray
Red = "\033[1;31m"         #Red
Green = "\033[1;32m"       #Green
Yellow = "\033[1;33m"      #Yellow
Blue = "\033[1;34m"        #Blue
Purple = "\033[1;35m"      #Purple
Cyan = "\033[1;36m"        #Cyan
#--------------------------------

print(Red+"""
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀               ██▓ ██▓███   █     █░▓██   ██▓
    ⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇             ▓██▒▓██░  ██▒▓█░ █ ░█░ ▒██  ██▒
    ⢤⣀⣀⣀⠀⢸⣷⡄⠀ ⣀⣤⣴⣿⣿⣿⣆            ▒██▒▓██░ ██▓▒▒█░ █ ░█   ▒██ ██░
      ⠹⠏⠀⠀⣿⣧ ⠹⣿⣿⣿⣿⣿⡿⣿            ░██░▒██▄█▓▒ ▒░█░ █ ░█   ░ ▐██▓░
           ⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟           ░██░▒██▒ ░  ░░░██▒██▓   ░ ██▒▓░
            ⠦⠴⢿⢿⣿⡿⠷⠀⣿
 Website IP Info Or Your IP?     ░▓  ▒▓▒░ ░  ░░ ▓░▒ ▒     ██▒▒▒
        ⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃               ▒ ░░▒ ░       ▒ ░ ░   ▓██ ░▒░
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿                 ▒ ░░░         ░   ░   ▒ ▒ ░░
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀                ░               ░     ░ ░
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁                 ░ \n""")
print(White+"This Tool Was Programmed By : TLER AL-BISHI", "\nWebsite For All Accs : "+Blue+"https://linktr.ee/tler.sa")
print(White+"- "*25)

print("[1] - Website IP Info | [2] - Your Device IP")
option = input("Choose A Number : ")

if option == "1":
    URL = input(Red+"[1] - Enter The URL : ")
    Website_IP = socket.gethostbyname(URL)
    print(Green+"URL IP is : \033[31m" +Website_IP)

    website_ip_info = input(Red+"[2] - Enter The IP : ")
    def ipinfo():
        url1 = f'https://demo.ip-api.com/json/{website_ip_info}?fields=66842623&lang=en'
        headers1 = {
	    'Accept': '*/*',
	    'Accept-Encoding': 'gzip, deflate, br',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Connection': 'keep-alive',
	    'Host': 'demo.ip-api.com',
	    'Origin': 'https://ip-api.com',
	    'Referer': 'https://ip-api.com/',
	    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': "Windows",
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-site',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36' }
        req1 = requests.post(url1, headers=headers1)
        print(f'\033[31m[+] Status : \033[32m'+req1.json()['status'])
        print(f'\033[31m[+] Continent : \033[32m'+req1.json()['continent'])
        print(f'\033[31m[+] ContinentCode : \033[32m'+req1.json()['continentCode'])
        print(f'\033[31m[+] Country : \033[32m'+req1.json()['country'])
        print(f'\033[31m[+] CountryCode : \033[32m'+req1.json()['countryCode'])
        print(f'\033[31m[+] Region : \033[32m'+req1.json()['region'])
        print(f'\033[31m[+] RegionName : \033[32m'+req1.json()['regionName'])
        print(f'\033[31m[+] City : \033[32m'+req1.json()['city'])
        print(f'\033[31m[+] District : \033[32m'+req1.json()['district'])
        print(f'\033[31m[+] Zip : \033[32m'+req1.json()['zip'])
        print(f'\033[31m[+] Timezone : \033[32m'+req1.json()['timezone'])
        print(f'\033[31m[+] Currency : \033[32m'+req1.json()['currency'])
        print(f'\033[31m[+] Isp : \033[32m'+req1.json()['isp'])
        print(f'\033[31m[+] As : \033[32m'+req1.json()['as'])
        print(f'\033[31m[+] Asname : \033[32m'+req1.json()['asname'])
        print(f'\033[31m[+] Query : \033[32m'+req1.json()['query'])
        print(f'\033[31m[+] Lat : \033[32m'+str(req1.json()['lat']))
        print(f'\033[31m[+] Lon : \033[32m'+str(req1.json()['lon']))
        print(f'\033[31m[+] Offset : \033[32m'+str(req1.json()['offset']))
        print(f'\033[31m[+] Mobile : \033[32m'+str(req1.json()['mobile']))
        print(f'\033[31m[+] Proxy : \033[32m'+str(req1.json()['proxy']))
        print(f'\033[31m[+] Hosting : \033[32m'+str(req1.json()['hosting']))

        url2 = f'https://ipwhois.pro/{website_ip_info}?key=Sxd2AkU2ZL0YtkSR&security=1&lang=en'
        headers2 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Connection': 'keep-alive',
	    'Host': 'ipwhois.pro',
	    'Origin': 'https://ipwhois.io',
	    'Referer': 'https://ipwhois.io/',
	    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': "Windows",
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'cross-site',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36ed-with' }
        req2 = requests.get(url2, headers=headers2)
        print(f'\033[31m[+] Calling Code : \033[32m'+str(req2.json()['calling_code']))
        print(f'\033[31m[+] img Country : \033[32m'+str(req2.json()['flag']['img']))
        print(f'\033[31m[+] VPN : \033[32m'+str(req2.json()['security']['vpn']))
        print(f'\033[31m[+] TOR : \033[32m'+str(req2.json()['security']['tor']))
        print(f'\033[31m[+] Anonymous : \033[32m'+str(req2.json()['security']['anonymous']))

        req3 = requests.get(f'https://ipapi.co/{website_ip_info}/json/')
        print(f'\033[31m[+] Version : \033[32m'+str(req3.json()['version']))
        print(f'\033[31m[+] Asn : \033[32m'+str(req3.json()['asn']))
        print(f'\033[31m[+] Location : \033[32m'+str(req.json()['lat'])+','+str(req.json()['lon']))

    ipinfo()

if option == "2":
    device_hostname = socket.gethostname()
    device_IP = socket.gethostbyname(device_hostname)
    print("\033[32mDevice Host Name : "+"\033[37m"+device_hostname+"\n\033[32mDevice IP : "+"\033[31m"+device_IP)