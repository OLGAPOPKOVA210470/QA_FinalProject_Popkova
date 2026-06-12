'@pytest.mark.api'  
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def test_api_connection():
    """Verify API is accessible and token is valid"""
    token = os.getenv("TANDOOR_TOKEN")
    base_url = os.getenv("BASE_URL")

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{base_url}/api/recipe/", headers=headers)

    assert response.status_code == 200
    print("API connection successful")