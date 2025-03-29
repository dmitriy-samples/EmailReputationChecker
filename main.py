import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('API')
url = 'https://emailrep.io/query/'


def get_status(email: str, url: str, headers: dict):
    new_url = url + email.strip().replace("@", "%40")
    response = requests.get(url=new_url, headers=headers)
    text = response.json()
    status = text['reputation']
    print(f"Checking {email.strip()}  status is  {status}", )
    return status


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://emailrep.io/",
    "Cookie": f"key={key}",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

with open('email_list.txt', 'r', encoding='utf-8') as file:
    email_list = file.readlines()

email_status_list = []
for email in email_list:
    data = str(get_status(email=email, url=url, headers=headers))
    email_status_list.append(str(email).strip() + '    ' + data)

with open('output.txt', 'w', encoding='utf-8') as file:
    for email_with_status in email_status_list:
        file.write(f"{email_with_status}\n")

print('Work is done')
