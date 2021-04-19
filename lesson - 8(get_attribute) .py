# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/math.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
# #Проверяем зачение атрибута "required" у "I'm the robot".
#     people_radio = browser.find_element_by_id("robotCheckbox")
#     the_robot = people_radio.get_attribute("required")
#     print("value of I'm the robot:", the_robot)
#     assert the_robot is not None, "the_robot is not selected by default"
#
# finally:
#     time.sleep(10)

from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    print("value:", x)
    # x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    check1 = browser.find_element_by_css_selector(".check-input")
    check1.click()

    radio1 = browser.find_element_by_id("robotsRule")
    radio1.click()

    button = browser.find_element_by_css_selector('.btn.btn-default')
    button.click()

  # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()