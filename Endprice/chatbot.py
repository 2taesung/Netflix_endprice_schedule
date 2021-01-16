import requests
from bs4 import BeautifulSoup


# 챗봇 
# 넷플 주식 데이터 크롤링
# 변수 없어도 될듯
# 챗봇과 주식 연결
# 일단 매일
# 평일만은 연구 해보자

Netflix_naver_url = 'https://m.stock.naver.com/worldstock/index.html#/stock/NFLX.O/total'

response = requests.get(Netflix_naver_url).text

# print(response)
soup = BeautifulSoup(response, 'html.parser')

print(soup)
print(soup.select_one('#content'))
Netflix_endprice = soup.select_one('#content > div.GraphMain_mainGraph__AOW1s.GraphMain_FALLING__1d1yB > div.GraphMain_frameGraph__2UNJX > div.GraphMain_stockInfo__31Xpb > strong')
# Netflix_endprice = soup.select_one('#content > div.GraphMain_mainGraph__AOW1s.GraphMain_FALLING__1d1yB > div.GraphMain_frameGraph__2UNJX > div.GraphMain_stockInfo__31Xpb > strong').text


print(Netflix_endprice)