import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.mark.ui
def test_open_tandoor():
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get("https://tandoor.vs1.srv.eduson.tv")
    assert "Вход" in driver.title or "Tandoor" in driver.title
    driver.quit()
    print("✅ UI тест пройден: страница открыта")