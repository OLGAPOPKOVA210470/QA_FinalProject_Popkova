from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class MealPlanPage(BasePage):
    """Страница Meal Plan"""
    
    # Локаторы
    CREATE_BUTTON = (By.CSS_SELECTOR, "button[title='Создать'], button:contains('Create')")
    RECIPE_INPUT = (By.CSS_SELECTOR, "[placeholder*='Рецепт'], [placeholder*='Recipe']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CALENDAR_CELL = (By.CSS_SELECTOR, ".calendar-day, [class*='day']")
    
    def click_create_button(self):
        """Нажать кнопку 'Создать'"""
        self.click(self.CREATE_BUTTON)
    
    def select_recipe(self, recipe_name):
        """Выбрать рецепт из выпадающего списка"""
        element = self.find_element(self.RECIPE_INPUT)
        element.send_keys(recipe_name)
        element.send_keys(Keys.ENTER)
    
    def save_meal_plan(self):
        """Сохранить план питания"""
        self.click(self.SAVE_BUTTON)
    
    def is_meal_plan_visible(self):
        """Проверить, появился ли план питания в календаре"""
        try:
            self.find_element(self.CALENDAR_CELL)
            return True
        except:
            return False