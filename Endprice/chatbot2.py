import requests

#======================================================================================
#네트워크로 네이버 주식에서 넷플릭스 주가 가져오기
url = 'https://api.stock.naver.com/stock/NFLX.O/basic'

response = requests.get(url).json()

Netflix_closeprice = response['closePrice']

result_text = f'넷플릭스 오늘의 마감가는 {Netflix_closeprice}'
#======================================================================================


token = '1561854892:AAG2DmKoGlY1A_3SlZkcmQhzjtJcrSPAzN0'

url = f'https://api.telegram.org/bot{token}/getUpdates'

# from pprint import pprint

response1 = requests.get(url).json()

id = response1['result'][0]['message']['chat']['id']

m_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={result_text}'

requests.get(m_url)

