from selenium import webdriver
import time
import os


try:

    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Alex")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Rusinov")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("alex@gmail.com")

    current_dir = os.path.abspath(os.path.dirname("/Users/alexr/environments/selenium_env/Scripts/Try/"))
    file_name = '../selenium_env/Scripts/Try/empty_file.txt'
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_name('file')
    element.send_keys(file_path)


    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()