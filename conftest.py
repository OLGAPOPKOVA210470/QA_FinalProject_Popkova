import os
import pytest
import json
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from api.client import TandoorAPIClient

load_dotenv()


@pytest.fixture
def api_client():
    """Фикстура для API-клиента"""
    return TandoorAPIClient()


@pytest.fixture
def driver():
    """Фикстура для браузера с поддержкой headless для CI"""
    options = Options()
    
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def get_or_create_recipe(api_client):
    """Находит существующий рецепт или создаёт новый через импорт по ссылке"""
    response = api_client.get_recipes()
    
    if response and 'results' in response and len(response['results']) > 0:
        recipe = response['results'][0]
        return recipe
    else:
        with open('data/recipe_urls.json', 'r', encoding='utf-8') as f:
            urls = json.load(f)
        
        result = api_client.import_recipe_by_url(urls[0])
        
        if result and 'results' in result and len(result['results']) > 0:
            return result['results'][0]
        return result


# Хук для скриншотов при падении тестов
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{rep.when}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\nСкриншот сохранён: {screenshot_path}")