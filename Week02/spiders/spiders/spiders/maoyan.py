# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from spiders.items import SpidersItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        print(response.url)
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        try:
            for movie in movies[:10]:
                name = movie.xpath('./div[1]/span[@class="name "]/text()')
                item = SpidersItem()
                item['name'] = name.extract_first().strip()
                print(name.extract_first().strip())
                category = movie.xpath('./div[2]/text()')
                item['category'] = category.extract()[1].strip()
                print(category.extract()[1].strip())
                plan_date = movie.xpath('./div[4]/text()')
                item['plan_date'] = plan_date.extract()[1].strip()
                print(plan_date.extract()[1].strip())
                yield item
        except Exception as e:
            print(e)
        finally:
            pass
