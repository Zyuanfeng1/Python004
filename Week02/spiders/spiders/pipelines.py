# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class SpidersPipeline:
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='',
                               database='test',
                               charset='utf8mb4'
                               )
        # 获得cursor游标对象
        self.con1 = self.conn.cursor()
    def process_item(self, item, spider):
        name = item['name']
        category = item['category']
        plan_date = item['plan_date']
        print(name)
        print(category)
        print(plan_date)
        # 操作的行数
        count = self.con1.execute('insert into movies values(%s,%s,%s);', (name, category, plan_date))
        count = self.con1.execute('commit;')
        # 执行批量插入
        # values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
        # cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)
        return item
    def close_spider(self,spider):
        self.con1.close()
        self.conn.close()

