import requests
from decouple import config

base = 'https://api.telegram.org'
token = config('TOKEN')
url = f'{base}/bot{token}/getUpdates'
res = requests.get(url)
data = res.json()

# 1. 나의 chat_id를 가져옴
chat_id = data['result'][0]['message']['chat']['id']

# 2. 해당하는 chat_id에 메세지를 보내기

text = 'python send message'
send_url = f'{base}/bot{token}/sendMessage?text={text}&chat_id={chat_id}'
requests.get(send_url)