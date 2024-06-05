from paddleocr import PaddleOCR
from selenium.webdriver.common.by import By
import time
import json

"""
    登录部分
"""

with open('setting.json', 'r') as f:
    config = json.load(f)

def try_login(driver):
    success = False
    while not success:
        try:
            login(driver)
            time.sleep(2)

        except Exception as e:
            print("登录失败:", e)
            # 如果登录失败，等待一段时间后重新尝试
            time.sleep(2)

        try:
            current_title = driver.title
            if "本科生选课" in current_title:
                print("页面标题为 '本科生选课'，开始操作...")
                success = True
        except Exception as e:
            print("发生异常：", e)



def login(driver):

    # 初始化 PaddleOCR
    ocr = PaddleOCR(use_angle_cls=False, lang='en')

    # 获取验证码图片
    captcha_element = driver.find_element(By.ID, "captcha")  # 假设验证码图片的id为 'captchaImg'
    captcha_screenshot = captcha_element.screenshot_as_png

    # 保存验证码图片
    with open("captcha.png", "wb") as file:
        file.write(captcha_screenshot)


    # 进行 OCR 识别
    result = ocr.ocr("captcha.png", cls=False)

    # 提取识别结果
    captcha_text = ""
    for line in result:
        for word in line:
            if isinstance(word, list) and len(word) == 2:
                captcha_text += word[1][0]


    print("识别的验证码文本:", captcha_text)

    # 找到并填写用户名和密码
    username = driver.find_element(By.ID, "j_username")
    password = driver.find_element(By.ID, "j_password")
    ca = driver.find_element(By.NAME, "_login_image_")

    # 输入用户名和密码
    username.send_keys(config["user"]["name"])
    password.send_keys(config["user"]["password"])
    ca.send_keys(captcha_text)

    button = driver.find_element(By.XPATH, "//a[@href='#' and contains(@onclick, 'doLogin()')]")
    button.click()