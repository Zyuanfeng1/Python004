import pymysql
import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv('shortsModified.csv',header=None,names=['star','rate','short'])
print(df)
conn = create_engine('mysql+mysqldb://root:@localhost:3306/test?charset=utf8')

pd.io.sql.to_sql(df,'shorts',con=conn,schema='test',if_exists='append',index=False)
#关闭
conn.dispose()
# con1.execute('insert into movies values(%s,%s,%s);', (name, category, plan_date))
# con1.execute('commit;')