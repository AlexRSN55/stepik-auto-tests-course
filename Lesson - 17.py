from selenium import webdriver
import time
import unittest


class TestInput(unittest.TestCase):
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def test_input(self):
        self.assertNotEqual(self.browser.find_element_by_css_selector(".first_block .form-control.first")
                         .send_keys("Alex"), " ")

    def test_input2(self):
        self.assertNotEqual(self.browser.find_element_by_css_selector('.first_block .form-control.second')
                         .send_keys("Rusinov"), "Enter second name")

    def test_input3(self):
        self.assertNotEqual(self.browser.find_element_by_css_selector('.first_block .form-control.third')
                         .send_keys("alex@mail.su"), "Enter email")

    def push_button(self):
        self.assertNotEqual(self.browser.find_element_by_css_selector(".button.btn").click(), "button click")

    def welcome_text(self):
        self.assertEqual(self.browser.find_element_by_tag_name("h1"),
                         "Congratulations! You have successfully registered!")
        # self.assertEqual("Congratulations! You have successfully registered!")
    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
    # # закрываем браузер после всех манипуляций
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
    print("All tests passed!")