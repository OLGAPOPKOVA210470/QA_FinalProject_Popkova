'@pytest.mark.api'  
import pytest
import requests
import os
import datetime
import allure
from dotenv import load_dotenv

load_dotenv()


@allure.feature("Meal Plan")
@allure.story("Create meal plan")
def test_create_meal_plan():
    with allure.step("Get API token and base URL"):
        token = os.getenv("TANDOOR_TOKEN")
        base_url = os.getenv("BASE_URL")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    with allure.step("Get list of recipes"):
        response = requests.get(f"{base_url}/api/recipe/", headers=headers)
        recipes = response.json().get("results", [])

    if not recipes:
        pytest.skip("No recipes found")

    recipe_id = recipes[0]["id"]
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    with allure.step(f"Create meal plan for recipe {recipe_id} on {tomorrow}"):
        data = {
            "recipe": recipe_id,
            "from_date": tomorrow,
            "meal_type": {"name": "lunch"},
            "servings": 2
        }
        response = requests.post(f"{base_url}/api/meal-plan/", headers=headers, json=data)

    with allure.step("Verify meal plan was created"):
        assert response.status_code in [200, 201], f"Failed: {response.text}"
        allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.JSON)