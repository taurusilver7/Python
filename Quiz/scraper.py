#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/Gyronax-Rubber-Nunchaku-Handle-9-inch/dp/B07SW5G3W9/ref=pd_rhf_gw_p_img_9?_encoding=UTF8&psc=1&refRID=3ZGX6FTGD7K496AAVPA6'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
conv_price = float(price[0:5])


print(title.strip())