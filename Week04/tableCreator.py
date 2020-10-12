import pandas as pd
import numpy as np

group = ['x','y','z']
table1 = pd.DataFrame({
    "name":[group[x] for x in np.random.randint(0,len(group),20)] ,
    "id":np.random.randint(5,15,20),
"age":np.random.randint(15,50,20)
    })
table2 = pd.DataFrame({
    "name":[group[x] for x in np.random.randint(0,len(group),20)] ,
    "id":np.random.randint(990,1000,20),
"order_id":np.random.randint(40,50,20)
    })
table1 = pd.DataFrame({
    "name":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "id":np.random.randint(990,1000,10),
    })

data3 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10),
    "salary":np.random.randint(5,50,10),
    })

# 一对一
pd.merge(data1, data2)

# 多对一
pd.merge(data3, data2, on='group')

# 多对多
pd.merge(data3, data2)

# 连接键类型，解决没有公共列问题
pd.merge(data3, data2, left_on= 'age', right_on='salary')

# 连接方式
# 内连接，不指明连接方式，默认都是内连接
pd.merge(data3, data2, on= 'group', how='inner')
# 左连接 left
# 右连接 right
# 外连接 outer

# 纵向拼接
pd.concat([data1, data2])


 
