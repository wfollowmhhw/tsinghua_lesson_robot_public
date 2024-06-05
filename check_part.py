from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def check_lesson(driver,target_class,target_number):

    success = False

    # 切换到名为 "right" 的 frame
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "right")))

    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframe2")))

    time.sleep(2)

    # 查找所有符合条件的 <tr> 元素
    tr_elements = driver.find_elements(By.XPATH, "//tr[@class='trr2']")

    for tr_element in tr_elements:
        # print(tr_element)
        # print(tr_element.get_attribute('outerHTML'))
        # 检查每个 <tr> 元素的子元素是否符合要求
        td_element_2 = tr_element.find_element(By.XPATH, "./td[3]")
        td_element_4 = tr_element.find_element(By.XPATH, "./td[5]")
        if target_class in td_element_2.text and target_number in td_element_4.text:
            print("找到符合条件的 <tr> 元素")
            success = True  # 找到符合条件的元素后，停止循环
            break

    driver.switch_to.default_content()

    return success

