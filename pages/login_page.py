import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    URL = "https://tandoor.vs1.srv.eduson.tv/"

    # Точные локаторы с главной страницы логина
    USERNAME_INPUT = (By.ID, "id_login")
    PASSWORD_INPUT = (By.ID, "id_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn-success[type='submit']")

    @allure.step("Открыть страницу логина")
    def open(self, url=None):
        self.driver.get(self.URL)
        return self

    @allure.step("Выполнить вход пользователем {username}")
    def login(self, username, password):
        # Ждём поле username
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        
        # Вводим username
        username_field = self.driver.find_element(*self.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(username)
        print(f"✓ Введён username: {username}")
        
        # Вводим password
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        print("✓ Введён password")
        
        # Небольшая пауза перед кликом
        time.sleep(0.5)
        
        # Нажимаем кнопку входа
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()
        print("✓ Нажата кнопка входа")
        
        # Ждём перехода со страницы логина
        time.sleep(3)
        
        return self

    @property
    def url(self):
        return self.URL