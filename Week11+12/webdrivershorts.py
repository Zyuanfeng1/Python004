import time
import lxml.etree
from fake_useragent import UserAgent
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait
import pymysql
import pandas as pd
import xlwt

try:
    # conn = pymysql.connect(host='localhost',
    #                        port=3306,
    #                        user='root',
    #                        password='',
    #                        database='test',
    #                        charset='utf8mb4'
    #                        )
    # con1 = conn.cursor()
    with open ('shorts.csv',mode='w',encoding='utf-8') as f:
        f.write('')
    browser = webdriver.Chrome()
    browser.get('https://movie.douban.com/subject/35155748/comments?status=P')
    time.sleep(3)
    for i in range(1,21):
        time.sleep(3)
        rate = browser.find_element_by_xpath(f'//*[@id="comments"]/div[{i}]/div[2]/h3/span[2]/span[2]').get_attribute('title')
        print(type(rate))
        print(rate)
        if len(rate)>4:
            rate='还行'
        time.sleep(3)
        short = browser.find_element_by_xpath(f'//*[@id="comments"]/div[{i}]/div[2]/p/span').text
        print(short)
        output=f'{rate},{short}\n'
        with open('./shorts.csv',mode='a+',encoding='utf-8') as f:
            f.write(output)
except Exception as e:
    print(e)
finally:
    pass
