import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from api.client import TandoorAPIClient

load_dotenv()


@pytest.fixture
def api_client():
    return TandoorAPIClient()


@pytest.fixture
def get_or_create_recipe(api_client):
    recipes = api_client.get_recipes()
    
    if recipes.get("results"):
        recipe_id = recipes["results"][0]["id"]
        return recipe_id
    else:
        import json
        data_path = os.path.join(os.path.dirname(__file__), "data", "recipe_urls.json")
        with open(data_path, "r") as f:
            urls = json.load(f)["recipes"]
        
        response = api_client.import_recipe_by_url(urls[0])
        recipe_id = response.get("id")
        return recipe_id


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("CI"):
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()