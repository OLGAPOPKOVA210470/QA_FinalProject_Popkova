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

```
TANDOOR_PROJECT/
├── .github/workflows/
│   └── main.yml
├── api/
│   └── client.py
├── data/
│   └── recipe_urls.json
├── pages/
│   ├── base_page.py
│   ├── header_component.py
│   └── login_page.py
├── tests/
│   ├── test_api_client.py
│   ├── test_api_delete_meal_plan.py
│   ├── test_api_shopping_list.py
│   ├── test_api_simple.py
│   ├── test_meal_plan_api.py
│   ├── test_ui_full_meal_plan.py
│   ├── test_ui_meal_plan.py
│   ├── test_ui_shopping_list.py
│   └── test_ui_simple.py
├── conftest.py
├── generate_test_data.py
├── pytest.ini
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Реализованные сценарии

### API тесты (выполнены)
1. `test_api_connection` — проверка соединения с API
2. `test_get_recipes` — получение списка рецептов
3. `test_create_meal_plan` — создание плана питания
4. `test_get_meal_plans` — получение списка планов
5. `test_get_shopping_list` — получение списка покупок
6. `test_api_delete_meal_plan` — удаление плана питания

### UI тесты (выполнены)
1. `test_open_tandoor` — открытие главной страницы
2. `test_login_and_open_meal_plan` — авторизация и переход в Meal Plan
3. `test_full_cycle_meal_plan` — полный цикл: создание, проверка, удаление плана через UI
4. `test_shopping_list_page` — проверка доступности страницы Shopping List

## Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/OLGAPOPKOVA210470/QA_FinalProject_Popkova.git
cd QA_FinalProject_Popkova
```

### 2. Создать виртуальное окружение
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Создать файл `.env`
```
BASE_URL=https://tandoor.vs1.srv.eduson.tv
TANDOOR_USERNAME=your_email@example.com
TANDOOR_PASSWORD=your_password
TANDOOR_TOKEN=your_token
```

### 5. Запустить тесты
```bash
pytest tests/ -v
```

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
8. Скопируйте токен и вставьте в файл `.env`

## Известные проблемы

1. **GitLab**: регистрация невозможна из-за гео-ограничений. Использован GitHub Actions (разрешено ревьюером).

2. **UI-тесты**: в текущей версии тестового стенда кнопка "Создать" на странице Meal Plan загружается нестабильно. Основной упор сделан на API-тесты, которые полностью покрывают требования ТЗ и работают стабильно.

3. **Отображение "ERROR" в календаре**: на тестовом сервере Eduson в некоторых ячейках календаря Meal Plan отображается надпись "ERROR" вместо названия рецепта. Это связано с битыми ссылками на рецепты на стороне сервера и не является ошибкой автотестов. Тесты корректно работают при наличии валидных данных.