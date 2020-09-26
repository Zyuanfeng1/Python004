import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd
from time import sleep

user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'

header = {'cookies':'LREF=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT; httponly',
                    'user-agent': user_agent}

myurl = 'https://maoyan.com/films?showType=3&offset=0'
response = requests.get(myurl, headers=header)
# print(response.text)
bs_info = bs(response.text, 'html.parser')
for tags in bs_info.find_all('div',attrs={'class':'movie-hover-info'},limit=10):
   film_name=tags.find('span',attrs={'class':'name'}).text
   print(film_name)
   category=[]
   for atag in tags.find_all('div',attrs={'class':'movie-hover-title'}):
       category.append(atag.get_text().split())
   kind=category[1]
   print(category[1])
   plan_date=category[3]
   print(category[3])
   sleep(5)
   mylist = [film_name,kind, plan_date]
   movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
   movie1.to_csv('./maoyan.csv', mode='a',encoding='utf8', index=False, header=False)