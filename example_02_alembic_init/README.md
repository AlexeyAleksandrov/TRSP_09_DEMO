# Пример 2: Начало работы с Alembic

## Описание
Демонстрация инициализации и настройки Alembic для работы с миграциями базы данных.

## Структура проекта
```
example_02_alembic_init/
├── alembic/
│   ├── versions/         # Папка для миграций (пока пустая)
│   ├── env.py            # Настройка окружения Alembic
│   ├── script.py.mako    # Шаблон для генерации миграций
│   └── README
├── database.py           # Модель SQLAlchemy (Product)
├── alembic.ini           # Конфигурация Alembic
├── .env.example          # Пример файла с переменными окружения
├── requirements.txt      # Зависимости проекта
└── README.md             # Документация
```

## Установка

1. Создайте базу данных PostgreSQL:
```sql
CREATE DATABASE demo_alembic_db;
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. (Опционально) Создайте файл `.env` на основе `.env.example`:
```bash
cp .env.example .env
```

## Основные команды Alembic

### 1. Инициализация Alembic (уже выполнено в этом примере)
```bash
alembic init alembic
```

### 2. Проверка текущей версии базы данных
```bash
alembic current
```

### 3. Просмотр истории миграций
```bash
alembic history
```

### 4. Создание первой миграции (будет выполнено в следующем примере)
```bash
alembic revision --autogenerate -m "initial migration"
```

### 5. Применение миграций
```bash
alembic upgrade head
```

## Настройка Alembic

### alembic.ini
Основной конфигурационный файл, содержит:
- Путь к папке с миграциями (`script_location = alembic`)
- URL подключения к базе данных (`sqlalchemy.url`)
- Настройки логирования

**Важно:** В продакшене лучше использовать переменные окружения вместо хардкода URL в `alembic.ini`.

### env.py
Файл окружения, который:
- Импортирует модели SQLAlchemy
- Настраивает метаданные (`target_metadata = Base.metadata`)
- Определяет функции для онлайн/офлайн миграций

**Ключевой момент:** В `env.py` мы импортируем `Base` из `database.py`, чтобы Alembic знал о наших моделях:
```python
from database import Base
target_metadata = Base.metadata
```

## Модель Product

Пример простой модели для демонстрации:
- `id`: уникальный идентификатор (primary key)
- `name`: название продукта (обязательное)
- `description`: описание продукта (опциональное)
- `price`: цена продукта (обязательное)

## Следующие шаги

После настройки Alembic можно переходить к созданию миграций (см. Пример 3).
