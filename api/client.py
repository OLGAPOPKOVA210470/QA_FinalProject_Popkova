import requests
import os
from dotenv import load_dotenv

load_dotenv()


class TandoorAPIClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.token = os.getenv("TANDOOR_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        response.raise_for_status()
        return response.json()

    # Методы для работы с рецептами
    def get_recipes(self):
        return self._make_request("GET", "/api/recipe/")

    def import_recipe_by_url(self, url):
        return self._make_request("POST", "/api/recipe/import/", json={"url": url})

    def delete_recipe(self, recipe_id):
        return self._make_request("DELETE", f"/api/recipe/{recipe_id}/")

    # Методы для работы с планами питания
    def create_meal_plan(self, recipe_id, start_date, end_date, meal_type=1):
        """Создаёт план питания с обязательным полем meal_type"""
        data = {
            "recipe": recipe_id,
            "start_date": start_date,
            "end_date": end_date,
            "meal_type": meal_type
        }
        return self._make_request("POST", "/api/meal-plan/", json=data)

    def get_meal_plans(self):
        return self._make_request("GET", "/api/meal-plan/")

    def get_meal_plan(self, plan_id):
        return self._make_request("GET", f"/api/meal-plan/{plan_id}/")

    def delete_meal_plan(self, plan_id):
        return self._make_request("DELETE", f"/api/meal-plan/{plan_id}/")

    def get_shopping_list(self):
        return self._make_request("GET", "/api/shopping-list/")