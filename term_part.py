import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def choose_term(driver,term_value):
    WebDriverWait(driver, 2).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "tree")))
    time.sleep(1)

    choose_element = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.NAME, "menu1"))
    )

    choose_element.click()

    try:
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[@value='{term_value}' and @selected='selected']"))
        )
    except TimeoutException:
        term_element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[@value='{term_value}']"))
        )
        term_element.click()

    driver.switch_to.default_content()