import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def api_client():
    from api.client import TandoorAPIClient
    return TandoorAPIClient()