import requests
from bs4 import BeautifulSoup

url = 'https://www.bithumb.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
coins = soup.select('.coin_list tr')
with open('bithumb.csv','w', encoding='utf-8') as f:
    for coin in coins:
        name = coin.select_one('td:nth-child(1) p a strong').text.strip()
        price = coin.select_one('td:nth-child(2) strong').text.replace(',','')
        f.write(f'{name},{price}\n')