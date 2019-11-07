import time
import math
import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
links = ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"]


class TestAnswers:
    @pytest.mark.parametrize("link", links)
    def test_answer_check(self, browser, link):
        browser.get(link)
        inpu_form = browser.find_element_by_css_selector("textarea")
        # WebDriverWait.until(ec.visibility_of(inpu_form))
        inpu_form.send_keys(str(math.log(int(time.time()))))
        browser.find_element_by_class_name("submit-submission").click()
        assert browser.find_element_by_class_name("smart-hints__hint").text == "Correct!"