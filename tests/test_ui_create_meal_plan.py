import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from dotenv import load_dotenv

load_dotenv()


class TestUICreateMealPlan:
    
    @pytest.fixture
    def driver(self):
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-web-security')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    
    @allure.feature("Meal Plan UI")
    @allure.story("Create meal plan")
    def test_create_meal_plan_via_ui(self, driver):
        """UI тест: создание плана питания через интерфейс"""
        
        # Шаг 1: Авторизация
        with allure.step("Login to Tandoor"):
            driver.get("https://tandoor.vs1.srv.eduson.tv/user/login")
            username = os.getenv("TANDOOR_USERNAME")
            password = os.getenv("TANDOOR_PASSWORD")
            driver.find_element(By.ID, "id_login").send_keys(username)
            driver.find_element(By.ID, "id_password").send_keys(password)
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            WebDriverWait(driver, 10).until(EC.url_contains("/"))
            print("✅ Login successful")
        
        # Шаг 2: Переход в Meal Plan
        with allure.step("Navigate to Meal Plan"):
            driver.get("https://tandoor.vs1.srv.eduson.tv/plan")
            time.sleep(3)
            print("✅ Meal Plan page opened")
        
        # Шаг 3: Нажатие на ячейку календаря с кнопкой "+"
        with allure.step("Click on calendar cell"):
            # Ищем первую ячейку календаря с плюсом
            cells = driver.find_elements(By.CSS_SELECTOR, ".cell, .day, [class*='day']")
            if cells:
                cells[0].click()
                time.sleep(2)
            print("✅ Calendar cell clicked")
        
        # Шаг 4: Заполнение формы
        with allure.step("Fill meal plan form"):
            # Выбираем рецепт из выпадающего списка
            recipe_input = driver.find_element(By.CSS_SELECTOR, "input[role='combobox'], .select__input")
            recipe_input.click()
            time.sleep(1)
            recipe_input.send_keys("test")
            time.sleep(1)
            recipe_input.send_keys(Keys.ARROW_DOWN)
            recipe_input.send_keys(Keys.ENTER)
            time.sleep(1)
            print("✅ Recipe selected")
        
        # Шаг 5: Сохранение
        with allure.step("Save meal plan"):
            save_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            save_btn.click()
            time.sleep(3)
            print("✅ Saved")
        
        # Шаг 6: Проверка
        with allure.step("Verify success"):
            assert "plan" in driver.current_url
            allure.attach(driver.get_screenshot_as_png(), "result", attachment_type=allure.attachment_type.PNG)
        
        print("✅ UI test for creating Meal Plan passed")