import requests, webbrowser, socket, os
from ast import Try
from email import header

try:
    import requests, webbrowser, socket, os
    from ast import Try
    from email import header
except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install webbrowser")
    os.system("pip install socket")
    os.system("pip install os")
    os.system("pip install ast")
    os.system("pip install email")

    os.system("clear")

#--------------------------------
Black = "\033[1;30m"       #Black
Red = "\033[1;31m"         #Red
Green = "\033[1;32m"       #Green
Yellow = "\033[1;33m"      #Yellow
Blue = "\033[1;34m"        #Blue
Purple = "\033[1;35m"      #Purple
Cyan = "\033[1;36m"        #Cyan
White = "\033[1;37m"       #White
Gray = "\033[1;39m"        #Gray
DarkRed = "\033[2;31m"     #Dark Red
DarkBlue = "\033[2;34m"    #Drak Blue
DarkPink = "\033[2;35m"    #Dark Pink
DarkCyan = "\033[2;36m"    #Dark Cyan
#--------------------------------

print("""\033[1;31m
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
print("\033[1;37mThis Tool Was Programmed By : TLER AL-BISHI \nWebsite For All Accs : \033[1;34mhttps://linktr.ee/tler.sa")
print("\033[1;37m- "*25)

print("\033[1;37m[\033[1;33m1\033[1;37m] - Website IP Info | \033[1;37m[\033[1;33m2\033[1;37m] - Your Device IP Info")
option = input("Choose A Number : \033[1;33m")

if option == "1":
    URL = input("\033[1;37m[\033[1;33m1\033[1;37m] - \033[1;31mEnter The URL \033[1;37m: \033[1;31m")
    Website_IP = socket.gethostbyname(URL)
    print(Green+"URL IP is \033[1;37m: \033[1;31m" +Website_IP)

    website_ip_info = input("\033[1;37m[\033[1;33m2\033[1;37m] - \033[1;31mEnter The IP \033[1;37m: \033[1;31m")
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
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mStatus \033[1;37m: \033[1;32m'+req1.json()['status'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mContinent \033[1;37m: \033[1;32m'+req1.json()['continent'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mContinentCode \033[1;37m: \033[1;32m'+req1.json()['continentCode'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mCountry \033[1;37m: \033[1;32m'+req1.json()['country'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mCountryCode \033[1;37m: \033[1;32m'+req1.json()['countryCode'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mRegion \033[1;37m: \033[1;32m'+req1.json()['region'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mRegionName \033[1;37m: \033[1;32m'+req1.json()['regionName'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mCity \033[1;37m: \033[1;32m'+req1.json()['city'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mDistrict \033[1;37m: \033[1;32m'+req1.json()['district'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mZip \033[1;37m: \033[1;32m'+req1.json()['zip'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mTimeZone \033[1;37m: \033[1;32m'+req1.json()['timezone'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mCurrency \033[1;37m: \033[1;32m'+req1.json()['currency'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mIsp \033[1;37m: \033[1;32m'+req1.json()['isp'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mAs \033[1;37m: \033[1;32m'+req1.json()['as'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mAsname \033[1;37m: \033[1;32m'+req1.json()['asname'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mQuery \033[1;37m: \033[1;32m'+req1.json()['query'])
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mLat \033[1;37m: \033[1;32m'+str(req1.json()['lat']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mLon \033[1;37m: \033[1;32m'+str(req1.json()['lon']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mOffset \033[1;37m: \033[1;32m'+str(req1.json()['offset']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mMobile \033[1;37m: \033[1;32m'+str(req1.json()['mobile']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mProxy \033[1;37m: \033[1;32m'+str(req1.json()['proxy']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mHosting \033[1;37m: \033[1;32m'+str(req1.json()['hosting']))

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
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mCallingCode \033[1;37m: \033[1;32m'+str(req2.json()['calling_code']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mimg Country \033[1;37m: \033[1;32m'+str(req2.json()['flag']['img']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mVPN \033[1;37m: \033[1;32m'+str(req2.json()['security']['vpn']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mTOR \033[1;37m: \033[1;32m'+str(req2.json()['security']['tor']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mAnon \033[1;37m: \033[1;32m'+str(req2.json()['security']['anonymous']))

        req3 = requests.get(f'https://ipapi.co/{website_ip_info}/json/')
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mVersion \033[1;37m: \033[1;32m'+str(req3.json()['version']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mAsn \033[1;37m: \033[1;32m'+str(req3.json()['asn']))
        print(f'\033[1;37m[\033[1;33m+\033[1;37m] \033[1;31mLocation \033[1;37m: \033[1;32m'+str(req.json()['lat'])+','+str(req.json()['lon']))

    ipinfo()

if option == "2":
    device_hostname = socket.gethostname()
    device_IP = socket.gethostbyname(device_hostname)
    print("\033[1;31mDevice Host Name \033[1;37m: \033[1;37m"+device_hostname+"\n\033[1;31mDevice IP \033[1;37m: \033[1;32m"+device_IP)

else:
    print("\033[1;31mPlease Choose A Valid Number!")
