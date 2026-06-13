# Дипломный проект: Тестирование Meal Plan (Tandoor)

## Студент
Ольга Попкова

## Описание проекта
Автоматизация smoke-тестирования раздела Meal Plan веб-приложения Tandoor.

## Технологии
- Python
- Pytest
- Requests
- Allure
- GitHub Actions

## Структура проекта
TANDOOR_PROJECT/
├── .github/workflows/
│ └── main.yml
├── api/
│ └── client.py
├── data/
│ ├── recipe_urls.json
│ └── recipe_ids.json
├── pages/
│ ├── base_page.py
│ ├── header_component.py
│ └── login_page.py
├── tests/
│ ├── test_api_simple.py
│ ├── test_meal_plan_api.py
│ ├── test_api_shopping_list.py
│ ├── test_api_delete_meal_plan.py
│ ├── test_ui_simple.py
│ └── test_ui_meal_plan.py
├── generate_test_data.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env
└── README.md  

## Реализованные сценарии

### API тесты (выполнены)
1. test_api_connection — проверка соединения с API
2. test_create_meal_plan — создание плана питания
3. test_get_shopping_list — получение списка покупок
4. test_create_and_delete_meal_plan_via_api — удаление плана питания

### UI тесты (выполнены)
1. test_open_tandoor — открытие главной страницы
2. test_login_and_open_meal_plan — авторизация и переход в Meal Plan

## Установка и запуск

### 1. Клонировать репозиторий
git clone https://github.com/OLGAPOPKOVA210470/QA_FinalProject_Popkova.git
cd QA_FinalProject_Popkova

### 2. Создать виртуальное окружение
python -m venv venv
venv\Scripts\activate

### 3. Установить зависимости
pip install -r requirements.txt

### 4. Создать файл .env
BASE_URL=https://tandoor.vs1.srv.eduson.tv
TANDOOR_USERNAME=your_email@example.com
TANDOOR_PASSWORD=your_password
TANDOOR_TOKEN=your_token

### 5. Запустить тесты
pytest tests/ -v

## CI/CD
Автоматический запуск API тестов через GitHub Actions при каждом push.

## Как получить API-токен

1. Зайдите на https://tandoor.vs1.srv.eduson.tv
2. Войдите под своей учётной записью
3. Нажмите на аватар → Настройки (Settings)
4. В левом меню выберите API
5. Нажмите Create Token
6. Назовите токен (например, "Diplom")
7. Выберите права: read и write
8. Скопируйте токен и вставьте в файл .env

## Известные проблемы

1. GitLab: регистрация невозможна из-за гео-ограничений. Использован GitHub Actions.
2. UI-тесты в CI выполняются в headless-режиме (без графического интерфейса), локально все тесты проходят успешно.
