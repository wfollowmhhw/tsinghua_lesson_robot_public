from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
import time


def handle_all_alerts(driver):
    while True:
        try:
            # 尝试等待并处理alert
            alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert出现: {alert_text}")
            alert.accept()  # 接受alert
            print("已接受alert，继续检查")
        except:
            # 当没有alert时退出循环
            print("没有更多alert")
            break


def handle_alert(driver):
    try:
        alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alert出现: {alert_text}")
        alert.accept()  # 接受alert
        print("已接受alert，继续执行")
    except Exception as e:
        print(f"处理alert时出错: {e}")


def submit_lesson(driver, target_class, target_number, target_type):
    # 切换到名为 "right" 的 frame
    WebDriverWait(driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "right")))

    WebDriverWait(driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframe1")))
    time.sleep(2)

    if target_type == "必修":
        type_element = driver.find_element(By.ID, "mod0")
    elif target_type == "限选":
        type_element = driver.find_element(By.ID, "mod1")
    elif target_type == "任选":
        type_element = driver.find_element(By.ID, "mod2")
    elif target_type == "体育":
        type_element = driver.find_element(By.ID, "mod3")
    elif target_type == "重修":
        type_element = driver.find_element(By.ID, "mod4")
    else:
        print("无效的课程类型")
        return

    type_element.click()

    time.sleep(2)

    class_element = driver.find_element(By.ID, "p_kch")

    class_element.send_keys(target_class)

    search_element = driver.find_element(By.XPATH, "//input[@value='查询']")

    search_element.click()

    handle_all_alerts(driver)

    # 查找所有符合条件的 <tr> 元素
    tr_elements = driver.find_elements(By.XPATH, "//tr[@class='trr2']")

    for tr_element in tr_elements:
        try:
            # 检查每个 <tr> 元素的子元素是否符合要求
            td_element_2 = tr_element.find_element(By.XPATH, "./td[2]")
            td_element_3 = tr_element.find_element(By.XPATH, "./td[3]")
            if target_class in td_element_2.text and target_number in td_element_3.text:
                print("找到符合条件的 <tr> 元素")
                td_element_1 = tr_element.find_element(By.XPATH, "./td[1]/input")
                td_element_1.click()
                break  # 找到符合条件的元素后，停止循环
        except NoSuchElementException as e:
            print(f"查找<td>元素时出错: {e}")
        except UnexpectedAlertPresentException as e:
            print(f"点击<td>元素时出现未预期的alert: {e}")
            handle_alert(driver)  # 处理alert

    try:
        submit_element = driver.find_element(By.XPATH, "//input[@value='提交']")
        submit_element.click()
        handle_alert(driver)  # 提交后处理alert
    except NoSuchElementException as e:
        print(f"查找提交按钮时出错: {e}")
    except UnexpectedAlertPresentException as e:
        print(f"点击提交按钮时出现未预期的alert: {e}")
        handle_alert(driver)  # 处理alert

    handle_all_alerts(driver)

    driver.switch_to.default_content()

