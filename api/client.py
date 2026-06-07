import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TandoorAPIClient:
    """Клиент для взаимодействия с API Tandoor"""

    def __init__(self):
        self.base_url = os.getenv('BASE_URL')
        self.token = os.getenv('TANDOOR_TOKEN')

        if not self.base_url or not self.token:
            raise ValueError("BASE_URL or TANDOOR_TOKEN not set in .env")

        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        logger.info(f"API client initialized. URL: {self.base_url}")

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = self.headers.copy()

        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))

        try:
            logger.info(f"Sending {method} request to {url}")
            response = requests.request(method=method, url=url, headers=headers, **kwargs)
            response.raise_for_status()

            if not response.text:
                return True
            return response.json()

        except requests.exceptions.RequestException as e:
            logger.error(f"API request error: {e}")
            raise

    def get_recipes(self):
        """Get list of all recipes"""
        endpoint = "/api/recipe/"
        return self._make_request('GET', endpoint)

    def create_meal_plan(self, recipe_id, from_date, meal_type_name="lunch", servings=1):
        """Create a meal plan for specific date"""
        endpoint = "/api/meal-plan/"
        data = {
            "recipe": recipe_id,
            "from_date": from_date,
            "meal_type": {"name": meal_type_name},
            "servings": servings
        }
        logger.info(f"Creating meal plan: {data}")
        return self._make_request('POST', endpoint, json=data)