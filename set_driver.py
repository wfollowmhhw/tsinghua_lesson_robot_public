from selenium.webdriver.firefox.options import Options
from selenium import webdriver

def set_driver():

    # 设置Firefox选项
    options = Options()
    options.set_preference("security.tls.version.min", 1)
    options.set_preference("security.tls.version.max", 4)
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0")
    options.add_argument('--ignore-certificate-errors')
    options.set_preference("network.proxy.type", 0)  # 0 表示没有代理
    options.add_argument("--headless")

    # 初始化Firefox浏览器
    driver = webdriver.Firefox(options=options)

    return driver