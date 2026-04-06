# Пример 1: CRUD операции с FastAPI и SQLAlchemy

## Описание
Демонстрация базовых CRUD операций (Create, Read, Update, Delete) с использованием FastAPI и SQLAlchemy.

## Структура проекта
```
example_01_crud/
├── database.py       # Модели SQLAlchemy и настройка БД
├── schemas.py        # Pydantic схемы для валидации
├── main.py           # FastAPI приложение с эндпоинтами
├── test_api.http     # HTTP запросы для тестирования
├── requirements.txt  # Зависимости проекта
└── README.md         # Документация
```

## Установка

1. Создайте базу данных PostgreSQL:
```sql
CREATE DATABASE demo_crud_db;
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn main:app --reload
```

Приложение будет доступно по адресу: http://localhost:8000

Документация API: http://localhost:8000/docs

## Тестирование

Используйте файл `test_api.http` в PyCharm для тестирования всех эндпоинтов.

## Основные возможности

- **CREATE**: Создание нового пользователя
- **READ**: Получение списка пользователей и конкретного пользователя
- **UPDATE**: Обновление данных пользователя
- **DELETE**: Удаление пользователя

## Модель User

- `id`: уникальный идентификатор (primary key)
- `username`: имя пользователя (уникальное, обязательное)
- `email`: электронная почта (уникальное, обязательное)
- `full_name`: полное имя (опциональное)
