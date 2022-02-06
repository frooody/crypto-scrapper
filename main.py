from bs4 import BeautifulSoup as bs
import requests as rq
import re
import csv
import time
from time import gmtime, strftime

prices = {}

while True:
    time_now = strftime("%H_%M_%S", gmtime())
    for i in range(1, 94):
        url = f'https://coinmarketcap.com/?page={i}'
        site = rq.get(url).text
        doc = bs(site, 'html.parser')
        tbody = doc.tbody
        trs = tbody.contents
        for tr in trs[:10]:
            name, price = tr.contents[2:4]
            fixed_name = name.p.string
            fixed_price = price.span.string
            prices[fixed_name] = fixed_price
        for tr in trs[10:]:
            name, price = tr.contents[2:4]
            f_name = name.find('span', {'class': 'crypto-symbol'}).string
            f_price = price.find('span')
            fp = re.sub(r'<!-- -->', '', str(f_price))
            fp1 = re.sub(r'<span>', '', str(fp))
            fp2 = re.sub(r'</span>', '', str(fp1))
            prices[f_name] = fp2
    
    f_name = 'crypto_' + str(time_now).replace(' ', '') + '.csv'
    file = open(f_name, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(["Currency", "Price"])
    writer.writerow([time_now])

    for key, value in prices.items():
        writer.writerow([key, value.replace(',', "")])
    
    print(str(time_now) + f_name)
    time.sleep(60)