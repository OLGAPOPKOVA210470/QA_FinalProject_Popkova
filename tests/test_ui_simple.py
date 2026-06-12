'@pytest.mark.ui'  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_open_tandoor():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-web-security')
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://tandoor.vs1.srv.eduson.tv")
    
    assert "Вход" in driver.title or "Tandoor" in driver.title
    
    driver.quit()
    print("✅ UI тест пройден: страница открыта")