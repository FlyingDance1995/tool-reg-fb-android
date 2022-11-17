import asyncio
import re
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\\setup\\chromedriver", port=9090)
# driver2 = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\\setup\\chromedriver", port=9091)
# driver3 = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\\setup\\chromedriver", port=9092)


def load_web(device_id):
    url = "https://temp-mail.org/vi/"
    if device_id == "emulator-5554":
        driver.get(url)
    # elif device_id == "f521da0e":
    #     driver3.get(url)
    # else:
    #     driver2.get(url)
    # pyautogui.countdown(10)


def handle_get_mail(device_id, p_count):
    if p_count < 10:
        get_new_email(device_id)
        pyautogui.countdown(10)
        try:
            if device_id == "emulator-5554":
                mail = driver.find_element(By.ID, "mail")
            # elif device_id == "f521da0e":
            #     mail = driver3.find_element(By.ID, "mail")
            # else:
            #     mail = driver2.find_element(By.ID, "mail")
        except Exception as e:
            pyautogui.countdown(10)
            if device_id == "emulator-5554":
                mail = driver.find_element(By.ID, "mail")
            # elif device_id == "f521da0e":
            #     mail = driver3.find_element(By.ID, "mail")
            # else:
            #     mail = driver2.find_element(By.ID, "mail")

        if not mail or len(mail.get_attribute("value").strip()) == 0 or "đang tải" in mail.get_attribute(
                "value").lower():
            pyautogui.countdown(10)
            if device_id == "emulator-5554":
                mail = driver.find_element(By.ID, "mail")
            # elif device_id == "f521da0e":
            #     mail = driver3.find_element(By.ID, "mail")
            # else:
            #     mail = driver2.find_element(By.ID, "mail")

        if not mail or len(mail.get_attribute("value").strip()) == 0 or "đang tải" in mail.get_attribute(
                "value").lower():
            p_count += 1
            mail = handle_get_mail(device_id, p_count)
        return mail
    else:
        return None


def min_window(device_id):
    if device_id == "emulator-5554":
        driver.minimize_window()
    # elif device_id == "f521da0e":
    #     driver3.minimize_window()
    # else:
    #     driver2.minimize_window()


def max_window(device_id):
    if device_id == "emulator-5554":
        driver.maximize_window()
    # elif device_id == "f521da0e":
    #     driver3.maximize_window()
    # else:
    #     driver2.maximize_window()


def close_window(device_id):
    if device_id == "emulator-5554":
        driver.delete_all_cookies()
    # elif device_id == "f521da0e":
    #     driver3.delete_all_cookies()
    # else:
    #     driver2.delete_all_cookies()


def get_mail(device_id):
    max_window(device_id)
    try:
        mail = handle_get_mail(device_id, 0)
        print("mail.get_attribute('value'): ", mail.get_attribute("value"))
    except Exception as e:
        mail = handle_get_mail(device_id, 0)
        print("error: ", e)
    min_window(device_id)
    return None if mail is None else mail.get_attribute("value")


def get_new_email(device_id):
    try:
        if device_id == "emulator-5554":
            btn = driver.find_element(By.ID, "click-to-delete")
            btn.click()
        # elif device_id == "f521da0e":
        #     btn = driver3.find_element(By.ID, "click-to-delete")
        #     btn.click()
        # else:
        #     btn = driver2.find_element(By.ID, "click-to-delete")
        #     btn.click()
    except Exception as e:
        if device_id == "emulator-5554":
            pyautogui.countdown(10)
            btn = driver.find_element(By.ID, "click-to-delete")
            btn.click()
            print("error: ", e)
        # elif device_id == "f521da0e":
        #     pyautogui.countdown(10)
        #     btn = driver3.find_element(By.ID, "click-to-delete")
        #     btn.click()
        #     print("error: ", e)
        # else:
        #     pyautogui.countdown(10)
        #     btn = driver2.find_element(By.ID, "click-to-delete")
        #     btn.click()
        #     print("error: ", e)


def refresh_mail_box(device_id):
    if device_id == "emulator-5554":
        btn = driver.find_element(By.ID, "click-to-refresh")
        btn.click()
    # elif device_id == "f521da0e":
    #     btn = driver3.find_element(By.ID, "click-to-refresh")
    #     btn.click()
    # else:
    #     btn = driver2.find_element(By.ID, "click-to-refresh")
    #     btn.click()


def get_code(device_id, p_count):
    if p_count < 30:
        max_window(device_id)
        pyautogui.countdown(10)
        try:
            if device_id == "emulator-5554":
                inbox_datalist = driver.find_element_by_xpath("//div[@class='inbox-dataList']")
            # elif device_id == "f521da0e":
            #     inbox_datalist = driver3.find_element_by_xpath("//div[@class='inbox-dataList']")
            # else:
            #     inbox_datalist = driver2.find_element_by_xpath("//div[@class='inbox-dataList']")
            inbox_datalist = inbox_datalist.get_attribute("innerHTML")
            inbox_datalist = str(inbox_datalist)
            phoneNumRegex = re.findall(r'(\d{5}) là mã', inbox_datalist)
            fb_code = ""
            if len(phoneNumRegex) > 0:
                fb_code = phoneNumRegex[0]
            if fb_code is None or len(fb_code.strip()) == 0:
                min_window(device_id)
                return None
            else:
                print(f"fb_code: {fb_code}")
                min_window(device_id)
                return fb_code
        except Exception as e:
            p_count += 1
            print("error: ", e)
            min_window(device_id)
            return get_code(device_id, p_count)
    else:
        min_window(device_id)
        return None
