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
sleep(5)

for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'},limit=10):
     for atag in tags.find_all('a'):
        urls = 'https://maoyan.com' + atag.get('href')
        print(urls)
        response1 = requests.get(urls, headers=header)
        selector = lxml.etree.HTML(response1.text)
        film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
        print(f'电影名称: {film_name}')
#
#  # 电影类型
        category = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()')
        print(f'电影类型：{category}')
#
 # # 上映日期
        plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
        print(f'上映日期: {plan_date}')
# #
# #
        mylist = [film_name, category, plan_date]
        #print(f'返回码是：{response.status_code}')

        movie1 = pd.DataFrame(data = mylist)

# # windows需要使用gbk字符集


        movie1.to_csv('./movie1.csv', mode='a',encoding='utf8', index=False, header=False)

        sleep(5)