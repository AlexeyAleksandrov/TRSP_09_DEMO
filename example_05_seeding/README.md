# Пример 5: База данных - наполнение данными (seeding)

## Описание
Демонстрация заполнения базы данных начальными данными (seeding) через миграции Alembic.

## Структура проекта
```
example_05_seeding/
├── alembic/
│   ├── versions/
│   │   ├── 001_create_tables.py      # Создание таблиц
│   │   ├── 002_seed_countries.py     # Заполнение стран
│   │   └── 003_seed_cities.py        # Заполнение городов
│   ├── env.py
│   ├── script.py.mako
│   └── README
├── database.py           # Модели SQLAlchemy (Country, City)
├── alembic.ini           # Конфигурация Alembic
├── requirements.txt
└── README.md
```

## Установка

1. Создайте базу данных PostgreSQL:
```sql
CREATE DATABASE demo_seeding_db;
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Модели

### Country (Страна)
- `id`: уникальный идентификатор
- `name`: название страны (уникальное)
- `code`: код страны (ISO 3166-1 alpha-3, уникальный)
- `capital`: столица
- `population`: население

### City (Город)
- `id`: уникальный идентификатор
- `name`: название города
- `country_code`: код страны
- `population`: население
- `description`: описание города

## Что такое Seeding?

**Seeding (засеивание)** — это процесс заполнения базы данных начальными данными. Эти данные могут быть:

- **Тестовыми** — для разработки и тестирования
- **Справочными** — страны, валюты, категории
- **Начальными** — администратор по умолчанию, базовые настройки

## Зачем использовать миграции для seeding?

1. **Версионность** — данные версионируются вместе со схемой БД
2. **Воспроизводимость** — легко развернуть проект с данными на новой машине
3. **Откат** — можно откатить не только структуру, но и данные
4. **Командная работа** — все разработчики получают одинаковые данные

## Пошаговая инструкция

### Шаг 1: Применение всех миграций

Примените все три миграции сразу:

```bash
alembic upgrade head
```

Alembic выполнит:
1. Миграцию 001 — создаст таблицы `countries` и `cities`
2. Миграцию 002 — заполнит таблицу `countries` данными
3. Миграцию 003 — заполнит таблицу `cities` данными

### Шаг 2: Проверка данных

Подключитесь к БД и проверьте данные:

```sql
-- Проверка стран
SELECT * FROM countries;

-- Проверка городов
SELECT * FROM cities;

-- Города с населением больше 10 млн
SELECT name, population FROM cities WHERE population > 10000000;

-- Города России
SELECT name, population FROM cities WHERE country_code = 'RUS';
```

### Шаг 3: Просмотр истории миграций

```bash
alembic history --verbose
```

Вы увидите три миграции:
- `001` — create tables
- `002` — seed countries
- `003` — seed cities

### Шаг 4: Откат данных

Откатите последнюю миграцию (cities):

```bash
alembic downgrade -1
```

Проверьте БД — таблица `cities` будет пустой.

Вернитесь обратно:

```bash
alembic upgrade +1
```

## Методы заполнения данных

### Метод 1: op.bulk_insert() (рекомендуется)

Используется в миграциях 002 и 003. Позволяет эффективно вставить много записей:

```python
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

countries_table = table(
    'countries',
    column('id', Integer),
    column('name', String),
    column('code', String)
)

def upgrade() -> None:
    data = [
        {'id': 1, 'name': 'Россия', 'code': 'RUS'},
        {'id': 2, 'name': 'США', 'code': 'USA'}
    ]
    op.bulk_insert(countries_table, data)

def downgrade() -> None:
    op.execute("DELETE FROM countries WHERE code IN ('RUS', 'USA')")
```

**Преимущества:**
- Эффективная вставка множества записей
- Типизированные данные
- Чистый Python-код

### Метод 2: op.execute() (для простых случаев)

Выполнение сырого SQL:

```python
def upgrade() -> None:
    op.execute("""
        INSERT INTO countries (id, name, code, capital, population) VALUES
        (1, 'Россия', 'RUS', 'Москва', 146000000),
        (2, 'США', 'USA', 'Вашингтон', 331000000)
    """)

