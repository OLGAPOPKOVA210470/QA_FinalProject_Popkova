'@pytest.mark.api'  
import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def test_get_shopping_list():
    """API тест: получить список покупок"""
    
    token = os.getenv("TANDOOR_TOKEN")
    base_url = os.getenv("BASE_URL")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(f"{base_url}/api/shopping-list/", headers=headers)
    
    assert response.status_code == 200
    assert "results" in response.json()
    
    print("✅ API test: shopping list accessible")