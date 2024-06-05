from set_driver import set_driver
import time
from login_part import try_login
from go_in_choose_part import try_choose_part
import pandas as pd
from check_part import check_lesson
from submit_part import submit_lesson
from term_part import choose_term
from wait_part import wait_to_time
import datetime
import json


if __name__ == "__main__":

    with open('setting.json', 'r') as f:
        config = json.load(f)

    # 初始化Firefox浏览器
    driver = set_driver()

    target_datetime_str = config["time"]["start"]

    target_datetime = datetime.datetime.strptime(target_datetime_str, "%Y-%m-%d %H:%M:%S")

    # 减去5分钟
    target_datetime_1 = target_datetime - datetime.timedelta(minutes=5)

    target_datetime_2 = target_datetime - datetime.timedelta(seconds=15)

    wait_to_time(target_datetime_1)

    # 访问登录页面
    driver.get("https://zhjwxk.cic.tsinghua.edu.cn/xklogin.do")

    # 等待页面加载
    time.sleep(2)

    try_login(driver)

    term_option = config["term"]

    choose_term(driver, term_option)
    time.sleep(2)

    wait_to_time(target_datetime_2)

    try_choose_part(driver)

    choose_lessons = pd.read_csv("lessons.csv", encoding="utf-8", dtype=str)

    for index, row in choose_lessons.iterrows():
        times = 0
        while True:
            submit_lesson(driver, row.iloc[0], row.iloc[1], row.iloc[2])
            if check_lesson(driver, row.iloc[0], row.iloc[1]):
                break
            if times == 2:
                break
            times += 1

    # 关闭浏览器
    driver.quit()

