from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def choose_part(driver):
    # 切换到名为 "tree" 的 frame
    WebDriverWait(driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "tree")))

    try:
        link_element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "一级选课"))
        )

        link_element.click()
    except TimeoutException:
        # 如果在2秒内没有找到link_element
        # 查找并点击带有部分文本“选课操作”的 <a> 元素
        link_element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "选课操作"))
        )

        link_element.click()

        link_element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "一级选课"))
        )

        link_element.click()

    # 切换回主内容
    driver.switch_to.default_content()


def check(driver):
    WebDriverWait(driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "right")))
    try:
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'iframe1'))
        )
        result = True
    except TimeoutException:
        # 如果在1秒内没有找到iframe，返回False
        result = False

    driver.switch_to.default_content()

    return result

def try_choose_part(driver):
    while True:
        choose_part(driver)
        if check(driver):
            break