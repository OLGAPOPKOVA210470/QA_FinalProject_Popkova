from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации"""
    
    # Локаторы
    USERNAME_INPUT = (By.ID, "id_login")
    PASSWORD_INPUT = (By.ID, "id_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    def login(self, username, password):
        """Выполнить вход"""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)