"""
Тесты для проверки работы API-клиента
"""

import pytest
from datetime import datetime, timedelta
from api.client import TandoorAPIClient


@pytest.mark.api
class TestAPIClient:
    """Тесты для API-клиента"""
    
    def test_api_connection(self, api_client):
        """Проверка соединения с API"""
        result = api_client.get_recipes()
        assert 'results' in result
        print("✅ API доступен")
    
    def test_get_recipes(self, api_client):
        """Проверка получения списка рецептов"""
        result = api_client.get_recipes()
        assert 'results' in result
        assert isinstance(result['results'], list)
        print(f"✅ Получено {len(result['results'])} рецептов")
    
    def test_create_meal_plan(self, api_client, get_or_create_recipe):
        """Проверка создания плана питания"""
        today = datetime.now().strftime("%Y-%m-%d")
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        
        result = api_client.create_meal_plan(
            recipe_id=get_or_create_recipe['id'],
            start_date=today,
            end_date=tomorrow,
            meal_type=1
        )
        
        assert 'id' in result
        print(f"✅ Создан план с ID: {result['id']}")
        
        # Чистим за собой
        api_client.delete_meal_plan(result['id'])
    
    def test_get_meal_plans(self, api_client):
        """Проверка получения списка планов питания"""
        result = api_client.get_meal_plans()
        assert 'results' in result
        print(f"✅ Получено {len(result['results'])} планов")
    
    def test_get_shopping_list(self, api_client):
        """Проверка получения списка покупок"""
        result = api_client.get_shopping_list()
        assert 'results' in result
        print("✅ Список покупок получен")