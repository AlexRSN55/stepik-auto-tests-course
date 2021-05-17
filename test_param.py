import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    time.sleep(5)


@pytest.mark.parametrize("url", ["236895", "236896", "236897", "236898", "236899",
                                 "236903", "236904", "236905"])
class TestMainPages():
    def test_pages_search_answer(self, browser, url):
        link = (f"https://stepik.org/lesson/{url}/step/1/")

        browser.get(link)
        time.sleep(5)

        answer = math.log(int(time.time()))

        text_cor = browser.find_element_by_css_selector(".textarea.string-quiz__textarea.ember-text-area.ember-view")
        text_cor.send_keys(str(answer))

        button = browser.find_element_by_css_selector('.submit-submission')
        button.click()

        time.sleep(5)

        message = browser.find_element_by_css_selector(".smart-hints__hint")
        assert "Correct!" in message.text

        time.sleep(5)


if __name__ == "__main__":
    print("All tests passed!")