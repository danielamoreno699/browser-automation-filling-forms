import sys
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import requests
import random

#local from selenium.webdriver.chrome.service import Service
# service = Service("absolute path of chromediver.exe")

random_checkbox = ''
label = ''
random_checkboxes = []

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"] )
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options)
    driver.get("https://www.toluna.com/group/guest/account/profile-surveys")
    return driver

# retreiving data from form
def get_data():
    url = "https://www.toluna.com/group/guest/account/profile-surveys"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # sys.stdout.reconfigure(encoding='utf-8')

    print(soup)

    # td_elements = soup.find_all('div', id="group_20001420")
   
    # if td_elements:
    #     for td_element in td_elements:
    #         print(td_element)
            # input_checkboxes = td_element.find_all('input', type='checkbox')
            # print(td_element.get_text())
            # for checkbox in input_checkboxes:
            #     random_checkboxes.append(checkbox)          
    # else:
    #     print("Element not found")

# function to select random checkbox
# def select_random_checkbox():
#     if random_checkboxes:
#         random_checkbox = random.choice(random_checkboxes)
#         print('random selection', random_checkbox)
#         return random_checkbox
#     else:
#         print("No checkboxes found")
#         return None


# print(get_data())
# print(random_checkboxes)
# print(select_random_checkbox())

def main():
   driver = get_driver()
   time.sleep(2)
   driver.find_element("id", "_com_liferay_login_web_portlet_LoginPortlet_login").send_keys("danielamoreno699@gmail.com")
   time.sleep(2)
   driver.find_element("id", "_com_liferay_login_web_portlet_LoginPortlet_password").send_keys("1020769229mariaD&" + Keys.RETURN)
   time.sleep(2)
   driver.find_element("id", "_com_liferay_login_web_portlet_LoginPortlet_button-submit").click()
   time.sleep(5)
   print(driver.current_url)

print(main())

# print(get_data())
# print(main())
# if __name__ == "__main__":
    # random_checkbox = get_data()
    # print(random_checkbox)
    # main()