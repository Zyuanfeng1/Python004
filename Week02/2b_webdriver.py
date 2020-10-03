import time

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html

    browser.get('https://processon.com/login?f=index')
    time.sleep(1)

    # browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])
    # btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    # btm1.click()

    browser.find_element_by_xpath('//input[@name="login_email"]').send_keys('929809235@qq.com')
    browser.find_element_by_xpath('//input[@id="login_password"]').send_keys('zyfzxh')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="signin_btn"]').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="new-file"]').click()
    time.sleep(3)
    browser.find_element_by_xpath('/html/body/div[4]/div[1]/span[2]').click()

    # cookies = browser.get_cookies() # 获取cookies
    # print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    pass
