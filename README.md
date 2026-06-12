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
```bash
git clone https://github.com/OLGAPOPKOVA210470/QA_FinalProject_Popkova.git
cd QA_FinalProject_Popkova
2. Создать виртуальное окружение
bash
python -m venv venv
venv\Scripts\activate
3. Установить зависимости
bash
pip install -r requirements.txt
4. Создать файл .env
env
BASE_URL=https://tandoor.vs1.srv.eduson.tv
TANDOOR_USERNAME=your_email@example.com
TANDOOR_PASSWORD=your_password
TANDOOR_TOKEN=your_token
5. Запустить тесты
bash
pytest tests/ -v
CI/CD
Автоматический запуск API тестов через GitHub Actions при каждом push.

Как получить API-токен
Зайдите на https://tandoor.vs1.srv.eduson.tv

Войдите под своей учётной записью

Нажмите на аватар → Настройки (Settings)

В левом меню выберите API

Нажмите Create Token

Назовите токен (например, "Diplom")

Выберите права: read и write

Скопируйте токен и вставьте в файл .env

Известные проблемы
GitLab: регистрация невозможна из-за гео-ограничений. Использован GitHub Actions.

UI-тесты в CI выполняются в headless-режиме (без графического интерфейса), локально все тесты проходят успешно.