def downgrade() -> None:
    op.execute("DELETE FROM countries WHERE id IN (1, 2)")
```

**Преимущества:**
- Простота для небольших данных
- Прямой контроль над SQL

**Недостатки:**
- Нет типизации
- Менее читаемо

### Метод 3: Загрузка из файла (для больших объёмов)

Создайте файл `seed_data.py` с данными:

```python
COUNTRIES = [
    {'id': 1, 'name': 'Россия', 'code': 'RUS', ...},
    # ... много данных
]
```

В миграции:

```python
from seed_data import COUNTRIES

def upgrade() -> None:
    op.bulk_insert(countries_table, COUNTRIES)
```

## Структура миграции с seeding

```python
"""seed countries

Revision ID: 002
Revises: 001
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

revision: str = '002'
down_revision: Union[str, None] = '001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Определение структуры таблицы для seeding
countries_table = table(
    'countries',
    column('id', Integer),
    column('name', String),
    column('code', String),
    column('capital', String),
    column('population', Integer)
)

def upgrade() -> None:
    # Данные для вставки
    initial_countries = [
        {'id': 1, 'name': 'Россия', 'code': 'RUS', 'capital': 'Москва', 'population': 146000000},
    ]
    
    # Вставка данных
    op.bulk_insert(countries_table, initial_countries)

def downgrade() -> None:
    # Удаление данных при откате
    op.execute("DELETE FROM countries WHERE code = 'RUS'")
```

## Важные моменты

### 1. Порядок миграций важен!

Сначала создайте таблицы, затем заполняйте данные:
```
001_create_tables -> 002_seed_data
```

### 2. Downgrade должен удалять данные

В функции `downgrade()` важно удалить именно те данные, которые были добавлены в `upgrade()`:

```python
def downgrade() -> None:
    op.execute("DELETE FROM cities WHERE id BETWEEN 1 AND 10")
```

### 3. Используйте WHERE для безопасности

Не используйте `DELETE FROM table` без WHERE — это удалит ВСЕ данные!

```python
# ПЛОХО
op.execute("DELETE FROM countries")

# ХОРОШО
op.execute("DELETE FROM countries WHERE code IN ('RUS', 'USA')")
```

### 4. Внешние ключи

Если есть связи между таблицами, заполняйте данные в правильном порядке:
1. Сначала родительские таблицы (countries)
2. Потом дочерние таблицы (cities)

## Практическое задание

1. Примените все миграции: `alembic upgrade head`
2. Проверьте данные в БД
3. Откатите миграцию с городами: `alembic downgrade -1`
4. Убедитесь, что таблица `cities` пустая
5. Примените миграцию обратно: `alembic upgrade head`
6. Создайте свою миграцию с seeding для таблицы `regions`

## Дополнительное задание

Создайте новую миграцию, которая добавит ещё 5 стран:

```bash
alembic revision -m "add more countries"
```

В файле миграции:

```python
def upgrade() -> None:
    more_countries = [
        {'id': 9, 'name': 'Канада', 'code': 'CAN', 'capital': 'Оттава', 'population': 38000000},
        # ... добавьте ещё 4 страны
    ]
    op.bulk_insert(countries_table, more_countries)

def downgrade() -> None:
    op.execute("DELETE FROM countries WHERE id BETWEEN 9 AND 13")
```

Примените миграцию и проверьте результат!

## Когда использовать seeding в миграциях?

**✅ Используйте для:**
- Справочных данных (страны, валюты)
- Ролей пользователей (admin, user, moderator)
- Начальных настроек системы
- Тестовых данных для разработки

**❌ Не используйте для:**
- Больших объёмов данных (используйте отдельные скрипты)
- Пользовательских данных
- Данных, которые часто меняются
