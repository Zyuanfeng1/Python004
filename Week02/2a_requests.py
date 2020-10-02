import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent' : ua.random,
'Referer' : 'https://shimo.im'
}

s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
login_url = 'https://shimo.im/login?from=home'
form_data = {
'mobile':'13770188924',
'password':'zyfzxh'
}
response = s.post(login_url, data=form_data, headers=headers)

with open('profile.html','w+') as f:
    f.write(response.text)


