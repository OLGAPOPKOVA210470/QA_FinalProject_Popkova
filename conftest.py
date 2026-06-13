import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from api.client import TandoorAPIClient

load_dotenv()


@pytest.fixture
def api_client():
    """Фикстура: возвращает API клиента"""
    return TandoorAPIClient()


@pytest.fixture
def get_or_create_recipe(api_client):
    """Фикстура: находит существующий рецепт или создаёт новый через API"""
    recipes = api_client.get_recipes()
    
    if recipes.get("results"):
        recipe_id = recipes["results"][0]["id"]
        print(f"Using existing recipe with ID: {recipe_id}")
        return recipe_id
    else:
        # Импортируем рецепт из тестовых данных
        import json
        data_path = os.path.join(os.path.dirname(__file__), "data", "recipe_urls.json")
        with open(data_path, "r") as f:
            urls = json.load(f)["recipes"]
        
        response = api_client.import_recipe_by_url(urls[0])
        recipe_id = response.get("id")
        print(f"Created new recipe with ID: {recipe_id}")
        return recipe_id


@pytest.fixture
def driver():
    """Фикстура: возвращает драйвер браузера с поддержкой headless для CI"""
    options = Options()
    if os.getenv("CI"):
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()