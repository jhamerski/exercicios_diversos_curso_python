from bs4 import BeautifulSoup
import time
from datetime import date, datetime
import requests

i = 1
while True:
    html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/1443/saojose-sc").content
    soup = BeautifulSoup(html, 'html.parser')
    min = soup.find("span", class_="_margin-r-20")
    if i == 1:
        atual = min

    i = i + 1
    max = soup.find("span", id_="max-temp-1")
    data = datetime.strftime(date.today(), '%d/%m/%Y')
    print(f'{i} - Aguardando alterar temp...')
    if min != atual:
        atual = min
        print(f'Temperatura para {data} MIN: {min.string} ')
        break
    time.sleep(60)
