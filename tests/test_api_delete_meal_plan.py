'@pytest.mark.api'  
import pytest
import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()


def test_create_and_delete_meal_plan_via_api():
    """API тест: создать и удалить план питания"""
    
    token = os.getenv("TANDOOR_TOKEN")
    base_url = os.getenv("BASE_URL")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Шаг 1: Получить список рецептов
    response = requests.get(f"{base_url}/api/recipe/", headers=headers)
    recipes = response.json().get("results", [])
    
    if not recipes:
        pytest.skip("No recipes found")
    
    recipe_id = recipes[0]["id"]
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
    # Шаг 2: Создать план питания
    data = {
        "recipe": recipe_id,
        "from_date": tomorrow,
        "meal_type": {"name": "lunch"},
        "servings": 2
    }
    
    create_response = requests.post(f"{base_url}/api/meal-plan/", headers=headers, json=data)
    assert create_response.status_code in [200, 201]
    
    meal_plan_id = create_response.json().get("id")
    assert meal_plan_id is not None, "Meal plan ID not found"
    
    print(f"Meal plan created with ID: {meal_plan_id}")
    
    # Шаг 3: Удалить план питания
    delete_response = requests.delete(f"{base_url}/api/meal-plan/{meal_plan_id}/", headers=headers)
    assert delete_response.status_code in [200, 204]
    
    print(f"Meal plan {meal_plan_id} deleted successfully")
    
    # Шаг 4: Проверить, что план удалён
    get_response = requests.get(f"{base_url}/api/meal-plan/{meal_plan_id}/", headers=headers)
    assert get_response.status_code == 404
    
    print("API test: create and delete meal plan - PASSED")