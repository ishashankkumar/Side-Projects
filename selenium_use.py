from fake_useragent import UserAgent
from selenium import webdriver
from random import randrange
import time

ua = UserAgent(verify_ssl=False)
user_agent = ua.random

print("USER AGENT: " + user_agent)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=" + user_agent)
driver = webdriver.Chrome(chrome_options=chrome_options)


def getCode():
    id = randrange(100000000000000)
    url = "https://www.papajohnsfeedback.com/GBR?GUID=" + str(id)

    print(url)

    driver.get(url)
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    driver.find_element_by_xpath(
        "//div[contains(@class, 'Opt1')]/span").click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    driver.find_element_by_xpath(
        "//div[contains(@title, 'Highly Satisfied')]").click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    stars = driver.find_elements_by_css_selector("[title^='Highly Satisfied']")
    for div in stars:
        time.sleep(1)
        div.click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    driver.find_element_by_xpath(
        "//td[contains(@class, 'Opt5')]/span").click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    driver.find_element_by_xpath(
        "//div[contains(@class, 'Opt1')]/span").click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    driver.find_element_by_xpath(
        "//td[contains(@class, 'Opt2')]/span").click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    driver.find_element_by_xpath(
        "//div[contains(@class, 'Opt6')]/span").click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

    code = driver.find_element_by_class_name(
        'ValCode').get_attribute("innerHTML").split(' ')[2]

    return code


codes = []

for i in range(0, 10):
    c = getCode()
    print("CODE: " + c)
    codes.append(c)
    time.sleep(3)

print(codes)

driver.quit()
