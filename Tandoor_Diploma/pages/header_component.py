from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HeaderComponent(BasePage):
    """Компонент верхней панели навигации"""
    
    MEAL_PLAN_LINK = (By.XPATH, "//a[contains(@href, 'plan')]")
    SHOPPING_LIST_LINK = (By.XPATH, "//a[contains(@href, 'shopping')]")
    USER_MENU = (By.CSS_SELECTOR, ".dropdown-menu-right, [class*='user']")
    
    def go_to_meal_plan(self):
        self.click(self.MEAL_PLAN_LINK)
    
    def go_to_shopping_list(self):
        self.click(self.SHOPPING_LIST_LINK)
    
    def is_user_authenticated(self):
        try:
            self.find_element(self.USER_MENU)
            return True
        except:
            return False