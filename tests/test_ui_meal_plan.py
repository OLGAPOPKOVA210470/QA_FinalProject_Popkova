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


class TestUIMealPlan:
    
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
    @allure.story("Open page")
    def test_open_tandoor_page(self, driver):
        """Простой UI тест: открыть главную страницу Tandoor"""
        driver.get("https://tandoor.vs1.srv.eduson.tv/")
        assert "Tandoor" in driver.title or "Вход" in driver.title
        print("✅ Страница открыта")