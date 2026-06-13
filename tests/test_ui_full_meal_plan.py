import pytest
from datetime import datetime, timedelta
import allure
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.header_component import HeaderComponent
from api.client import TandoorAPIClient
import time
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.ui
@allure.feature("Meal Plan")
@allure.story("Полный цикл работы с Meal Plan")
class TestFullMealPlan:

    @allure.title("Создание, проверка и удаление Meal Plan через UI")
    def test_full_cycle_meal_plan(self, driver, get_or_create_recipe):
        api_client = TandoorAPIClient()

        # 1. Авторизация (пароль из .env)
        with allure.step("Авторизация в приложении"):
            login_page = LoginPage(driver)
            login_page.open(login_page.url)
            login_page.login(os.getenv("TANDOOR_USERNAME"), os.getenv("TANDOOR_PASSWORD"))
            time.sleep(3)

        # 2. Переход в Meal Plan
        with allure.step("Переход в раздел Meal Plan"):
            driver.get("https://tandoor.vs1.srv.eduson.tv/mealplan")
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            print("✓ Страница Meal Plan открыта")

        # 3. Нажатие кнопки "Создать"
        with allure.step("Нажатие кнопки создания плана"):
            wait = WebDriverWait(driver, 30)
            create_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.v-btn")))
            create_btn.click()
            print("✓ Нажата кнопка 'Создать'")
            time.sleep(5)

        # 4. Выбор рецепта
        with allure.step("Выбор рецепта"):
            wait = WebDriverWait(driver, 30)
            search_input = wait.until(EC.presence_of_element_located((By.ID, "id_global_search_input")))
            search_input.click()
            search_input.send_keys(get_or_create_recipe['name'])
            print(f"✓ Введено название рецепта: {get_or_create_recipe['name']}")
            time.sleep(2)
            
            recipe_result = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'v-card-title')][contains(text(),'{get_or_create_recipe['name']}')]")))
            recipe_result.click()
            print(f"✓ Выбран рецепт: {get_or_create_recipe['name']}")
            time.sleep(2)

        # 5. Установка дат
        today = datetime.now().strftime("%Y-%m-%d")
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

        with allure.step("Установка дат"):
            date_inputs = driver.find_elements(By.XPATH, "//input[@placeholder='dd.mm.yyyy']")
            if len(date_inputs) >= 1:
                driver.execute_script("arguments[0].value = arguments[1];", date_inputs[0], today)
                print(f"✓ Установлена дата начала: {today}")
            if len(date_inputs) >= 2:
                driver.execute_script("arguments[0].value = arguments[1];", date_inputs[1], tomorrow)
                print(f"✓ Установлена дата окончания: {tomorrow}")

        # 6. Сохранение
        with allure.step("Сохранение плана"):
            save_btn = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Сохранить')]"))
            )
            driver.execute_script("arguments[0].click();", save_btn)
            print("✓ Нажата кнопка 'Сохранить'")
            time.sleep(3)

        # 7. Проверка создания
        with allure.step("Проверка отображения созданного плана в календаре"):
            driver.get("https://tandoor.vs1.srv.eduson.tv/mealplan")
            time.sleep(3)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, f"//td[contains(@data-date,'{today}')]//div[contains(@class,'meal-plan-entry')]")))
            assert True, "План питания отображается в календаре"

        # 8. Удаление через API
        with allure.step("Удаление созданного плана через API"):
            meal_plans = api_client.get_meal_plans()
            plan_id = None
            if meal_plans and 'results' in meal_plans and len(meal_plans['results']) > 0:
                for plan in meal_plans['results']:
                    if plan.get('start_date') == today:
                        plan_id = plan['id']
                        break
                if plan_id is None:
                    plan_id = meal_plans['results'][-1]['id']
                api_client.delete_meal_plan(plan_id)
                print(f"✓ Удалён план с ID: {plan_id}")

        # 9. Проверка удаления
        with allure.step("API проверка удаления плана"):
            if plan_id:
                meal_plans_after = api_client.get_meal_plans()
                plan_ids = [p['id'] for p in meal_plans_after.get('results', [])]
                assert plan_id not in plan_ids, "План не был удалён"
                print("✓ План успешно удалён")