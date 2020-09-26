# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline:
    def process_item(self, item, spider):
        name = item['name']
        #item['name']="".join(item['name'].split())
        category = item['category']
        plan_date = item['plan_date']
        output = f'|{name}|\t|{category}|\t|{plan_date}|\n\n'
        with open('./maoyan2.csv', 'a', encoding='utf-8') as article:
            article.write(output)
        return item