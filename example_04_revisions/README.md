# Пример 4: Управление версиями и ревизии

## Описание
Демонстрация работы с версиями миграций, управление ревизиями, зависимостями между миграциями.

## Структура проекта
```
example_04_revisions/
├── alembic/
│   ├── versions/         # Папка для миграций
│   ├── env.py
│   ├── script.py.mako
│   └── README
├── database.py           # Модели SQLAlchemy (Category, Book)
├── alembic.ini           # Конфигурация Alembic
├── requirements.txt
└── README.md
```

## Установка

1. Создайте базу данных PostgreSQL:
```sql
CREATE DATABASE demo_revisions_db;
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Модели

### Category (Категория)
- `id`: уникальный идентификатор
- `name`: название категории (уникальное)
- `description`: описание категории

### Book (Книга)
- `id`: уникальный идентификатор
- `title`: название книги
- `author`: автор книги
- `isbn`: ISBN код (уникальный)
- `category_id`: связь с категорией (Foreign Key)
- `published_year`: год издания
- `created_at`: дата добавления

## Пошаговая инструкция

### Шаг 1: Создание первой миграции (таблица categories)

Временно закомментируйте модель `Book` в `database.py`, оставив только `Category`:

```python
# class Book(Base):
#     ...
```

Создайте первую миграцию:

```bash
alembic revision --autogenerate -m "create categories table"
```

Примените миграцию:

```bash
alembic upgrade head
```

### Шаг 2: Создание второй миграции (таблица books)

Раскомментируйте модель `Book` в `database.py`.

Создайте вторую миграцию:

```bash
alembic revision --autogenerate -m "create books table"
```

Примените миграцию:

```bash
alembic upgrade head
```

### Шаг 3: Просмотр истории миграций

Посмотрите историю всех миграций:

```bash
alembic history
```

Вывод будет примерно таким:
```
<hash2> -> <hash3> (head), create books table
<hash1> -> <hash2>, create categories table
<base> -> <hash1>, initial
```

Более подробная информация:

```bash
alembic history --verbose
```

### Шаг 4: Проверка текущей версии

Узнайте, какая версия миграции применена к БД:

```bash
alembic current
```

Покажет что-то вроде:
```
<hash3> (head)
```

### Шаг 5: Переход на конкретную версию

Откатитесь к первой миграции (укажите хеш первой миграции):

```bash
alembic downgrade <hash1>
```

Проверьте текущую версию:

```bash
alembic current
```

Вернитесь на последнюю версию:

```bash
alembic upgrade head
```

### Шаг 6: Относительные переходы

Откатитесь на одну версию назад:

```bash
alembic downgrade -1
```

Продвиньтесь на две версии вперёд:

```bash
alembic upgrade +2
```

### Шаг 7: Работа с параметрами down_revision и depends_on

Откройте любой файл миграции в `alembic/versions/`. Вы увидите:

```python
revision: str = 'abc123'
down_revision: Union[str, None] = 'xyz789'  # На какую миграцию опирается
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None  # Дополнительные зависимости
```

**down_revision** — указывает на предыдущую миграцию в цепочке.

**depends_on** — позволяет указать дополнительные зависимости. Например, если миграция требует выполнения двух других миграций:

```python
depends_on = ['migration_hash_1', 'migration_hash_2']
```

### Шаг 8: Создание миграции с зависимостями (пример)

Создайте пустую миграцию:

```bash
alembic revision -m "add index to books"
```

Откройте созданный файл и вручную отредактируйте:

```python
def upgrade() -> None:
    op.create_index('idx_books_isbn', 'books', ['isbn'])

def downgrade() -> None:
    op.drop_index('idx_books_isbn', 'books')
```

Примените:

```bash
alembic upgrade head
```

## Полезные команды для работы с версиями

| Команда | Описание |
|---------|----------|
| `alembic current` | Показать текущую версию БД |
| `alembic history` | Показать историю всех миграций |
| `alembic history --verbose` | Подробная история с деталями |
| `alembic upgrade head` | Применить все миграции до последней |
| `alembic upgrade <revision>` | Перейти на конкретную версию |
| `alembic upgrade +2` | Применить 2 миграции вперёд |
| `alembic downgrade <revision>` | Откатиться к конкретной версии |
| `alembic downgrade -1` | Откатить одну миграцию назад |
| `alembic downgrade base` | Откатить все миграции |
| `alembic show <revision>` | Показать детали конкретной миграции |
| `alembic heads` | Показать последние ревизии |

## Параметры ревизии

В каждом файле миграции есть важные параметры:

- **revision**: уникальный ID миграции (генерируется автоматически)
- **down_revision**: ID предыдущей миграции (создаёт цепочку)
- **branch_labels**: метки для ветвления миграций
- **depends_on**: список ID миграций, от которых зависит текущая

## Структура цепочки миграций

```
base -> revision_1 -> revision_2 -> revision_3 (head)
```

При откате к `revision_1`:
```bash
alembic downgrade <revision_1_hash>
```

Alembic выполнит `downgrade()` для `revision_3` и `revision_2`.

## Практическое задание

1. Создайте две миграции (categories и books)
2. Примените обе миграции
3. Просмотрите историю командой `alembic history --verbose`
4. Откатитесь к первой миграции
5. Проверьте текущую версию
6. Вернитесь к последней версии
7. Создайте третью миграцию с добавлением индекса
8. Изучите параметры `revision` и `down_revision` в файлах миграций

## Визуализация зависимостей

Представьте сложный проект с параллельными миграциями:

```
       revision_A
      /
base ---> revision_1 ---> revision_2
      \
       revision_B
```

Миграция `revision_2` может зависеть от `revision_A` и `revision_B`:

```python
down_revision = 'revision_1'
depends_on = ['revision_A', 'revision_B']
```

Это гарантирует, что перед применением `revision_2` будут выполнены все зависимости.
