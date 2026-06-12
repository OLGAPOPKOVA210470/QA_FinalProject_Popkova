import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.ui
class TestUIMealPlan:
    
    @pytest.fixture
    def driver(self):
        options = Options()
        if os.getenv("CI"):
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    
    @allure.feature("Meal Plan UI")
    @allure.story("Login and navigation")
    def test_login_and_open_meal_plan(self, driver):
        with allure.step("Open login page"):
            driver.get("https://tandoor.vs1.srv.eduson.tv/user/login")
        
        with allure.step("Login with credentials"):
            username = os.getenv("TANDOOR_USERNAME")
            password = os.getenv("TANDOOR_PASSWORD")
            driver.find_element(By.ID, "id_login").send_keys(username)
            driver.find_element(By.ID, "id_password").send_keys(password)
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            WebDriverWait(driver, 10).until(EC.url_contains("/"))
        
        with allure.step("Navigate to Meal Plan"):
            driver.get("https://tandoor.vs1.srv.eduson.tv/plan")
        
        with allure.step("Verify Meal Plan page"):
            assert "plan" in driver.current_url
            allure.attach(driver.get_screenshot_as_png(), "meal_plan_page", attachment_type=allure.attachment_type.PNG)
        
        print("✅ UI тест: авторизация и переход в Meal Plan успешны")