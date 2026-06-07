from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц (Page Object Model)"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, url):
        """Открыть URL"""
        self.driver.get(url)
    
    def find_element(self, locator):
        """Найти один элемент"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        """Кликнуть по элементу"""
        self.find_element(locator).click()
    
    def type_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_title(self):
        """Получить заголовок страницы"""
        return self.driver.title