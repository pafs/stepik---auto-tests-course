from selenium import webdriver
import time
import unittest

class RegisterTest(unittest.TestCase):

    def test_reg(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome("C:\development\chromedriver\chromedriver.exe")
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector("input.first:required")
        first_name.send_keys("FirstName")
        second_name = browser.find_element_by_css_selector("input.second:required")
        second_name.send_keys("SecondName")
        email_field = browser.find_element_by_css_selector("input.third:required")
        email_field.send_keys("my@email.this")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_reg_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome("C:\development\chromedriver\chromedriver.exe")
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector("input.first:required")
        first_name.send_keys("FirstName")
        second_name = browser.find_element_by_css_selector("input.second:required")
        second_name.send_keys("SecondName")
        email_field = browser.find_element_by_css_selector("input.third:required")
        email_field.send_keys("my@email.this")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    unittest.main()
