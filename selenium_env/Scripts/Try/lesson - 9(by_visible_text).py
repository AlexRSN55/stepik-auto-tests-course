from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import time


def calc(x, y):
    result = int(x) + int(y)
    return str(result)


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    print("value:", x)

    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    print("value:", y)

    sum = calc(x,y)
    print(sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)
    button = browser.find_element_by_css_selector('.btn.btn-default')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()