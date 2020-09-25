import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd
from time import sleep

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

header = {'cookies':'id=222b81faa5c3009c||t=1600866336|et=730|cs=002213fd488c9a7fdbe1362dd7',
                    'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250?start=0&filter='
response = requests.get(myurl, headers=header)
bs_info = bs(response.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a'):
        urls =  atag.get('href')
        print(urls)
        response1 = requests.get(urls, headers=header)
        selector = lxml.etree.HTML(response1.text)
        film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
        print(f'电影名称: {film_name}')
#
#  # 电影类型
        category = selector.xpath('//*[@id="info"]/span[5]/text()')
        print(f'电影类型：{category}')
#
 # # 上映日期
        plan_date = selector.xpath('//*[@id="info"]/span[11]/text()')
        print(f'上映日期: {plan_date}')
# #
# #
        mylist = [film_name, category, plan_date]
        print(f'返回码是：{response.status_code}')

        movie1 = pd.DataFrame(data = mylist)

# # windows需要使用gbk字符集
        movie1.to_csv('./movie1.csv', mode='a',encoding='utf8', index=False, header=False)
        sleep(5)