import pytest
from datetime import datetime
import allure
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.ui
@allure.feature("Shopping List")
class TestShoppingList:

    @allure.title("Проверка Shopping List")
    def test_shopping_list_page(self, driver):
        """Простой тест: проверить, что страница Shopping List доступна"""

        # 1. Авторизация
        with allure.step("Авторизация в приложении"):
            login_page = LoginPage(driver)
            login_page.open(login_page.url)
            login_page.login(os.getenv("TANDOOR_USERNAME"), os.getenv("TANDOOR_PASSWORD"))
            print("✓ Авторизация выполнена")

        # 2. Переход в Shopping List напрямую
        with allure.step("Переход в Shopping List"):
            driver.get("https://tandoor.vs1.srv.eduson.tv/shopping")
            time.sleep(5)
            print("✓ Страница Shopping List открыта")

        # 3. Проверка, что страница загрузилась
        with allure.step("Проверка загрузки страницы"):
            body_text = driver.find_element(By.TAG_NAME, "body").text
            print(f"✓ Длина текста на странице: {len(body_text)}")
            
            # Проверяем, что страница не пустая
            assert len(body_text) > 50, "Страница Shopping List пустая"
            
            # Проверяем, что есть заголовок
            assert "Список покупок" in body_text or "Shopping" in body_text or "Ingredient" in body_text, \
                "Страница не похожа на Shopping List"
            
            print("✓ Shopping List страница работает корректно")

        print("\n" + "=" * 40)
        print("✅ ТЕСТ ПРОЙДЕН: Shopping List доступен")
        print("=" * 40)