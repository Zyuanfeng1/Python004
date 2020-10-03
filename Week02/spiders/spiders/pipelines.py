# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class SpidersPipeline:
    def process_item(self, item, spider):
        name = item['name']
        # item['name']="".join(item['name'].split())
        category = item['category']
        plan_date = item['plan_date']

        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='',
                               database='test',
                               charset='utf8mb4'
                               )

        # 获得cursor游标对象
        con1 = conn.cursor()

        # 操作的行数
        count = con1.execute('insert into movies values(%s,%s,%s);', (name, category, plan_date))
        count = con1.execute('commit;')

        # 获得所有查询结果
        print(con1.fetchall())

        con1.close()
        conn.close()

        # 执行批量插入
        # values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
        # cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)

        # output = f'|{name}|\t|{category}|\t|{plan_date}|\n\n'
        # with open('./maoyan2.csv', 'a', encoding='utf-8') as article:
        #     article.write(output)
        return item
