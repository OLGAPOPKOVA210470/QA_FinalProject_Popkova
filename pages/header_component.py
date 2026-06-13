import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HeaderComponent(BasePage):
    # Локатор ссылки Meal Plan (иконка календаря) — несколько вариантов
    MEAL_PLAN_LINK = (By.XPATH, "//a[@href='/mealplan']")
    MEAL_PLAN_LINK_2 = (By.XPATH, "//a[contains(@href, 'mealplan')]")
    MEAL_PLAN_LINK_3 = (By.XPATH, "//i[contains(@class, 'fa-calendar')]/parent::a")
    
    # Локатор для Shopping List
    SHOPPING_LIST_LINK = (By.XPATH, "//a[@href='/shoppinglist']")
    
    # Локатор меню пользователя
    USER_MENU = (By.CSS_SELECTOR, ".v-btn--stacked, [aria-label='account']")

    @allure.step("Переход в раздел Meal Plan")
    def go_to_meal_plan(self):
        """Кликает на иконку Meal Plan с отладкой"""
        # Сохраняем текущий URL для отладки
        current_url = self.driver.current_url
        print(f"Текущий URL после логина: {current_url}")
        
        # Пробуем найти элемент разными способами
        locators = [self.MEAL_PLAN_LINK, self.MEAL_PLAN_LINK_2, self.MEAL_PLAN_LINK_3]
        
        for i, locator in enumerate(locators):
            try:
                print(f"Пробуем локатор {i+1}: {locator}")
                # Ждём элемент
                element = self.wait.until(EC.presence_of_element_located(locator))
                # Прокручиваем
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                # Ждём кликабельности
                self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                print(f"Клик成功 по локатору {i+1}")
                return
            except Exception as e:
                print(f"Локатор {i+1} не сработал: {e}")
                continue
        
        # Если ничего не сработало — сохраняем страницу для анализа
        with open("debug_after_login.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        raise Exception("Не найден Meal Plan. Сохранён debug_after_login.html")

    @allure.step("Переход в раздел Shopping List")
    def go_to_shopping_list(self):
        """Кликает на ссылку Shopping List в хедере"""
        self.click(self.SHOPPING_LIST_LINK)

    @allure.step("Проверка авторизации пользователя")
    def is_user_authenticated(self):
        """Проверяет, авторизован ли пользователь"""
        return self.is_element_present(self.USER_MENU)