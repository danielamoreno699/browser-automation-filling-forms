import sys
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import requests
import random
#local from selenium.webdriver.chrome.service import Service
# service = Service("absolute path of chromediver.exe")
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"] )
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options)
    driver.get("https://as-c1-web07.opinion.life/WebProd/cgi-bin/AskiaExt.dll?Action=DoInterview&Survey=8SH2AW7UZHNBY234&Intvw=8SH1PDLCPE55H75T&Mri=eg==")
    return driver

# retreiving data from form
def get_data():
    url = "https://as-c1-web07.opinion.life/WebProd/cgi-bin/AskiaExt.dll?Action=DoInterview&Survey=8SH2AW7UZHNBY234&Intvw=8SH1PDLCPE55H75T&Mri=eg=="
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    sys.stdout.reconfigure(encoding='utf-8')

    td_elements = soup.find_all('td', class_="myresponse askia-response")
    random_checkbox = ''
    if td_elements:
        for td_element in td_elements:
            input_checkbox = td_element.find_all('input', type='checkbox')
            print(td_element.get_text())
            if input_checkbox:
                random_idx = random.randint(0, len(input_checkbox)-1)
                random_checkbox = input_checkbox[random_idx]
                
            #     for input_check in input_checkbox:
            #         print(input_check.get('name'))
    else:
        print("Element not found")

    print(f"Selected checkbox: {random_checkbox.get('id')}")


def main():
    driver = get_driver()
   

    print(driver.current_url)

# print(main())


print(get_data())