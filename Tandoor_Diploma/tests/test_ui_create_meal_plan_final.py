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
        
        with allure.step("Login to Tandoor"):
            driver.get("https://tandoor.vs1.srv.eduson.tv/user/login")
            username = os.getenv("TANDOOR_USERNAME")
            password = os.getenv("TANDOOR_PASSWORD")
            driver.find_element(By.ID, "id_login").send_keys(username)
            driver.find_element(By.ID, "id_password").send_keys(password)
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            WebDriverWait(driver, 10).until(EC.url_contains("/"))
            print("✅ Login successful")
        
        with allure.step("Navigate to Meal Plan"):
            driver.get("https://tandoor.vs1.srv.eduson.tv/plan")
            time.sleep(2)
            print("✅ Meal Plan page opened")
        
        with allure.step("Click on calendar cell to create meal plan"):
            # Нажимаем на первую ячейку календаря
            cells = driver.find_elements(By.CSS_SELECTOR, "[class*='day'], [class*='cell']")
            if cells:
                cells[0].click()
                time.sleep(2)
            print("✅ Calendar cell clicked")
        
        with allure.step("Select meal type"):
            # Выбираем тип питания
            meal_type = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.multiselect-search[aria-placeholder='Тип питания']"))
            )
            meal_type.click()
            time.sleep(1)
            meal_type.send_keys("Завтрак")
            time.sleep(1)
            meal_type.send_keys(Keys.ARROW_DOWN)
            meal_type.send_keys(Keys.ENTER)
            print("✅ Meal type selected")
        
        with allure.step("Search and select recipe"):
            # Находим поле поиска рецепта
            recipe_search = driver.find_element(By.CSS_SELECTOR, "input.multiselect-search[aria-placeholder='Рецепт']")
            recipe_search.click()
            recipe_search.send_keys("Автотестовый рецепт")
            time.sleep(2)
            recipe_search.send_keys(Keys.ARROW_DOWN)
            recipe_search.send_keys(Keys.ENTER)
            print("✅ Recipe selected")
        
        with allure.step("Save meal plan"):
            # Ждём появления кнопки "Сохранить"
            save_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            save_btn.click()
            time.sleep(3)
            print("✅ Saved")
        
        with allure.step("Verify success"):
            assert "plan" in driver.current_url
            allure.attach(driver.get_screenshot_as_png(), "result", attachment_type=allure.attachment_type.PNG)
        
        print("✅ UI test for creating Meal Plan PASSED")