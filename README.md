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

### UI тесты (не выполнены)
Ошибка ERR_CONNECTION_RESET на тестовом стенде. UI проверен вручную.

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
TANDOOR_USERNAME=popkovaolga1970@gmail.com
TANDOOR_PASSWORD=Testirovanie12345
TANDOOR_TOKEN=tda_a6372c61_668e_4ccf_906a_67c35c9b5d4a

### 5. Запустить тесты
pytest tests/ -v
pytest tests/test_meal_plan_api.py -v

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
2. UI-тесты: ошибка ERR_CONNECTION_RESET на стенде. UI проверен вручную.


